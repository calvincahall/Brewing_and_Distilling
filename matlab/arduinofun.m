
clear
port1='/dev/cu.usbserial-A700HIH5';
s=serial(port1);
fopen(s)
fread(s)

% fread(s)
fclose(s) 
instrreset

%%
port2='/dev/cu.usbserial-A700HIH5';
s=serial(port2);
fopen(s)
fclose(s)
instrreset

%%
clearvars -except s port

%%
% fopen(s)
% pause(10)
% tic
t = 0;
y = 1;

vbits = fscanf(s);
volt = str2double(vbits);

% clf
% h = animatedline(t,volt(y,1));

iter=0;
while t <= 33000
    iter=iter+1;
vbits = fscanf(s);
volt(y,1)=str2double(vbits)
% addpoints(h,t,volt(y,1))
data(t+1,1)=t;
data(t+1,2)=volt(y);
data(t+1,:);
t = t+1;
y = y+1;
% drawnow
end


%%
fclose(s);
% delete(s);
% clear s;
