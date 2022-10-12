% plotyeastdiffeq1

% "Model based control of a yeast fermentation bioreactor using optimally
%   designed artificial neural networks"
% -Zoltan Kalman Nagy

%%% Lots of information from above papers
%%
clc
global ks ks1 mux mup kp kp1 rsx rsp ...
   R ea1 ea2 tr a1 a2 dhr1 ta sa h cpwater ...
   massw vol mwetoh

% Fermenter dimensions
diam=0.33; % m
height=0.5; % m

% Useful constants
lpgal=3.78541; % liters per gallon
cpwater=4.184; % J/(K g)
lpml=10^-3; % liters per mL
mwetoh=46.06844; % g/mol

vol=5*lpgal; % l
denwater=1.0; % g/ml
points=0.060; % additional gravity in wort
denwort=denwater+points; % g/ml
massw=(vol/lpml)*denwort; % g

R=8.314; % j/(mol K)
dhr1=-74.4e3; % j/mol rxn
sa=pi*diam*height; % m^2
h=2*3600; % j/(h m2 K)
a1=9.5e8;
a2=2.55e33;
% tr=(72-32)*(5/9) % C
ta=ctof(68,1); % C
ea1=55e3; % j/mol
ea2=220e3; % j/mol
ks=1.030; % g/l
ks1=1.680; %g/l
kp=0.139; % g/l
kp1=0.070; % g/l
% mux=1; % 1/h
% mux=a1*exp(-ea1/(R*(tr+273)))...
%     -a2*exp(-ea2/(R*(tr+273)));
mup=1.790; % 1/h
rsx=0.607; % substrate/biomass
rsp=0.435; % substate/product
denetoh=789; % g/l

yi1=1; % yeast g/l
yi2=0; % ethanol g/l
yi3=100; % sugar g/l
yi4=ta; % Ambient temperature K
yi5=0; % no temp difference at t0

yinitial=[yi1 yi2 yi3 yi4 yi5];
tspan=1:1:200;

[t,y]=ode45(@yeastdiffeq2,tspan,yinitial);
tfar=ctof(y(end,4));
abv=100*y(:,2)/denetoh;

figure(2)
clf
% subplot(2,1,1)
plot(t,y(:,1))
hold on
plot(t,y(:,2))
plot(t,y(:,3))
plot(t,y(:,4))
% plot(t,y(:,5))
xlabel('time (hr)')
ylabel('g/l')
legend('Yeast','EtOH','Sugar','Temp C')

% subplot(2,1,2)
% plot(t,abv)
% xlabel('Time')
% ylabel('%ABV')
