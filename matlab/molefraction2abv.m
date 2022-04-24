function abv=molefraction2abv(molefraction)
% Converts mole fraction to abv for ethanol/water solution


ethden=0.7893; % g/ml, density of ethanol
waterden=0.9982; % g/ml, density of water
ethmw=46.07; % g/mol, MW ethnol
watermw=18.01; % g/mol, MW water

% 1 Liter Basis
x1=molefraction; % ethanol
x2=1-x1; % Water
mole=1; % 1 mole basis

% % 
masseth=x1*ethmw; % g, mass of ethanol in mole basis.
masswater=x2*watermw; % g, mass water in mole basis.
voleth=(masseth/ethden); % volume of pure ethanol
volwater=(masswater/waterden); % volume of pure water
vtot1=voleth+volwater;
abv1=voleth/(voleth+volwater);

% % Partial molar volumes
mve=@(x) 23.967*x^3 - 48.407*x^2 + 32.816*x + 50.414; % ml/mol
mvw=@(x) -2.1713*x^2 -1.8511*x + 18.138; % ml/mol
mvoleth=mve(x1);
mvolwater=mvw(x2);
vtot2=x1*mvoleth+x2*mvolwater;
abv2=(x1*mvoleth)./vtot2;


abv=abv1;


% figure(1)
% clf
% fplot(mve,[0,1])
% hold on
% fplot(mvw,[0,1])

end
