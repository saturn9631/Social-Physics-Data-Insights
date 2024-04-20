import typing
import pandas as pd
import numpy as np
import sympy as smp
import networkx as nx
import numba as nb
from numba import cuda
import numba
import math

import sys
sys.path.append("lib/")
sys.path.append("test/")

import Actor_Tensor

class Taylor_Model:
    """Encapsulates a best fit model based on Taylor's series."""
    def __init__(self, terms : int, center = 0 : int):
        self.coefficients = np.zeros(accuracy)
        self.center = center

    def forward (self, input):
        result = 0
        index = 0
        for coefficient in self.coefficients:
            result += (coefficient / math.factorial(index)) * (input - center) ** index
            index += 1
        return result
        """Pseudocode: f = taylor polynomial
        return f(input)"""
    
    def backward (data : np.ndarray):
        pass

    def regress(paramaters):
        pass

    def convert_to_diff_eq(order : int) -> smp.Eq:
        pass
        """
        Pseudocode:
        result returned for order=2 should be: smp.Eq(f(x)*self.coefficients[2]*d^2*y/dx^2, g(x)*self.coefficients[1]*dy/dx + h(x)*self.coefficients[0]*y
        order
        """


