% Analytical solution to keg carbonation

% syms 
% % ca = @(j,x,t) ((4*c0)/pi)...
% %     * sum (  (1/(2*j+1))*sin((2*j+1)*pi*(x/l))...
% %     * exp(-((((2j+1)^2)*(pi^2))/(l^2))*dab))
% 
% dab = 0.00016; %  cm^2/s, diffusivity of co2 in water
% l = 10; % cm
% T =20; % s
% cao=1.5; % g/l
% tottime=T*(1/(60*60*24)); % days
% 
% syms j x t;
% 
% ca = @(x,t) ((4*cao)/pi)...
%     * symsum((1/(2*j+1))*sin((2*j+1)*pi*(x/l))...
%     * exp(-((((2j+1)^2)*(pi^2))/(l^2))*dab*t),j,0,10);
% 
% % ca1 = @(x,t) symsum((1/(2*j+1))*sin((2*j+1)*pi*(x/l))...
% %     * exp(-((((2j+1)^2)*(pi^2))/(l^2))*dab*t),j,0,10);
% 
% for i=1:l
%     for j=1:T
%         cvals(i,j)=ca(i,j);
%     end
% end
% 
% cvals=real(double(cvals))
% 
% figure(1)
% clf
% surf(cvals)

%%
clear
dab = 0.00016; %  cm^2/s, diffusivity of co2 in water
cao=1.5; % g/l
l=5; % cm
x=1; % cm
t=10; % s
syms t j;

ca2 = @(t) ((4*cao)/pi)...
    * symsum((1/(2*j+1))*sin((2*j+1)*pi*(x/l))...
    * exp(-((((2j+1)^2)*(pi^2))/(l^2))*dab*t),j,0,10);

for i=1:100
    ca2vals(i)=ca2(i);
end

ca2vals=real(double(ca2vals))

%%

% figure(1)
% fplot(ca,

