function dx = stilldiffeq2(t,x)


x1=x(3);
y1=vlewaterethanol2(x1);

dx=zeros(2,1);

dx(1)=1; % dD, Constant flowrate out of still
dx(2)=-dx(1); % dW, All of distillate comes from Wash
dx(3)=dx(2)*(y1-x1)/x(2);


end

