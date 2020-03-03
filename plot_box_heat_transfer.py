'''
Script for plotting temperature data and calculating
insulation values.

Author: Calvin Cahall
Created: 20200208
'''

# Import Python Modules
import matplotlib.pyplot as plt

# Import Custom Modules
from MiscUtilities import *


temp_data = read_saps('./temp_time_data_box.json')
temp = temp_data["temperature"]
seconds = temp_data["time"]
ambient = temp_data["ambient"]

fig = plt.figure(1)
plt.plot(seconds,temp)

plt.show()

