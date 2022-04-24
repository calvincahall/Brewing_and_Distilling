'''
Type:       Lager
Name:       Amber Waves
Brewed:     20220102
Yeast:      Safelager S-23
Secondary:  20220114
Kegged:     20220121
Kicked:     TBD
'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def b20220102red_wheat_lager(beer_file='',save_beer=False, overwrite=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''

    # ================= INPUTS =============================
    name = "Amber Waves"
    classification = "Lager"
    beer_type = "Red Wheat Lager"
    yeast = 'Safelager S-23'

    beer = bu(saps, name)
    final_vol = mu.gal2l(5.8)
    og = 1.054
    fg = 1.015
    og_temp = 75 # F
    fg_temp = mu.c2f(15) # F

    # ========= MASH =======================================
    mash_in_temp_c = 70.2
    ambient_temp = 15
    grain_water_ratio = 3.5 # kg/l
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ======== HOPS ========================================
    # hops = [Alpha, Boil, Ounces]
    horizon = np.array([11.4,60,0.25])
    centennial = np.array([10,0,5])
    hops = np.array([horizon, centennial])
    hop_types = ['Horizon', 'Centennial']

    # ======= GRAIN ========================================
    grain_bill_dict = {
        'red_wheat_malt':   mu.lb2kg(6),
        'two_row_malt':     mu.lb2kg(6),
        'rye_malt':         mu.lb2kg(1),
    }

    #====================================================================
    # --------- Mash and water calculations
    #====================================================================
    total_grain = sum(grain_bill_dict.values())
    mash_vol, t_water = beer.mash_in(total_grain,mash_in_temp_c,
                                    grain_water_ratio,
                                    t_grain=ambient_temp)

    #====================================================================
    #---------- Calculated values
    #====================================================================
    beer.set_classification(classification)
    beer.set_beer_type(beer_type)
    beer.set_og(og) 
    beer.set_fg(fg)
    beer.set_yeast(yeast)
    beer.set_hop_types(hop_types)
    beer.set_final_vol_L(final_vol)
    beer.set_grain_bill_dict(grain_bill_dict)
    beer.set_hop_types(hop_types)
    beer.set_hops(hops)

    theoretical = beer.potential_gravity(grain_bill_dict, final_vol, 
                                        grain_units='plk')
    theo_points = (theoretical - 1) * 1000
    og_points = (og - 1) * 1000
    efficeincy = og_points/theo_points * 100
    beer.set_efficeincy(efficeincy)

    abv = beer.abv(tog=og_temp,tfg=fg_temp)
    ibus = beer.ibus(hops)
    calories = beer.calories(og,fg)


    print('\n')
    print("BEER: " + name + '\n')
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
    print('     IBUs:           {}'.format(round(ibus,2)))
    print('     Calories:       {}'.format(round(calories,2)))
    print('\n')

    if save_beer:
        mu.save_beer_to_archive(beer_file, beer, overwrite=overwrite)
    else:
        print("File not saved.")

    return beer

# Run function
if __name__ == "__main__":
    beer_file = './beers_pickle.pickle'
    beer = b20220102red_wheat_lager(beer_file, save_beer=False, overwrite=False)
    # print('stop')
