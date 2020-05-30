'''
Type: Wash
Name: Wash #0019
Brewed: 20200509
Yeast: WLP099 Super High Gravity Yeast

'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def m20200509wash0019(wash_file='',save_wash=False, overwrite=False):
    '''
    Returns wash object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = 70.5
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Wash #0019"
    yeast = 'WLP099 Super High Gravity Yeast'
    wash = bu(saps,name)
    final_vol = mu.gal2l(8)
    og = 1.124
    fg = 1.026
    og_temp = 84
    fg_temp = 70

    # Grain Bill kgs
    grain_bill_dict = {
                        'cracked_corn': 5,
                        'white_wheat_malt': 2,
                        'six_row_malt': 2.5,
                        'sucrose': mu.lb2kg(9),
                        }
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
    wash.set_yeast(yeast)
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


    if save_wash:
        mu.save_beer_to_archive(wash_file, wash, overwrite=overwrite)

    return wash

# Run function
wash_file = './washes_pickle.pickle'
wash = m20200509wash0019(wash_file, save_wash=False, overwrite=False)

