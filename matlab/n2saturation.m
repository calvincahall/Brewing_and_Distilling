%% Gas Diffusion into liquid
% One dimensional diffusion of gas through liquid
% Finite difference and euler's method

%% Assumptions
% Contant temperature, constant pressure, pure h2o, pure gas, natural
% diffusion.

clear
% Parameters to define the diffusion equation and the range in space and time 
L = 500; % cm
T =1000000; % s
tottime=T*(1/(60*60*24))
khco2=0.034; % mol/(L atm) henry constant for co2
mwco2=44; % g/mol, co2
psipatm=14.6959; % psi per atm.
press=30; % psi
cas=(press*khco2*mwco2)/psipatm %
cao=1.5; % g/l
dab = 0.0016; %  cm^2/s, diffusivity of co2 in water

%  Parameters needed to solve the equation within the explicit method
k = 5000; %  Number of time steps
dt = T/k; % differential time step
n = 50; %  Number of space steps
dx = L/n; % differential space step
b = dab*dt/(dx*dx); %  Stability parameter (b=<1)

%  Initial concentration of in liquid: a source of gas with no sink.
for i = 2:n
        x(i)=(i-1)*dx;
        c(i,1)=cao;
end

%  Concentration at boundary
for j=1:k
        c(1,j) = cas;
        time(j) = (j-1)*dt;
end
c(:,:)=cao;
c(1,:)=cas;

for j=1:k-1 % Time Loop
    for i=2:n-1; % Space Loop
        c(i,j+1) =b*c(i+1,j)+(1-2*b)*c(i,j)+b*c(i-1,j);
    end
    c(n,j+1)=c(n-1,j+1);
end

% Graphical representation of the temperature at different selected times
figure(1)
plot(x,c(:,50),'-',x,c(:,end/2),'-',x,c(:,end-1),'-')
title('Temperature within the explicit method')
xlabel('X')
ylabel('C')
axis([0 L 0 cas])
legend('Time 50','Time half','Time End')

figure(2)
mesh(x,time,c')
title('Temperature within the explicit method')
xlabel('X')
ylabel('Time')
zlabel('Concentration')