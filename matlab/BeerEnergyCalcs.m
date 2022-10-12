% Energy and Misc. Calcs

%% Conversions
clear

lpgal=3.78541; % liters per gallon
lpml=10^-3; % liters per mL
kjpj=10^-3; % kj per j
kgpg=10^-3; % kg per g
lbpg=0.0022; % lb per g
btupj=1/1055.06; % btu per j
cpf=5/9; % ?C per ?F
calpj=1/4.184; % g calories per joule

% Heat capacity
cpwater=4.184; % J/(K g)
% cpgrain=0.3822; % btu/(lb F)
cpgrain=1.5968; % J/(K g)

%% Mash water temps

% Mass grain
weightgrain=11; % lbs
massgrain=weightgrain/lbpg; % converted to g.

% Mass water in wort
wortvol=4.16; % volume wort gallon
masswater=(wortvol*lpgal/lpml); % g

% Temps
tfar=158; % Desired temp
tf=(tfar-32)*cpf; % ?C Convert to celcius
tingrain=20; % ?C Temp of grain

tinwater=(cpgrain*massgrain*(tf-tingrain)+cpwater*masswater*tf)/(cpwater*masswater); % Water temp in C
tfarwaterin=tinwater/cpf+32; % Water temp in F
temperature=[tfarwaterin tinwater]

%% Adding more water to increase temp

voladd=2; % Gallons added
massadded=(voladd*lpgal)/lpml;

tfinalf=165; % Desired temp in F
tfinalc=(tfinalf-32)*cpf; % desired temp in C
tmashf=150; % current mash temp in F
tmash=(tmashf-32)*cpf; % Converted to C

tadded=((cpgrain*massgrain+cpwater*masswater)*(tfinalc-tmash))/(massadded*cpwater)
taddedf=(tadded/cpf+32)+tmashf

%% Cooling Calcs
% Assumptions:
    % Water
% ldk

% Wort properties
denwater=1.0; % g/ml
points=0.060; % additional gravity in wort
denwort=denwater+points; % g/ml
brix=(((182.4601 * denwort -775.6821) * denwort +1262.7794) * denwort -669.5622); % Brix from SG

% Temp
tint=373; % K
tfin=298; % K

% Mass water in wort
wortvol=5; % volume wort gallon
masswater=(wortvol*lpgal/lpml)*denwort; % g

% CpWater with Temp
% swater=(1-(0.632-0.001*temp)*(brix/100))/calpj; % J/(K g)

% Energy change from tint to tfin
deltaq=abs(cpwater*masswater*(tfin-tint)); % energy change in joules

% Dry ice needed to cool wort
dhsubco2=571; % j/g
massco2=deltaq/dhsubco2; % j
weightco2=massco2*lbpg;

