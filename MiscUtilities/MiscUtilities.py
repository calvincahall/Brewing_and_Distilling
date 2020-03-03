'''
Miscellaneous utilities involved in common programs
that are not specific to brewing or distilling.

Author: Calvin Cahall
Created: 20191113
'''

# Import Python Modules
import json
from scipy.io import loadmat
import numpy as np
import pickle
import os
# Import Custom Modules


def read_saps(fname):
    
    with open(fname) as read_file:
        saps = json.load(read_file)
    return saps

def molefraction2abv(x_ethanol):
    '''
    Assumes binary solution of ethanol and water. Converts mole 
    fraction ethanol to alcohol by volume.

    Input:
        x_ethanol:      - Mole fraction of ethanol

    Returns:
        abv:            - Alcohol by volume (0 - 1.0)

    '''
    # Output
    abv = 0

    # Constants
    eth_den=0.7893       # g/ml, density of ethanol
    water_den=0.9982     # g/ml, density of water
    eth_mw=46.07         # g/mol, MW ethnol
    water_mw=18.01       # g/mol, MW water

    # 1 Liter Basis
    x1 = x_ethanol 
    x2 = 1-x1       # Water
    mole = 1        # 1 mole basis

    mass_eth = x1 * eth_mw          # g, mass of ethanol in mole basis.
    mass_water = x2 * water_mw      # g, mass water in mole basis.
    vol_eth = mass_eth/eth_den      # ml, volume of pure ethanol
    vol_water = mass_water/water_den   # ml, volume of pure water
    v0l_tot1 = vol_eth + vol_water    # ml, total volume of solution
    abv1 = vol_eth / (vol_eth+vol_water) # alcohol fraction by volume.

    ## Partial molar volumes (ml/mol)
    # Molar volume ethanol
    mve = lambda x: 23.967 * x**3 - 48.407 * x**2 + 32.816 * x + 50.414
    # Molar volume water
    mvw = lambda x: -2.1713 * x**2 - 1.8511 * x + 18.138

    mv_eth = mve(x1)
    mv_water = mvw(x2)
    vtot2 = x1*mv_eth + x2*mv_water
    abv2= (x1*mv_eth) / vtot2

    abv=abv2

    return abv

def abv2molefraction(abv):
    '''
    Assumes binary solution of ethanol and water. Returns the mole
    faction of ethanol given the abv. ROUGH estimate.
    Input:
        abv         - Alcohol by volume
    Result:
        fraction    - Mole fraction ethanol
    '''
    # Output
    fraction = 0

    # Constants
    eth_den=0.7893       # g/ml, density of ethanol
    water_den=0.9982     # g/ml, density of water
    eth_mw=46.07         # g/mol, MW ethnol
    water_mw=18.01       # g/mol, MW water
    basis = 1            # L, solution

    mass_eth = (abv * basis) / eth_den
    mass_w = ((1-abv) * basis) / water_den
    fraction = mass_eth / (mass_eth + mass_w)
    
    return fraction

def kg2lb(kgs):
    '''
    Converts given kilograms to pounds.
    '''
    # lbs per kg
    unit_conversion = 2.20462
    lbs = kgs * unit_conversion
    return lbs

def lb2kg(lbs):
    '''
    Converts given pounds to kilograms.
    '''
    # kgs per lbs
    unit_conversion = 1 / 2.20462
    kgs = lbs * unit_conversion
    return kgs

def gal2l(gal):
    '''
    Converts gallons to liters.
    '''
    # liters per gallon
    unit_conversion = 3.78541
    liters = gal * unit_conversion
    return liters

def l2gal(liters):
    '''
    Converts liters to gallons.
    '''
    # gallon per liters
    unit_conversion = 1 / 3.78541
    gallons = liters * unit_conversion
    return gallons

def c2f(celcius):
    '''
    Converts Celcius to Fahrenheit.
    '''
    f = 32 + (9/5) * celcius
    return f

def f2c(fahrenheit):
    '''
    Converts fahrenheit to celcius.
    '''
    c = (fahrenheit-32) * (5/9)
    return c

def ppg_to_pkl_json(saps):
    '''
    Converts PPG to points per kg per liter using a json file
    of ppg.
    '''

    pkl = []
    max_ppg = read_saps(saps['GRAIN_PPG'])
    max_pkl = read_saps(saps['GRAIN_PKL'])
    dict_keys = max_pkl.keys()
    n_grains = len(max_ppg)

    for grain in max_ppg:
                pkl = round(kg2lb(max_ppg[grain]))
                pkl = round(gal2l(pkl),4)
                max_pkl.update({grain: pkl})

    with open(saps['GRAIN_PKL'], 'w') as f:
        json.dump(max_pkl,f,indent=4,sort_keys=True)

def distillate_abv(x_ethanol, stages, plot_stages=False, saps=None):
    '''
    Estimates the file proof of the distillate when given initial
    alchol fraction and estimated number of stages. Ideal system using
    ideal opporating line as default.

    Input: 
        x_ethanol:      - Mole fraction ethanol
        stages:         - Estimated or known number of stages
        reflux_ratio:   - Ratio of liquid recycled back in over distillate taken.

    Return:
        distillate:     - Mole fraction ethanol in distillate
    '''
    # Imported VLE data for Water/ethanol
    if not saps:
        saps = read_saps('./brew_saps.json')

    vle_data = loadmat(saps["ETHANOL_VLE_DATA"])
    vle = vle_data.get('vleimport')
    temp = vle[:,0]         # Temp celcius
    x2 = vle[:,1]           # Liquid water fraction
    y2 = vle[:,2]           # Vapor water fraction
    x1 = 1 - x2             # Liquid ethanol fraction
    y1 = 1 - y2             # Vapor ethanol fraction

    # Place holders for graphs.
    end = 1
    step = 0.01
    x_holder = np.array([(ii * step) for ii in range(int(end/step))])
    y_yholder = x_holder

    # Fit data to polynomial
    poly_degree = 8
    pvals = np.polyfit(x1, y1, poly_degree)
    vle_fun = lambda x: (pvals[8] * x**8 + pvals[7] * x**7 + pvals[6] * x**6 +
                        pvals[5] * x**5 + pvals[4] * x**4 + pvals[3] * x**3 +
                        pvals[2] * x**2 + pvals[1] * x**1 + pvals[0])
    
    # vle_fun2 = lambda x: (pvals[0] * x**8 + pvals[1] * x**7 + pvals[2] * x**6 +
    #                     pvals[3] * x**5 + pvals[4] * x**4 + pvals[5] * x**3 +
    #                     pvals[6] * x**2 + pvals[7] * x**1 + pvals[8])
    
    # Operating line
    # lod = reflux_ratio              # (Liquid recycled) / (distillate taken)
    # lov = lod / (1 + lod)           # liquid fraction over vapor fraction
    ol = lambda x: x     
    hl = lambda x: 0

    liquid = x_ethanol
    vapor_store = []
    liquid_store = []
    for ii in range(stages):
        vapor = np.polyval(pvals,liquid)
        vapor_store.append(vapor)
        liquid = vapor
        liquid_store.append(liquid)

    #=============FIX PLOTS
    # if plot_stages:
    #     for ii in range(len(liquid_list)):
    #         plt.plot()
    #=======================================

    return liquid

def pickle_save(var_list,path_name):
    '''
    Pickle saves variables to list.
    INPUT:
        var_list        - list of variables to save
        path_name       - path and file name
    '''
    # path_name += '.pickle'
    with open(path_name,'wb') as f:
        pickle.dump(var_list,f)
    return

def pickle_load(path_name):
    '''
    Returns the variables saved in pickle file.
    INPUT:
        path_name        - name of pickle file
    RETURN:
        var_list        - variable list saved in pickle file
    '''
    var_list = []
    with open(path_name,'rb') as f:
        var_list = pickle.load(f)

    return var_list

def save_beer_to_archive(path_name, new_beer, overwrite=False):
    '''
    Loads pickle file containing beer list, appends new beer
    to list, saves beer list to pickle file to contain all beers.
    INPUT:
        path_name:          -path to variable list
        new_beer:           -BrewUtilities object of new beer.
    RETURN:
        nothing.
    '''
    
    if os.path.exists(path_name):
        beer_list = pickle_load(path_name)
    else:
        beer_list = []

    # Check for existance of beer
    names = []
    for beer in beer_list:
        name = beer.get_name()
        names.append(name)

    new_name = new_beer.get_name()
    if new_name in names:
        if overwrite:
            element = np.where(np.array(names)==new_name)[0]
            beer_list[element[0]] = new_beer
            print(new_name + ' was overwritten.')
            # Find element number and replace
        else:
            print(new_name + ' already exists and overwrite is set to False.')
        
    else:
        print(new_name + ' was written as new beer to archive.')
        beer_list.append(new_beer)

    
    pickle_save(beer_list,path_name)

    return

def delete_beer_from_archive(path_name, old_name):
    '''
    Loads pickle file containing beer list, appends new beer
    to list, saves beer list to pickle file to contain all beers.
    INPUT:
        path_name:          -path to variable list
        old_beer:           -BrewUtilities object of old beer to delete.
    RETURN:
        nothing.
    '''
    
    if os.path.exists(path_name):
        beer_list = pickle_load(path_name)
    else:
        print('No beer archive file exists under that name.')
        return

    # Check for existance of beer
    names = []
    for beer in beer_list:
        name = beer.get_name()
        names.append(name)

    if old_name in names:

        ndx = names.index(old_name)
        del beer_list[ndx]
        print(old_name + ' was deleted from archive.')
        
    else:
        print(old_name + ' does not exist in archive.')

    pickle_save(beer_list,path_name)

    return

        


