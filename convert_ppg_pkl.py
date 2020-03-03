'''
Quick script for converting PPG json file to PKL.
'''

# Import custom modules
from MiscUtilities import *

saps = read_saps('./brew_saps.json')
ppg_to_pkl_json(saps)
