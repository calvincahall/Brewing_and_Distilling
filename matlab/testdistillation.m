% TEST Distillation

temp=vleimport(:,1);
x2=vleimport(:,2);
y2=vleimport(:,3);
x1=1-x2;
y1=1-y2;

% figure(1)
% plot(x2,temp,y2,temp)
% 
% figure(2)
% plot(x1,temp,y1,temp)
% title('Ethanol')
% legend('Bubble Point','Dew Point')
% ylabel('Temp ?C')
% xlabel('Mole Fraction Ethanol')

xhold=[0:0.1:1];
yhold=xhold;

[fit1,gof1]=fit(x1,y1,'poly9')

figure(3)
clf
plot(fit1,x1,y1)
hold on
plot(xhold,yhold)
title('VLE Ethanol')

fit1(0.1)
% vlewaterethanol(0.1)

%%
% We have 15% alcohol by volume

abvi=15; % percent alcohol by volume
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

x1i=ethmoli/(ethmoli+watermoli);
% y1i=fit1(x1i)
y1i=vlewaterethanol2(x1i);

y1f=y1i;
y2f=1-y1f;

ethvolf=y1f*ethmw/(ethden*1000);
watervolf=y2f*watermw/(waterden*1000);

abvf=(ethvolf/(ethvolf+watervolf))*100

%% Plot Diffeq
% 
% xinitial=[0 ethmoli x1i];
% tspan=[0:50];
% [t,x]=ode45(@stilldiffeq1,tspan,xinitial)
% %%
% data=[t x]
% D=x(:,1);
% W=x(:,2);
% x1=x(:,3);
% x2=1-x1;
% 
% % Normalized
% nD=D/max(D);
% nW=W/max(W);
% nx1=x1/max(x1);
% nx2=x2/max(x2);
% 
% figure(4)
% clf
% plot(t,nD,t,nW)
% hold on
% plot(t,nx1,t,nx2)

