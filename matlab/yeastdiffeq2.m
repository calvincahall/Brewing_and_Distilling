function dy = yeastdiffeq2(t,y)

global ks ks1 mux mup kp kp1 rsx rsp R tr ea1 ea2 a1 a2 ...
    dhr1 vol ta massw cpwater h sa mwetoh

dy=zeros(5,1);

mux=a1*exp(-ea1/(R*(y(4)+273)))-a2*exp(-ea2/(R*(y(4)+273)));

dy(1)=mux*y(1)*(y(3)/(ks+y(3)))*exp(-kp*y(2)); % Yeast biomass
dy(2)=mup*y(1)*(y(3)/(ks1+y(3)))*exp(-kp1*y(2)); % Ethanol 
dy(3)=-(1/rsx)*dy(1)-(1/rsp)*dy(2);              % Sugars
dy(4)=(-dhr1*dy(2)*vol)/(mwetoh*massw*cpwater)...
    -(h*sa*(y(4)-ta))/(massw*cpwater); % Temperature for natural convection 

end