'''
Type: Nut Brown
Name: Lead Ale (Pb)
Brewed: 20191231
Yeast: Safe Ale US-04 Yeast
Secondary: 20190105
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

def b20191231nut_brown(beer_file='',save_beer=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''
    # ---------- Constants -----------------------------
    mash_in_temp_c = 62
    mash_temp_data = False
    if mash_temp_data:
        print('load in data')

    # ================= INPUTS =============================
    name = "Lead Ale (Pb)"
    classification = 'Ale'
    beer_type = 'Brown'
    yeast = 'Safe Ale US-04 Yeast'
    beer = bu(saps, name)
    final_vol = mu.gal2l(5.8)
    og = 1.059
    fg = 1.016
    og_temp = 70
    fg_temp = 70

    # hops = [Alpha, Boil, Ounces]
    additions = 1
    hops = np.array((additions,3))
    east_kent_golding = np.array([4.4,60,1])
    hops = east_kent_golding
    hops = hops.reshape((additions,3))
    hop_types = ['east kent golding']

    # Grain Bill kgs
    pale_malt = mu.lb2kg(6)
    caramel_malt_80l = mu.lb2kg(3)
    chocolate_malt = mu.lb2kg(1)
    honey_malt = mu.lb2kg(1)
    victory_malt = mu.lb2kg(3)

    grain_bill_dict = {'pale_malt': pale_malt,
                    'caramel_malt_80l': caramel_malt_80l,
                    'chocolate_malt': chocolate_malt,
                    'honey_malt': honey_malt,
                    'victory_malt': victory_malt}

    #====================================================================
    # --------- Mash and water calculations
    #====================================================================
    total_grain = sum(grain_bill_dict.values())
    mash_vol, t_water = beer.mash_in(total_grain, mash_in_temp_c)

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

    mu.delete_beer_from_archive(beer_file, "Jiffy's Lube")

    return beer

# Run function
beer_file = './beers_pickle.pickle'
beer = b20191231nut_brown(beer_file, save_beer=True)

