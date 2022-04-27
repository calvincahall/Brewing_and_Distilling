'''
Type: 
Name:
Brewed:
Yeast:

'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./wash_saps.json')

def mNEW_WASH(wash_file='',save_wash=False, overwrite=False):
    '''
    Returns wash object with all attributes of brew day, fermentation, etc.
    '''

    # ================= INPUTS ============================
    id = "None"
    yeast = 'None'
    wash = bu(saps,id)
    final_vol = mu.gal2l(6.5)
    og = 1.01
    fg = 1.009
    og_temp = 75
    fg_temp = 75
    ambient_temp = 0
    # Grain Bill kgs
    grain_bill_dict = {

    }
    notes = {''}
    # ======== MASH ========================================
    mash_in_temp_c = 70.5
    grain_water_ratio = 3.5 # kg/l

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
    wash.set_notes(notes)
    theoretical = wash.potential_gravity(grain_bill_dict, final_vol, 
                                    grain_units='plk')
    theo_points = (theoretical - 1) * 1000
    og_points = (og - 1) * 1000
    efficeincy = wash.efficiency(og_points, og_temp, theo_points)
    abv = wash.abv(tog=og_temp,tfg=fg_temp)

    print('\n')
    print("Wash: " + id + '\n')
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



if "__main__" == __name__:
    wash_file = './washes_pickle.pickle'
    wash = mNEW_WASH(wash_file, save_wash=False, overwrite=False)

