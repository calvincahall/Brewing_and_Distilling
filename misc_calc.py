import numpy as np

a_tot = 9
b_tot = 12
c_tot = 16
d_tot = 3
e_tot = 3

b1 = 12
b2 = 14.5
b3 = 17
grains = np.array([a_tot,b_tot,c_tot,d_tot,e_tot])
tot_grain = grains.sum()
b1_frac = b1 / tot_grain
b2_frac = b2 / tot_grain
b3_frac = b3 / tot_grain

b1_grains = grains * b1_frac
b2_grains = grains * b2_frac
b3_grains = grains * b3_frac

print('stop')