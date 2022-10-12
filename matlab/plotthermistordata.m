
clear
load thermistordata.mat

%%
% Raw Data
tempc=table2array(thermistordata(:,1));
tempf=table2array(thermistordata(:,2));
rtr=table2array(thermistordata(:,4));
perc=table2array(thermistordata(:,5));
res=table2array(thermistordata(:,6));

% Get equation relating temperature and resistance
[fit1, gof1]=fit(res,tempc,'power2'); % resistance to temperature
[fit2, gof2]=fit(tempc,res,'exp2'); % temperature to resistance

%%
% Plot temperature and resistance
figure(1)
clf
plot(fit1,res,tempc)
ylabel('Temp (?C)')
xlabel('Resistance (Ohm)')
% 
% plot(fit2, tempc, res)
% xlabel('Temp (?C)')
% ylabel('Resistance (Ohm)')

%% Simple Voltage Splitter

% Resistance at desired temp bounds
lowt=3; 
hight=23;
lowtres=fit2(lowt);
hightres=fit2(hight);
% midtempres=fit2((lowt+hight)/2);
midtempres = 19700;
midres = midtempres
midres=(lowtres+hightres)/2;

% Voltage splitter equation
r1=fliplr([hightres:lowtres]); % (ohms) resistance dynamic range
r2=midres; % (ohms) constant resistor value
v1=5;

v2=v1*(r2./(r1+r2)); % Voltage at splitter

figure(2)
clf
plot(r1,v2)
ylabel('Voltage (V)')
xlabel('Resistance (Ohm)')

% map the bit values to voltage readings
bittov=5/1024;
lowtbit=round(v2(1)/bittov);
hightbit=round(v2(end)/bittov);
bitdif=hightbit-lowtbit;
tresolution=(hight-lowt)/bitdif % temp change per bit

%% Look at Wheatstone bridge
vs = 5; % V
% Resistance at desired temp bounds
lowt=65; 
hight=95;
lowtres=fit2(lowt);
hightres=fit2(hight);
midtres=(lowtres+hightres)/2;

% Resistance values in bridge.
R2 = fliplr([round(hightres):round(lowtres)]);
% R2 = [0:5e4];
R1 = midtres;
R3 = R1;
R4 = 100;

vg = vs*((R2./(R1+R2)) - (R4/(R3+R4)));
voltc = vs*(R2./(R1+R2));
voltd = vs*(R4/(R3+R4));
volts = voltc - voltd;

figure(3)
clf
plot(R2,vg)
hold on
plot(R2,voltc)
xlabel('Resistance')
ylabel('Voltage')
legend('Vg','Vc')
title('Individual Voltage')

% map the bit values to voltage readings
bittov=5/1024;
lowtbit=round(vg(1)/bittov);
hightbit=round(vg(end)/bittov);
bitdif=abs(hightbit-lowtbit);
tresolution=(hight-lowt)/bitdif % temp change per bit

%% Running Arduino

if exist('s')==1;
    fclose(s); % Close port
    delete(s); % Delete port
    instrreset;
end
port='/dev/cu.usbserial-A700HIH5'
s=serial(port);

fopen(s)
% pause(10)
% tic
y = 1;

vbits = fscanf(s);
vbits = fscanf(s,'%f');
volt=vbits*bittov;
resist=r2*(5-volt)/volt;
temp=fit1(resist);

iter=1;

figure(3)
clf
h = animatedline(iter,temp);

while iter <= 1000
    vbits = fscanf(s,'%f');
    volt=vbits*bittov;
    resist=r2*(5-volt)/volt;
    temp=fit1(resist);
    data(iter,:)=[iter temp];
    addpoints(h,iter,temp);
    drawnow
    iter=iter+1;
end

fclose(s);
intrreset;
