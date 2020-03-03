'''
Type: Oktober Fest
Name: OktoberBreast
Brewed: 20191123
Yeast: WLP036 Dusseldorf Alt Ale
Secondary: 20191215
Kegged: 20191221, #4
Kicked:
'''

# Import Python Modules
import numpy as np

# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def b20191207oktober_fest(beer_file='',save_beer=False, overwrite=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = 62
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Oktoberbreast"
    classification = "Ale"
    beer_type = "Oktoberfest"
    beer = bu(saps, name)
    final_vol = mu.gal2l(5.5)
    og = 1.062
    fg = 1.012
    og_temp = 70
    fg_temp = 70

    # hops = [Alpha, Boil, Ounces]
    additions = 1
    hops = np.array((additions,3))
    huell_melon = np.array([12.8,60,0.25])
    hop_types = ['heull melon']
    hops = huell_melon
    hops = hops.reshape((additions,3))

    # Grain Bill kgs
    grain_bill_dict = {'marris_otter_malt': mu.lb2kg(6),
                    'caramel_malt_20l': mu.lb2kg(1),
                    'caramel_malt_60l': mu.lb2kg(0.25),
                    'barke_munich_malt': mu.lb2kg(5),
                    'flaked_barley': mu.lb2kg(0.5)}

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
    beer.set_yeast('WLP036 Dusseldorf Alt Ale Yeast')
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
beer = b20191207oktober_fest(beer_file, save_beer=True, overwrite=True)

