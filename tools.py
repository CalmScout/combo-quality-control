"""
Auxiliary functions for the project.
"""
import numpy as np
import pandas as pd


def csv2ndarray(fname, nan=0.0):
    df = pd.read_csv(fname)
    values = df.values
    values = np.nan_to_num(values, nan=nan)
    return values

def get_label(fname):
    return fname.name.split('.')[0].split('_')[-1]