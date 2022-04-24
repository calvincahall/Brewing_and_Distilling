"""
Class for performing distillation calculations and plots.
"""

# Import Modules
from numpy import mat
import pandas as pd
from scipy.io import loadmat
import numpy as np

# Import Custom Modules


def convert_vle_mat_to_np(fname):
    '''
    Converts a .mat file to .csv file.
    '''

    data_dict = loadmat(fname)
    data_array = data_dict['vleimport']
    np_vle = np.array(data_array).squeeze()

    return np_vle


