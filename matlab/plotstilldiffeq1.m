% plotstilldiffeq1
% Still info for a pot still with no colomn.


clear
load stillvle.mat
temp=vleimport(:,1); % Imported VLE data for Water/ethanol
x2=vleimport(:,2);
y2=vleimport(:,3);
x1=1-x2;
y1=1-y2;

xhold=[0:0.1:1]; % Place holders for graphs.
yhold=xhold;

[fittemp1,goftemp1]=fit(y1,temp,'poly9'); % Fit Temp data to Vapor mole fraction
% figure(2)
% clf
% plot(fittemp1,y1,temp)
% hold on
% plot(x1,temp)
% title('Ethanol')
% legend('Fit Dew','Dew Point','Bubble Point')
% ylabel('Temp ?C')
% xlabel('Mole Fraction Ethanol')

[fit1,gof1]=fit(x1,y1,'poly9'); % Fit VLE data.
% figure(3)
% clf
% plot(fit1,x1,y1)
% hold on
% plot(xhold,yhold)
% title('VLE Ethanol')

% Possible Starting Values
abvi=12; % percent alcohol by volume
totvoli=6; % Gallons

abvi=abvi/100; % fraction alcohol by volume
lpgal=3.78541; % liters per gallon
totvoli=totvoli*lpgal; % Volume in liters
ethvoli=totvoli*abvi; % Liters pure ethanol
watervoli=totvoli-ethvoli; % Liters pure waters

ethden=0.789; % g/ml, density of ethanol
waterden=1.0; % g/ml, density of water
ethmw=46.07; % g/mol, MW ethnol
watermw=18.01; % g/mol, MW water

ethmoli=ethvoli*(ethden*1000)/ethmw; % Initial moles of ethanol present
watermoli=watervoli*(waterden*1000)/watermw; % Initial moles of water present
totmoli=ethmoli+watermoli; % Total moles in initial wash

x1i=ethmoli/(totmoli); % Liquid mole fraction ethanol
y1i=vlewaterethanol2(x1i); % Vapor mole fraction ethanol
y2i=1-y1i;

% Quick Thoeretical ABV for initial runnings of binary system.
ethvolf=y1i*ethmw/(ethden*1000);
watervolf=y2i*watermw/(waterden*1000);
abvf=(ethvolf/(ethvolf+watervolf))*100;


clear x1 x2 y1 y2 t x
xinitial=[0 totmoli x1i]; % [D W x1i]
tspan=[0:0.01:200];
[t,x]=ode45(@stilldiffeq1,tspan,xinitial);

% Output of Diffeq Equation
data=[t x];
D=x(:,1);
W=x(:,2);
x1=x(:,3);
x2=1-x1;
y1=vlewaterethanol(x1);
y2=1-y1;
vaportemp=fittemp1(y1);

% Normalized
nD=D/max(D);
nW=W/max(W);
nx1=x1/max(x1);
nx2=x2/max(x2);

% 1 mole basis to find volume changes.
basis=1; % mole
y1d=(y1*ethmw)/ethden; % volume ethanol per mole D @ time t.
y2d=(y2*watermw)/waterden; % voume water per mole D @ time t.
totd=(y1d+y2d); % Total volume per mole D @ time t.
abvd=(y1d./totd)*100; % Abv coming out at time t.
my1=mean(y1);
my2=mean(y2);

% Mean abv
volmy1=(my1*ethmw)/ethden;
volmy2=(my2*watermw)/waterden;
avabv=(volmy1/(volmy1+volmy2))*100;

% ABV final wash
volx1f=(x1(end)*ethmw)/ethden;
volx2f=(x2(end)*watermw)/waterden;
abvw=volx1f/(volx1f+volx2f);

for i=1:length(D)-1
    volout(i,1)=totd(i)*(D(i+1)-D(i));
end

totalvolout(1)=volout(1);
for i=2:length(volout)
    totalvolout(i)=sum(volout(1:i));
end

figure(4)
clf
subplot(2,1,1)
plot(t(2:end),totalvolout,t(2:end),[totvoli*1000-totalvolout]);
title('Volume Changes')
xlabel('Time')
ylabel('mL of Fluid')
legend('D','W')

subplot(2,1,2)
plotyy(t,x1,t,y1)
title('Mole Fraction')
ylabel('Mole Fraction')
xlabel('Time')
legend('x1,ethanol','y1,ethanol')

figure(5)
clf
pax=plotyy(totalvolout,abvd(2:end),totalvolout,vaportemp(2:end));
title('Exiting ABV')
ylabel(pax(1),'%ABV')
ylabel(pax(2),'Temp C')
xlabel('mL')

%% Check with book method

f=1./(y1-x1);

[fit2,gof2]=fit(x1,f,'power2');

int1=integrate(fit2,x1,x1(end));
area=int1(1);
Wfinal=totmoli*exp(-area);
yav=(totmoli*x1(1)-Wfinal*x1(end))/D(end);

[area Wfinal W(end)]

figure(5)
clf
pax=plotyy(x1,f,x1,int1);
ylabel(pax(1),'1/(y1-x1)')
ylabel(pax(2),'Integral')
xlabel('x1')
title('Graphical Integration')

data=[abvd(end) avabv totalvolout(end) abvw];
info=dataset({data,'finalABV','meanABV','totalvol','washABV'})
