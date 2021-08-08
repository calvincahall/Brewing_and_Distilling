'''
Type: Amber
Name: Queen Beer
Brewed: 20201128
Yeast: WLP883 Zurich Lager Yeast
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

def b20201128red_wheat_amber(beer_file='',save_beer=False, overwrite=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = saps["MASH_IN_TEMP"]
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Queen Beer"
    classification = "Lager"
    beer_type = "Red Wheat"
    yeast = 'WLP883 Zurich Lager'
    beer = bu(saps, name)
    final_vol = mu.gal2l(5.5)
    og = 1.051
    fg = 1.015
    og_temp = 61.5
    fg_temp = 63

    # hops = [Alpha, Boil, Ounces]
    additions = 2
    hops = np.array((additions,3))
    horizon_1 = np.array([10.4,60,0.33])
    horizon_2 = np.array([10.4,0,0.66])
    hops = np.array([horizon_1, horizon_2])
    hops = hops.reshape((additions,3))
    hop_types = ['Horizon']

    # Grain Bill kgs
    grain_bill_dict = {
        'six_row_malt':     mu.lb2kg(6),
        'red_wheat_malt':   mu.lb2kg(2),
        'cara_ruby_malt':   mu.lb2kg(1),
        'flaked_oats':      mu.lb2kg(0.5)
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
beer = b20201128red_wheat_amber(beer_file, save_beer=True, overwrite=True)
# print('stop')
