'''
Type: Chocolate Milk Porter
Name: Chocolate Portering Unit (CPU)
Brewed: 20200202
Yeast: WLP001 California Ale Yeast
Secondary: 20200210
Kegged: 20200225
Kicked:
'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def b20200202milk_porter(beer_file='',save_beer=False, overwrite=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = 65
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Chocolate Portering Unit (CPU)"
    classification = "Ale"
    beer_type = "Porter"
    yeast = 'WLP001 California Ale Yeast'
    beer = bu(saps, name)
    final_vol = mu.gal2l(6.2)
    og = 1.077
    fg = 1.026
    og_temp = 70
    fg_temp = 60

    # hops = [Alpha, Boil, Ounces]
    additions = 1
    hops = np.array((additions,3))
    willamette = np.array([3.8,60,0.65])
    hop_types = ['willamette']
    hops = willamette
    hops = hops.reshape((additions,3))

    # Grain Bill kgs
    grain_bill_dict = {'pale_malt': mu.lb2kg(2),
                    'pale_chocolate_malt': mu.lb2kg(1),
                    'black_malt': mu.lb2kg(3/16),
                    'chocolate_wheat_malt': mu.lb2kg(0.25),
                    'two_row_malt': mu.lb2kg(10),
                    'flaked_oats': mu.lb2kg(0.5)}

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
beer = b20200202milk_porter(beer_file, save_beer=True, overwrite=True)
# print('stop')
