% plotyeastdiffeq1
clc
global yinitial k1 k2 ks mumax kd kt N

mumax=0.1;
kd=0.001;
kt=0.001;
ks=0.01;
k1=1;
k2=1;
N=0.05;

yi1=60; % g/L
yi2=1;  % g/L
yi3=0;

yinitial=[yi1 yi2 yi3];
tspan=1:0.01:15;

[t,y]=ode45(@yeastdiffeq1,tspan,yinitial);

% clear dy
% for i=1:length(t);
%     dy(i,1)=-k1(1)*y(i,2); % sugar
%     dy(i,2)=k2(1)*y(i,2)*(1-(1-y(i,1)/yinitial(1))); % Yeast
% end

figure(2)
clf
% subplot(2,1,1)
plot(t,y(:,1))
hold on
plot(t,y(:,2))
plot(t,y(:,3))
xlabel('time (min)')
ylabel('a.u.')
legend('Sugar','Yeast','EtOH')

% subplot(2,1,2)
% plot(t,dy)
% xlabel('time')
% ylabel('dy/dt')
% legend('dSugar','dYeast')