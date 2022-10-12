% Programming for book example.

% contants
clear
dab = 0.000016; %  cm^2/s, diffusivity of co2 in water
cao=0; % g/l
cas=2.5; % g/l

l=70; % cm
tfin=10000000; % s
days=tfin*1/(60*60*24)

points=10; % Number of points from zero to lenght and time
stepl=l/points; % step size for length
stept=tfin/points; % step size for time

yo=(cao-cas)/(cao-cas);

syms n z t

y = @(z,t) (4/pi) * sum(subs( (1/n) * sin((n*pi*z)/l) * ...
    exp(-((n*pi*0.5)^2)*((dab*t)/((l)^2))),n,[1:2:99]));
%%
% time zero
zplot(1,1)=double(vpa(y(0,0))); % 
clear i j
for j=2:points+1 % all lengths for
    zin=(j-1)*stepl;
    zplot(1,j)=double(vpa(y(zin,0)));
end

% time >0
clear i j
for i=2:points+1; % time step
    for j=2:points+1; % length step
        zin=(j-1)*stepl;
        tin=(i-1)*stept;
        zplot(i,j)=double(vpa(y(zin,tin)));
    end
end

%%
xplot=[0:stepl:l];
yplot=[0:stept:tfin];

figure(1)
clf
mesh(xplot,yplot,zplot)
xlabel('x Length (cm)')
ylabel('y Time (s)')
zlabel('Relative Concentration')


%% One Dimensional

time1=100000; % s
len1=20; % cm

points1=50;
stime1=time1/points1;
slen1=len1/points1;

tin1=9e5;

lenx(1)=double(vpa(y(0,tin1)));
for i=2:points1+1
    lenin=(i-1)*slen1;
    lenx(i)=double(vpa(y(lenin,tin1)));
end
%%
xhold=[0:slen1:20];
figure(2)
plot(xhold,lenx)
