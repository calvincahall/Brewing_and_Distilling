% Column Distillation

clear
load stillvle.mat
temp=vleimport(:,1); % Imported VLE data for Water/ethanol
x2=vleimport(:,2);
y2=vleimport(:,3);
x1=1-x2;
y1=1-y2;

xhold=[0:0.1:1]; % Place holders for graphs.
yhold=xhold;

% [fittemp1,goftemp1]=fit(y1,temp,'poly9'); % Fit Temp data to Vapor mole fraction
% figure(2)
% clf
% plot(fittemp1,y1,temp)
% hold on
% plot(x1,temp)
% title('Ethanol')
% legend('Fit Dew','Dew Point','Bubble Point')
% ylabel('Temp ?C')
% xlabel('Mole Fraction Ethanol')

[fit1,gof1]=fit(x1,y1,'poly9'); % Fit VLE data.
% figure(3)
% clf
% plot(fit1,x1,y1)
% hold on
% plot(xhold,yhold)
% title('VLE Ethanol')

p=coeffvalues(fit1)';
vle=@(x) p(1)*x^9 + p(2)*x^8 + p(3)*x^7 + p(4)*x^6 +...
    p(5)*x^5 + p(6)*x^4 + p(7)*x^3 + p(8)*x^2 + p(9)*x + p(10);


% Defined
feed=1000; % kmol/h
zf=0.025; ; % mol fraction in feed
xd=0.5; % specified distillate fraction
xb=0.002; % Specified bottoms fraction

% Fractions to ABV
zfabv=molefraction2abv(zf);
xdabv=molefraction2abv(xd)
xbabv=molefraction2abv(xb);

bottoms=(feed*zf-feed*xd)/(xb-xd);
distillate=feed-bottoms;

q=1.1; % Specified for calculations. Feed is subcooled

% Calculated numbers
% Top Operating line
lod=0.6; % Reflux ratio
lov=lod/(1+lod); % top opperating line slope
tol=@(x) lov*x+(1-lov)*xd;  % Top Operating line for specfied parameters
fun1=@(x) x; % Max efficiency operating line.

% Feed line
feedslope=q/(q-1);
feedline=@(x) feedslope*(x-zf)+zf;

syms xvar
feedtol=solve(feedline(xvar)==tol(xvar),xvar); % Solve for x1 that crosses horizontal stage 3 line.
feedtol=double(feedtol);

% Bottom operating line. Create with interstion of TOL and Feed Line
%   with bottoms mole fraction.
bottomslope=(fun1(xb)-feedline(feedtol))/(xb-feedtol);
bol=@(x) bottomslope*(x-xb)+xb;

stages=25;

sh(1)=fun1(xd); % x-point for crossing TOL
shy{1}=@(x) sh(1);
for i=2:stages+1
    
    syms xvar
    sol1=vpasolve(vle(xvar)==sh(i-1),xvar); % Solve for x1 that crosses horizontal stage line.
    for j=1:length(sol1);
        test(j)=isreal(sol1(j));
    end
    test=find(test); % Eliminate imaginary roots
    sol1=sol1(test); % Isolate real root
    sv(i-1)=double(sol1); % Convert to type double.
    
    if sv(i-1)>feedtol
        sh(i)=tol(sv(i-1)); % Point were verticle line hits TOL
        shy{i}=@(x) sh(i);
    
    elseif sv(i-1)<feedtol && sv(i-1)>xb
        sh(i)=bol(sv(i-1)); % Point were verticle line hits BOL
        shy{i}=@(x) sh(i);
    
    elseif sv(i-1)<xb
        break
    end
    
end

figure(3)
clf
plot(fit1,'b',x1,y1)
hold on
plot(xhold,yhold)

fplot(feedline,[zf feedtol],'k')
fplot(tol,[feedtol xd],'k')
fplot(bol,[xb feedtol],'k')

fplot(shy{1},[sv(1),xd],'r')
for i=2:length(shy)
    fplot(shy{i},[sv(i) sv(i-1)],'r')
end
title('VLE Ethanol')
axis([0 1 0 1])

nstages=length(shy)
