function [abv C]= beergravity(og,to,fg,tf)
% og - original gravity
% to - temperature origininal gravity was taken.
% fg - final gravity
% temperature final gravity was taken.

abv(1)=((76.08*(og-fg)/(1.775-og))*(fg/0.794));

tref=60; % ?F
denwater60 = 1.00130346 - (1.34722124e-4)*tref + (2.04052596e-6)*tref^2 - (2.32820948e-9)*tref^3;
wtog = 1.00130346 - (1.34722124e-4)*to + (2.04052596e-6)*to^2 - (2.32820948e-9)*to^3;
wtfg = 1.00130346 - (1.34722124e-4)*tf + (2.04052596e-6)*tf^2 - (2.32820948e-9)*tf^3;
cog=og*wtog;
cfg=fg*wtfg;

abv(2)=((76.08*(cog-cfg)/(1.775-cog))*(cfg/0.794));


% Calories in my burr
C=3621*fg*((0.8114*fg+0.1886*og-1)+0.53*((og-fg)/(1.775-og)));

end