'''
Type: Wash
Name: Wash #13
Brewed: 20191231
Yeast: WLP099 Super High Gravity

'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def m20191231wash0013(wash_file='',save_wash=False, overwrite=False):
    '''
    Returns wash object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = 62
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Wash #0013"
    wash = bu(saps,name)
    final_vol = mu.gal2l(5.5)
    og = 1.078
    fg = 1.007
    og_temp = 70
    fg_temp = 88

    # Grain Bill kgs
    grain_bill_dict = {'white_wheat_malt': mu.lb2kg(4),
                    'pilsner_malt': mu.lb2kg(3),
                    'rye_malt': mu.lb2kg(3),
                    'flaked_corn': mu.lb2kg(3),
                    'pot_still_malt': mu.lb2kg(2)}

    #====================================================================
    # --------- Mash and water calculations
    #====================================================================
    total_grain = sum(grain_bill_dict.values())
    mash_vol, t_water = wash.mash_in(total_grain,mash_in_temp_c)

    #====================================================================
    #---------- Calculated values
    #====================================================================
    wash.set_og(og)
    wash.set_fg(fg)
    wash.set_yeast('WLP099 Super High Gravity Yeast')
    wash.set_final_vol_L(final_vol)
    wash.set_grain_bill_dict(grain_bill_dict)
    theoretical = wash.potential_gravity(grain_bill_dict, final_vol, 
                                    grain_units='plk')
    theo_points = (theoretical - 1) * 1000
    og_points = (og - 1) * 1000
    efficeincy = og_points/theo_points * 100
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

    overwrite = True
    if save_wash:
        mu.save_beer_to_archive(wash_file, wash, overwrite=overwrite)

    return wash

# Run function
wash_file = './washes_pickle.pickle'
wash = m20191231wash0013(wash_file, save_wash=True)

