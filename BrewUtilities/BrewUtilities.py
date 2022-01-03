'''
BrewUtilities:

Beer class for tracking all attributes of a given beer. Beer is object that 
can be used for later.

Author: Calvin Cahall, calvin.cahall10@gmail.com
Created: 20191005
'''

# Import Python Modules
import numpy as np

# Import Custom Modules
import MiscUtilities as mu


class BrewUtilities:

    def __init__(self, saps, name):
        self.saps = saps # System adjustable parameters json file
        self.name = name

# Setters and Getters
    def set_name(self,name):
        self.name = name
        
    def get_name(self):
        return self.name

    def set_yeast(self,yeast):
        self.yeast = yeast
    def get_yeast(self):
        return self.yeast

    def get_ibus(self):
        return self.ibus

    def set_og(self,og):
        self.og = og
    def get_og(self):
        return self.og
    
    def set_fg(self,fg):
        self.fg = fg
    def get_fg(self):
        return self.fg

    def set_final_vol_L(self,vol_l):
        '''Set final volume of beer in fermenter. (Liters)'''
        self.final_vol_L = vol_l
    def get_final_vol_L(self):
        return self.final_vol_L

    def set_mash_temps(self,mash_temps):
        self.mash_temps = mash_temps
    def get_mash_temps(self):
        return self.mash_temps

    def set_mash_in_temp(self,mash_in):
        self.mash_in_temp = mash_in
    def get_mash_in_temp(self):
        return self.mash_in_temp

    def set_grain_bill_dict(self,grain_bill_dict):
        self.grain_bill_dict = grain_bill_dict
    def get_grain_bill_dict(self):
        return self.grain_bill_dict

    def set_hop_types(self,hop_types):
        self.hop_types = hop_types
    def get_hop_types(self):
        return self.hop_types

    def set_hops(self,hops):
        self.hops = hops
    def get_hops(self):
        return self.hops

    def set_classification(self,beer_class):
        '''Lager or Ale.'''
        self.classification = beer_class
        return 
        
    def get_classification(self):
        return self.classification

    def set_beer_type(self,beer_type):
        self.type = beer_type
    def get_beer_type(self):
        return self.beer_type
        
    def set_efficeincy(self,eff):
        self.efficeincy = eff
    def get_efficeincy(self):
        return self.efficeincy
#
    # Properties
    def ibus(self, hops):
        '''
        Estimates IBU values based on boild time, alpha acid content, and mass.
        Input:
            hops: Array of hop additions by time and mass. np.array([alpha(%),time(min),mass(g)])
                        Minimum dimensions of (1,3).
        Return:
            ibus: Scalar of estimate IPUs.
        '''
        ibus = 0        
    
        # Break into data types
        alpha=hops[:,0]
        boil_time=hops[:,1]
        ounces=hops[:,2]

        assert len(alpha)==len(boil_time)==len(ounces), "Dimensions of each piece of data must be equal."

        # Ounces x Alpha Acid x Percentage Utilization(boil time) divided by 7.25
        # Determine utilization percentage by boil time.
        ut = np.zeros(alpha.shape)
        for index in range(len(boil_time)):
            if boil_time[index]>60:
                ut[index]=31 # In percentage. 
            elif boil_time[index]<=60 and boil_time[index]>50:
                ut[index]=30
            elif boil_time[index]<=50 and boil_time[index]>45:
                ut[index]=28.1
            elif boil_time[index]<=45 and boil_time[index]>40:
                ut[index]=26.9
            elif boil_time[index]<=40 and boil_time[index]>35:
                ut[index]=22.8
            elif boil_time[index]<=35 and boil_time[index]>30:
                ut[index]=18.8
            elif boil_time[index]<=30 and boil_time[index]>25:
                ut[index]=15.3
            elif boil_time[index]<=25 and boil_time[index]>20:
                ut[index]=12.1
            elif boil_time[index]<=20 and boil_time[index]>15:
                ut[index]=10.1
            elif boil_time[index]<=15 and boil_time[index]>10:
                ut[index]=8
            elif boil_time[index]<=10 and boil_time[index]>5:
                ut[index]=6
            elif boil_time[index]<=5 and boil_time[index] >=0:
                ut[index]=5
            elif boil_time[index] < 0:
                ut[index]=0

        ibuarray = (ounces * alpha * ut) / 7.25
        self.ibus = sum(ibuarray)

        return self.ibus


    def potential_gravity(self, grain_bill_dict, wort_vol, grain_units=None):
        '''
        Takes in grain bill and wort volume and returns the theoretical gravity
        Input:
            grain_bill_dict: Dictionary object containing grain bill in kg
            wort_vol: Volume of wort in Liters
        Return:
            gravity: Scalar gravity of wort.
        '''
        # Load parameters
        saps = self.saps

        if grain_units == 'ppg':
            max_yeild = mu.read_saps(saps['GRAIN_PPG'])
            final_vol = mu.l2gal(wort_vol)
        else:
            max_yeild = mu.read_saps(saps['GRAIN_PKL'])
        
        # Calculate
        potential_og = 0

        n_grains = len(grain_bill_dict)
        grain_keys = list(grain_bill_dict.keys())
        tot_points = 0

        for ii in range(n_grains):
            points = max_yeild[grain_keys[ii]]
            mass = grain_bill_dict[grain_keys[ii]]
            tot_points += points * mass

        points = tot_points / wort_vol
        self.potential_og = 1 + (points / 1000)

        return self.potential_og


    def abv(self, og=None,tog=60,fg=None,tfg=60):
        '''
        Calculates the estimated alcohol by volume using original and final gravities.
        Inputs:
            tog:        -temperature of original gravity measurement
            og:         -original gravity
            tfg:        -temperature of final gravity measurement
            fg:         -final gravity
        '''
        if not og:
            og = self.og
        if not fg:
            fg = self.fg

        # Reference temperature in 
        tref=60 #F

        # Reference density of water 
        den_water_60 = 1.00130346 - (1.34722124e-4)*tref + (2.04052596e-6)*tref**2 - (2.32820948e-9)*tref**3

        # Temperature corrrection factors
        wtog = 1.00130346 - (1.34722124e-4)*tog + (2.04052596e-6)*(tog**2) - (2.32820948e-9)*(tog**3)
        wtfg = 1.00130346 - (1.34722124e-4)*tfg + (2.04052596e-6)*(tfg**2) - (2.32820948e-9)*(tfg**3)
        cog=og*wtog
        cfg=fg*wtfg

        self.abv = (76.08*(cog-cfg))/(1.775-cog) * (cfg/0.794)
        return self.abv


    def calories(self, og=None, fg=None):
        '''
        Estimates calorie content based on final gravity and 
        alcohol content.
        
        Inputs:
            og:         -original gravity
            fg:         -final gravity

        Return:
            calories:   -estimated calories per 12oz
        '''
        if not og:
            og = self.og
        if not fg:
            fg = self.fg

        # Calories in my burr
        self.calories = 3621*fg*((0.8114*fg+0.1886*og-1)+0.53*((og-fg)/(1.775-og)))

        return self.calories


    def mash_in(self,mass_grain,target_temp,grain_water_ratio=3.5,
                    t_grain=20):
        '''
        Calculates the water volume and temperature needed for the desired
        grain to water ratio and mash-in temp.
        Inputs:
            mass_grain:         -mass of the grain in kg
            grain_units:        -'pkl' is default. 'ppg' may be future option
            grain_water_ratio:  -ratio of grain to water in liters/kg
            t_grain:            -ambient temperature in C.
        Return:
            mash_vol:           -Volume of water (l) needed for grain ratio
            t_water:            -water temperature (C) to pour over grain
        '''

        mash_in_temp = target_temp

        # Heat capacity
        cp_water=4.184      # J/(K g)
        cp_grain=1.5968     # J/(K g)

        # Mass grain
        mass_grain = mass_grain * 1000 # g

        # Mass water in wort
        mash_vol = grain_water_ratio * mass_grain
        mass_water = mash_vol # g

        # Temps
        self.t_water = (cp_grain*mass_grain*(mash_in_temp-t_grain)+cp_water*mass_water*mash_in_temp)/(cp_water*mass_water)
        self.liter_vol = mash_vol / 1000

        return self.liter_vol, self.t_water


    def lactose_addition(self, grain_bill, lactose_percent,
                            batch_vol=mu.gal2l(5), efficiency=0.8):
        '''
        Calculates how much lactose to add for given percentage.
        batch_vol(liters)
        '''
        lactose_percent /= 100
        og_points = (self.potential_gravity(grain_bill,batch_vol) - 1) * efficiency
        lac_og = (og_points * lactose_percent) / (1 - lactose_percent)

        mass_lac = mu.lb2kg(1)
        lac_bill = {
            'lactose': mass_lac
        }
        tol = 0.0001
        done = False
        while not done:
            lac_guess_points = self.potential_gravity(lac_bill,batch_vol) - 1

            if abs(lac_guess_points - lac_og) < tol:
                done = True
            else:
                error = (lac_og - lac_guess_points)/(lac_og + lac_guess_points)
                mass_lac = mass_lac + (mass_lac * error)
                lac_bill['lactose'] = mass_lac
        
        return mass_lac



