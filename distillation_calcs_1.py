"""
Script for general plotting and estimations for distillation.


"""


# Import Modules
from tkinter import Y
import numpy as np
import matplotlib.pyplot as mlp

# Import Custom Modules
from DistUtils import *



def plot_vle(x1, y1, show=True):
    '''
    Simple plot of vle data
    '''
    def f(x):
        y=x
        return y

    fig = mlp.plot(x1, y1)
    mlp.plot(x1,f(x1))
    mlp.xlabel("Liquid Mole Fraction")
    mlp.ylabel("Vapor Mole Fraction")
    mlp.show()
    return fig



def distillation_calcs_1():

    fname = './stillvle.mat'
    np_vle = convert_vle_mat_to_np(fname)
    temp = np_vle[:,0]
    x2_vle = np_vle[:,1] # water
    y2_vle = np_vle[:,2] # water vapor
    x1_vle = 1 - x2_vle  # etoh
    y1_vle = 1 - y2_vle  # etoh vapor

    show = True
    fig = plot_vle(x1_vle, y1_vle, show=show)






    # xhold=[0:0.1:1]; % Place holders for graphs.
    # yhold=xhold;

    # [fittemp1,goftemp1]=fit(y1vle,temp,'poly9'); % Fit Temp data to Vapor mole fraction
    # figure(2)
    # clf
    # plot(fittemp1,y1vle,temp)
    # hold on
    # plot(x1vle,temp)
    # title('Ethanol')
    # legend('Fit Dew','Dew Point','Bubble Point')
    # ylabel('Temp ?C')
    # xlabel('Mole Fraction Ethanol')

    # [fit1,gof1]=fit(x1vle,y1vle,'poly9'); % Fit VLE data.
    # figure(3)
    # clf
    # plot(fit1,x1vle,y1vle)
    # hold on
    # plot(xhold,yhold)
    # title('VLE Ethanol')
    # xlabel('Mole Fraction Ethanol')

    # p=coeffvalues(fit1)';
    # vle=@(x) p(1).*x.^9 + p(2).*x.^8 + p(3).*x.^7 + p(4).*x.^6 +...
    # p(5).*x.^5 + p(6).*x.^4 + p(7).*x.^3 + p(8).*x.^2 + p(9).*x + p(10);


    # %% Possible Starting Values
    # abvi=15; % percent alcohol by volume
    # totvoli=5; % Gallons

    # abvi=abvi/100; % fraction alcohol by volume
    # lpgal=3.78541; % liters per gallon
    # totvoli=totvoli*lpgal; % Volume in liters
    # ethvoli=totvoli*abvi; % Liters pure ethanol
    # watervoli=totvoli-ethvoli; % Liters pure waters

    # ethden=0.789; % g/ml, density of ethanol
    # waterden=1.0; % g/ml, density of water
    # ethmw=46.07; % g/mol, MW ethnol
    # watermw=18.01; % g/mol, MW water

    # ethmoli=ethvoli*(ethden*1000)/ethmw; % Initial moles of ethanol present
    # watermoli=watervoli*(waterden*1000)/watermw; % Initial moles of water present
    # totmoli=ethmoli+watermoli; % Total moles in initial wash

    # x1i=ethmoli/(totmoli); % Liquid mole fraction ethanol
    # x2i=watermoli/totmoli; % Liquid mole fraction water
    # y1i=vle(x1i); % Vapor mole fraction ethanol
    # y2i=1-y1i;

    # % Possible Final values, 1 mole basis for ABV.
    # y1f=0.072; % Final vapor fraction ethanol
    # y2f=1-y1f; % Final water fraction
    # ethvolf=y1f*ethmw/(ethden*1000);
    # watervolf=y2f*watermw/(waterden*1000);
    # abvf=ethvolf/(ethvolf+watervolf);

    # %%
    # tic
    # lod=2/3;
    # lov=lod/(1+lod);
    # y1=[0.005:0.001:0.65]';
    # stages=3;

    # load columndata.mat
    # % clear sv sh shy sol1
    # % for k=1:length(y1)
    # %     
    # %     fun1=@(x) x; % Max efficiency operating line.
    # %     ol{k}=@(x) lov*x+(1-lov)*y1(k);  % Operating line for specfied parameters
    # %     sh(k,1)=fun1(y1(k)); % x-point for xd crossing x=y.
    # %     shy{k,1}=@(x) sh(k); % Horizontal line for stage 3
    # % 
    # % for j=1:stages
    # %     syms xvar
    # %     sol1=vpasolve(vle(xvar)==sh(k,j),xvar); % Solve for x1 that crosses horizontal stage line.
    # %     for i=1:length(sol1);
    # %         test(i)=isreal(sol1(i));
    # %     end
    # %     test=find(test); % Eliminate imaginary roots
    # %     sol1=sol1(test);
    # %     sv(k,j)=double(sol1); % Convert to type double.
    # % 
    # %     sh(k,j+1)=ol{k}(sv(k,j)); % Point were stage verticle line hits OL.
    # %     shy{k,j+1}=@(x) sh(k,j+1);
    # % end
    # % 
    # % end
    # % save columndata.mat
    # toc
    # % 
    # %% Operating line graphs
    # % for kgraph=1:length(xd)
    # %     kgraph=500;
    # kgraph=indexx1i+296
    # figure(4)
    # clf
    # fplot(fit1,[0,1])
    # hold all
    # fplot(fun1,[0,1])
    # fplot(ol{kgraph},[0,1])
    # fplot(shy{kgraph,1},[sv(kgraph,1),y1(kgraph)])
    # for q=1:stages-1
    # fplot(shy{kgraph,q+1},[sv(kgraph,q+1) sv(kgraph,q)])
    # end
    # xlabel('x1')
    # ylabel('y1')
    # axis([0 1 0 1])
    # % end

    # %% Graph for integration for ABV
    # x1=flipud(sv(:,end));
    # x2=1-x1;
    # xd=flipud(y1);
    # f=1./(xd-x1);

    # [fit2,gof2]=fit(x1,f,'cubicspline');

    # x1f=0.01;

    # [c indexx1i]=min(abs(x1-x1i)); % Initial pot concentration
    # [c indexx1f]=min(abs(x1-x1f)); % Final pot concentration
    # [c indexy1f]=min(abs(xd-y1f)); % Final vapor concentration

    # % clear c int1
    # figure(5)
    # clf
    # % plot(fit2,x1,f)
    # plot(fit2,x1(indexx1i:indexx1f),f(indexx1i:indexx1f))
    # xlabel('xw')
    # ylabel('1/(xd-xw)')

    # clear int1 wfinal dfinal area xdav
    # for i=1:indexx1f-indexx1i
    # int1(i,1)=integrate(fit2,x1(indexx1i),x1(indexx1i+i));
    # end

    # area=int1;
    # wfinal=totmoli*exp(-area);
    # dfinal=totmoli-wfinal;

    # for i=1:length(wfinal)
    # xdav(i,1)=(totmoli.*x1(indexx1i)-wfinal(i).*x1(indexx1i+i))./dfinal(i);
    # end
    # x1wash=x1(indexx1i:indexx1f-1);
    # xdinst=xd(indexx1i:indexx1f-1);

    # %%

    # wfinalml=(wfinal.*x1(indexx1i:indexx1i+length(wfinal)-1)*ethmw/ethden)+...
    # (wfinal.*x2(indexx1i:indexx1i+length(wfinal)-1)*watermw/waterden); % mL
    # wfinalgal=wfinalml/lpgal/1000;
    # dfinalml=(totvoli-wfinalml/1000)*1000;

    # xdtemp=fittemp1(xdinst);

    # x1abv=(x1wash.*wfinal*ethmw/ethden)./wfinalml;
    # xdavabv=molefraction2abv(xdav);
    # xdinstabv=molefraction2abv(xdinst);

    # data=[x1wash xdinst xdav xdavabv xdinstabv xdtemp wfinalml/1000 dfinalml/1000]
    # data(1,:)
    # subs=2;
    # figure(6)
    # subplot(subs,1,1)
    # plot(dfinalml,xdinstabv)
    # title('ABV at Distillate Volume')
    # ylabel('ABV')
    # xlabel('Volume Distillate (mL)')

    # subplot(subs,1,2)
    # plot(xdtemp,xdinstabv)



    # %% Save 
    # save columndata.mat


if __name__ == '__main__':
    distillation_calcs_1()
