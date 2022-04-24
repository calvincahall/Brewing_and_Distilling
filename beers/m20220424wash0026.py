'''
Type: Wash, Whiskey 
Name: Wash0026
Brewed: April 24, 2022
Yeast:

'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./wash_saps.json')

def m20220424wash0025(wash='',save_wash=False, overwrite=False):
    '''
    Returns wash object with all attributes of brew day, fermentation, etc.
    '''

    # ================= INPUTS =============================
    name = "None"
    yeast = 'None'
    wash = bu(saps,name)
    final_vol = mu.gal2l(9)
    og = 1.075
    fg = 1.015
    og_temp = 70
    fg_temp = 88

    # ======== MASH ========================================
    mash_in_temp_c = 70.5
    ambient_temp = 15
    grain_water_ratio = 3.5 # kg/l
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')


    # Grain Bill kgs
    grain_bill_dict = {
            'flaked_corn':      mu.lb2kg(8),
            'two_row_malt':     mu.lb2kg(8),
            'white_wheat_malt': mu.lb2kg(4)
    }

    #====================================================================
    # --------- Mash and water calculations
    #====================================================================
    total_grain = sum(grain_bill_dict.values())
    mash_vol, t_water = wash.mash_in(total_grain,mash_in_temp_c,
                                grain_water_ratio,
                                t_grain=ambient_temp)

    #====================================================================
    #---------- Calculated values
    #====================================================================
    wash.set_og(og)
    wash.set_fg(fg)
    wash.set_yeast(yeast)
    wash.set_final_vol_L(final_vol)
    wash.set_grain_bill_dict(grain_bill_dict)
    theoretical = wash.potential_gravity(grain_bill_dict, final_vol, 
                                    grain_units='plk')
    theo_points = (theoretical - 1) * 1000
    og_points = (og - 1) * 1000
    efficeincy = wash.efficiency(og_points, og_temp, theo_points)
    abv = wash.abv(tog=og_temp,tfg=fg_temp)

    print('\n')
    print("Wash: " + name + '\n')
    print('MASH:')
    print('     Water vol(l):   {}'.format(round(mash_vol,2)))
    print('     Water vol(gal): {}'.format(round(mu.l2gal(mash_vol),2)))
    print('     Water Temp(C):  {}'.format(round(t_water,2)))
    print('     Water Temp(F):  {}'.format(round(mu.c2f(t_water),2)))
    print('Final:')
    print('     Potential OG:   {}'.format(round(theoretical,3)))
    print('     Actual OG:      {}'.format(og))
    print('     Efficiency:     {}'.format(round(efficeincy,2)))
    print('     ABV:            {}'.format(round(abv,2)))
    print('\n')


    if save_wash:
        mu.save_beer_to_archive(wash_file, wash, overwrite=overwrite)
    else:
        print("File not saved.")

    return wash

# Run function
wash_file = './washes_pickle.pickle'
wash = m20220424wash0025(wash_file, save_wash=False, overwrite=False)

