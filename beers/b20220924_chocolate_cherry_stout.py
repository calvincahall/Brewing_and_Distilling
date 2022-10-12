

# Import Python Modules
import numpy as np
import sys


# Import Custom Modules
from BrewUtilities import BrewUtilities as bu
import MiscUtilities as mu

# SAPS
saps = mu.read_saps('./brew_saps.json')

def b20220924_chocolate_cherry_stout(beer_file='',save_beer=False, overwrite=False):
    '''
    Returns beer object with all attributes of brew day, fermentation, etc.
    '''

    # ================= INPUTS =============================
    id = 'b0007'
    name = "Madam Curie's Cherry Pie"
    classification = "Ale"
    beer_type = "Stout"
    yeast = "WLP001 and SafeAle US-05"

    ambient_temp = mu.f2c(65) # C
    final_vol = mu.gal2l(5.4)
    og = 1.076
    fg = 1.016
    og_temp = mu.c2f(26.4) # F
    fg_temp = mu.c2f(19.4) # F

    # ======== HOPS ========================================
    # hops = [Alpha, Boil, Ounces]
    hop1= np.array([4.6,60,0.5])
    hop2= np.array([4.6,30,0.5])
    hops = np.array([hop1, hop2])
    hop_types = ['Fuggle', 'Fuggle']

    # ======= GRAIN ========================================
    grain_bill_dict = {
        'two_row_malt':         mu.lb2kg(14),
        'caramel_malt_120l':    mu.lb2kg(2),
        'black_malt':           mu.lb2kg(0.25),
        'roasted_barley_malt':  mu.lb2kg(0.25),
        'carafa_iii_malt':      mu.lb2kg(0.25),
        'pale_chocolate_malt':  mu.lb2kg(1)
    }

    #====================================================================
    # --------- Mash and water calculations
    #====================================================================
    beer = bu(saps, id)
    # ========= MASH =======================================
    mash_in_temp_c = 70.5 # F 
    grain_water_ratio = 3.5 # kg/l
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
    og_points = (og-1) * 1000
    efficeincy = beer.efficiency(og_points, og_temp, theo_points)
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
    beer = b20220924_chocolate_cherry_stout(beer_file, save_beer=False, overwrite=False)
    # print('stop')
