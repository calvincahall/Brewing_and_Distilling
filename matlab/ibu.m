function output = ibu(hops)
% Function calculates approx IBUs in beer based on alpha acid and boil
% time.
alpha=hops(:,1);
boiltime=hops(:,2);
ounces=hops(:,3);

if length(ounces)~=length(boiltime)
    error('Ounces must equal Boiltime')
elseif length(boiltime)~=length(alpha)
    error('Boiltime must equal alpha')
elseif length(alpha)~=length(ounces)
    error('alpha must equal ounces')
end

% Ounces x Alpha Acid x Percentage Utilization(boil time) divided by 7.25
% Determine utilization % by boil time. 
for index=1:length(boiltime)
    if boiltime(index)>60
        ut(index)=31; % In percentage. 
    elseif boiltime(index)<=60 & boiltime(index)>50;
        ut(index)=30;
    elseif boiltime(index)<=50 & boiltime(index)>45;
        ut(index)=28.1;
    elseif boiltime(index)<=45 & boiltime(index)>40;
        ut(index)=26.9;
    elseif boiltime(index)<=40 & boiltime(index)>35;
        ut(index)=22.8;
    elseif boiltime(index)<=35 & boiltime(index)>30;
        ut(index)=18.8;
    elseif boiltime(index)<=30 & boiltime(index)>25;
        ut(index)=15.3;
    elseif boiltime(index)<=25 & boiltime(index)>20;
        ut(index)=12.1;
    elseif boiltime(index)<=20 & boiltime(index)>15;
        ut(index)=10.1;
    elseif boiltime(index)<=15 & boiltime(index)>10;
        ut(index)=8;
    elseif boiltime(index)<=10 & boiltime(index)>5;
        ut(index)=6;
    elseif boiltime(index)<=5 & boiltime(index)>=0;
        ut(index)=5;
    end
end

ibuarray=(ounces.*alpha.*ut')/7.25;
output=sum(ibuarray);

end