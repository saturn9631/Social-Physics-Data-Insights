import pandas as pd
import numpy as np
import sympy as smp
import networkx as nx
import torch
import numba as nb
from numba import cuda

import sys
sys.path.append("lib/")
sys.path.append("test/")

import Actor_Tensor

def taylor_series_regression (accuracy):
    taylor_coefficients_matrix = np.zeros(accuracy)

@cuda.jit
def regress():
    pass

def convert_taylor_to_diff_eq():
    pass

#Write code to fit a taylor series to the data and then use that generate a differential equation by eliminating insignificant terms and setting the remaing terms equal to each other.
