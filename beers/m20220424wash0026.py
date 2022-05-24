'''
Type: Wash, Whiskey 
Name: Wash0026
Brewed: April 24, 2022
Yeast: Redstar spirit yeast

'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./wash_saps.json')

def m20220424wash0026(wash='',save_wash=False, overwrite=False):
    '''
    Returns wash object with all attributes of brew day, fermentation, etc.
    '''

    # ================= INPUTS =============================
    id = "Wash0026"
    yeast = 'Redstar Spirit Yeast'
    wash = bu(saps,id)
    final_vol = mu.gal2l(14)
    og = 1.070
    fg = 1.022
    og_temp = mu.c2f(40)
    fg_temp = mu.c2f(20)
    notes = {''}

    # ======== MASH ========================================
    mash_in_temp_c = 70.5
    ambient_temp = 15
    grain_water_ratio = 3.5 # kg/l
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')


    # Grain Bill kgs
    # # 1
    # grain_bill_dict = {
    #         'flaked_corn':      mu.lb2kg(7),
    #         'pale_malt':        mu.lb2kg(8),
    #         'rye_malt':         mu.lb2kg(2),
    #         'white_wheat_malt': mu.lb2kg(3)
    # }
    # # 2
    # grain_bill_dict = {
    #         'flaked_corn':      mu.lb2kg(2),
    #         'pale_malt':        mu.lb2kg(8),
    #         'rye_malt':         mu.lb2kg(2),
    #         'white_wheat_malt': mu.lb2kg(3)
    # }
    # TOTAL
    grain_bill_dict = {
            'flaked_corn':      mu.lb2kg(15),
            'pale_malt':        mu.lb2kg(16),
            'rye_malt':         mu.lb2kg(4),
            'white_wheat_malt': mu.lb2kg(6)
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
    wash.set_efficeincy(efficeincy)
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

# Run function
wash_file = './washes_pickle.pickle'
wash = m20220424wash0026(wash_file, save_wash=True, overwrite=False)

