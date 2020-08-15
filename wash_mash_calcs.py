'''
Misc calcs for brew day of double wash.

'''

# Import custom modules
from BrewUtilities import *
import MiscUtilities as mu

temp_1 = 48
vol_1 = mu.gal2l(3.5)
vol_2 = mu.gal2l(2)
grain_mass = 0
target_t = 70.5

# temp_1 = mu.f2c(152)
# vol_1 = mu.gal2l(5)
# vol_1 = mu.gal2l(5.5)
# grain_mass = mu.lb2kg(20)
# target_t = mu.f2c(158)

ti = mu.what_water_temp(target_t,vol_2,vol_1,temp_1,grain_mass)
print(ti)
