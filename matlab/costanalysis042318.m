% Brewery

% Time brewing
brewtime=6; % hours

% Salary
employees=3;
yearly=5e4;
monthly=yearly/12
hourly=yearly/(48*5*8);

% Rent
rentunit=1400; % $/month
renthourly=rentunit/(30*24);

% Energy
electricunit=150; % $/month
electrichourly=electricunit/(30*24);
propaneunit=18; % $/tank

% Water
waterunit=0.01; % $/gal

% Grain
grainunit=2.5; % $/lb

% Hops
hopunit=2.5; % $/oz

% Yeast
yeastunit=5; % $/pack

% Cleaning material

% General Beer
grain=12;
hops=2;
yeast=1;
water=100;
propane=0.2;
beers=(5.5*128)/12;

materials=(grainunit*grain)+(hopunit*hops)+(yeastunit*yeast)+...
    (waterunit*water)

energy=(propaneunit*propane)+(electrichourly*brewtime)+(renthourly*brewtime)

building=(renthourly*brewtime)

payroll=(employees*hourly*brewtime)

totalcost=materials+energy+building
beercost=totalcost/beers

beerprice=5; % $/beer
monthlysold=3.3e3
dailysold=monthlysold/30
money=(beerprice-beercost)*monthlysold-(monthly*employees)
