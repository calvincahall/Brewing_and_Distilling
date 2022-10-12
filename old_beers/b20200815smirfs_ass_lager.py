'''
Type: Lager
Name: Smirfs Ass Lager
Brewed: 20200815
Yeast: WLP883 Zurich Yeast
Secondary:
Kegged:
Kicked:
'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def b20200815smirfs_ass(beer_file='',save_beer=False, overwrite=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = saps["MASH_IN_TEMP"]
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Smirf's Ass Lager"
    classification = "Lager"
    beer_type = "Citrus Lager"
    yeast = 'WLP883 Zurich Lager'
    beer = bu(saps, name)
    final_vol = mu.gal2l(5.8)
    og = 1.056
    fg = 1.012
    og_temp = 87
    fg_temp = 70

    # hops = [Alpha, Boil, Ounces]
    additions = 3
    hops = np.array((additions,3))
    citra = np.array([13.5,60,0.20])
    horizon = np.array([10.4,20,0.20])
    centennial = np.array([6,0,5])
    hops = np.array([citra, horizon, centennial])
    hops = hops.reshape((additions,3))
    hop_types = ['citra','horizon','centennial']

    # Grain Bill kgs
    grain_bill_dict = {
            'two_row_malt': mu.lb2kg(5),
            'white_wheat_malt': mu.lb2kg(4),
            'caramel_malt_10l': mu.lb2kg(2),
            'flaked_wheat': mu.lb2kg(1)
            }

    #====================================================================
    # --------- Mash and water calculations
    #====================================================================
    total_grain = sum(grain_bill_dict.values())
    mash_vol, t_water = beer.mash_in(total_grain,mash_in_temp_c)

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

    return beer

# Run function
beer_file = './beers_pickle.pickle'
beer = b20200815smirfs_ass(beer_file, save_beer=True, overwrite=True)
# print('stop')
