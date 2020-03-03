'''
Script for estimating heat transfer and temperatures for fermentation box.

Author: Calvin Cahall
Email: calvin.cahall10@gmail.com
Created: 20191223
'''

# Import Python Modules
import numpy as np
import math
import matplotlib.pyplot as plt

# Import Custom Modules
import MiscUtilities as mu
import BrewUtilities


# Shared properties
digs = 2 # Rounding digits
t_ambient =         24      # C
t_inside =          12.5    # C
Q_fermentation =    40      # W at peak times.


# =====================================================================
# ============== Calculate energy flux into box =======================
# Assumptions:
#	- Box is well mixed.
#	- Convective heat transfer to inside walls is perfect (zero resistance).
# Equation:
#	q_box = -k(dT/dx)   (W/m2 K)
#	Q_box = q_box * area * T_dif

k_insulation = 1.136          # (W in/m2 K)
box_width = 0.7                 # m
box_height = 0.95                # m
box_length = 0.9                # m
insulation_thickness = 1      # inch
side_1 = box_width * box_height
side_2 = box_height * box_length
side_3 = box_length * box_height
box_area = (side_1 * 2) + (side_2 * 2) + (side_3 * 2) # m2
print('Box surface area: {} m^2'.format(box_area))

Q_box = -(k_insulation / insulation_thickness) * box_area * (t_inside - t_ambient)
print('Rate of energy transport on box: {} W'.format(round(Q_box,digs)))

# ======================================================================
# =========== Heat generation in box ===================================
# Assumptions:
#	- Internal fan is very inefficient
#	- 

fan_volt = 12
fan_amp = 1.8
fan_power = fan_volt * fan_amp
fan_eff = 0.3
Q_fan = (1 - fan_eff) * fan_power   # W


# Bottom of hot side heat sink---------------------
t_sink = 24.4		  # C
sink_area = 36 		  # in2
sink_area *= (0.0254)**2  # m2
convective_coeff = 200	  # (W/m2 K)
Q_sink = sink_area * convective_coeff * (t_sink - t_inside)


Q_gen = Q_fan + Q_sink

# =====================================================================
# ============ Control volume =========================================
# Total energy transfere on control volume
# Assumptions:
#	- Steady state. 0 = Q_box + Q_out + Q_gen

Q_out = -(Q_box + Q_gen)

print('Cooler must operate at {} W to ensure steady state at {} C in  {} C ambient.'.format(
        round(Q_out,digs),t_inside,t_ambient))



# Control volume is fermentor
area_basis = 1
water_per = 0.3
t_amb = mu.f2c(68)     # C
t_water = mu.f2c(50)   # C
t_ferm = mu.f2c(55)
water_coeff = 400    # W/m2 K
air_coeff = 50    # W/m2 K

Q_water = area_basis * water_per * water_coeff * (t_water - t_ferm)
Q_air = area_basis * (1-water_per) * air_coeff * (t_amb - t_ferm)
Q_gen = 40

print('Net tranfer: {}'.format(round(Q_water + Q_air + Q_gen,digs)))

print('stop')

