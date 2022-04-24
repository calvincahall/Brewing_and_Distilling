% Project Euler Problem 31.


% Determine the number of ways that 2£ can be made with any 
% number of coins. Coins: 1p, 2p ,5p, 10p, 20p, 50p, £1, £2.
% 
% Created: 20190324
%   This code does not incorporate the 2£ coin

%%
% Set values of pence, initialize coeffients, set target
eur1=100;
p50=50;
p20=20;
p10=10;
p5=5;
p2=2;
p1=1;
targetval=100;
options=0;
%%

%Determine max value for each in target
eur1max=round(targetval/eur1);
p50max=round(targetval/p50);
p20max=round(targetval/p20);
p10max=round(targetval/p10);
p5max=round(targetval/p5);
p2max=round(targetval/p2);
p1max=round(targetval/p1);
%%
% Loop through possible options.
tic
iter1=0;
iter2=0;
iter3=0;
iter4=0;
iter5=0;
iter6=0;
iter7=0;
clear val allcombos
options = 0;

for a1 = 0:eur1max+1
    iter1 = iter1+1;
    for a2 = 0:p50max+1
        iter2 = iter2+1;
        for a3 = 0:p20max+1
            iter3 = iter3+1;
            for a4 = 0:p10max+1
                iter4 = iter4+1;
                for a5 = 0:p5max+1
                    iter5 = iter5+1;
                    for a6 = 0:p2max+1
                        iter6 = iter6+1;
                        for a7 = 0:p1max+1
                            iter7 = iter7+1;
                            combo = [a1 a2 a3 a4 a5 a6 a7];
                            val = doesit(combo);
                            if val == targetval
                                options = options + 1;
                                allcombos(options,:)=combo;
                            end
                        end
                    end
                end
            end
        end
    end
end

toc
options

uops=unique(allcombos,'rows');
size(unops)
% Function to determine pence value of each combination
function [out] = doesit(a)
eur1=100;
p50=50;
p20=20;
p10=10;
p5=5;
p2=2;
p1=1;
penceval = (a(1)*eur1) + (a(2)*p50) + (a(3)*p20) + (a(4)*p10)...
    + (a(5)*p5) + (a(6)*p2) + (a(7)*p1);
out = penceval;
end
