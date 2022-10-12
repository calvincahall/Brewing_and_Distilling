function dy = yeastdiffeq1(t,y)

global yinitial k1 k2 ks mumax kd kt N

dy=zeros(2,1);

rs=k1*y(2); % Sugar consumption
rg=mumax*y(1)*y(2)/(ks+y(1)); % Yeast growth
rd=(kd+kt*y(3))*y(2); % Yeast death
ret=k2*y(1); % ethanol production

dy(1)=-rs; % Fermentable Sugars
dy(2)=rg-rd; % Yeast
dy(3)=ret;
dy;

end