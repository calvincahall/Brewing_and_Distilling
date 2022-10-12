function fgravity = potentialgravity(cvol,fvol,cgravity)
% Determines the potential final gravity if wort boiled down to target
% volume

lpgal=3.78541; % liters per gallon
lpml=10^-3; % liters per mL


masssol=cgravity*cvol*lpgal/lpml; % Mass of total solution
masscw=cvol*lpgal/lpml;
sugar=masssol-masscw;

massfw=fvol*lpgal/lpml;
finalmasssol=sugar+massfw;

fgravity=finalmasssol*lpml/(fvol*lpgal);

end