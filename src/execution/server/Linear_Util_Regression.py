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
    def __init__(self, terms: int):
        self.taylor_coefficients_matrix = np.zeros(accuracy)

    def forward (self, input):
        result = 0
        index = 0
        for coefficient in self.taylor_coefficients_matrix:
            result = (coefficient / math.factorial(index)) * (input) ** index
            index += 1
        return result
        """Pseudocode: f = taylor polynomial
        return f(input)"""
    
    def backward (data : np.ndarray):
        pass

    def regress(paramaters):
        pass

    def convert_to_diff_eq():
        pass
        """
        Algebra: f(x) = f(a) + (f'(a)/1!)(x - a) + (f"(a)/2!)(x - a)^2 + (f"'(a)/3!)(x - a)^3 + (f""(a)/4!)(x - a)^4 + ...
        f(x) =~ f(a) + (f'(a)/1!)(x - a) + (f"(a)/2!)(x - a)^2
        f'(x) =~ f'(a) + f"(a)(x - a)
        f"(x) =~ f"(a)
        f'(x) - f'(a) =~ f"(a)(x - a)
        (f'(x) - f'(a))/f"(a) =~ x - a or (f'(x) - f'(a))/(x - a) =~ f"(a)
        f(x) =~ f(a) + f'(a)((f'(x) - f'(a))/f"(a)) + f"(a)(f'(x) - f'(a))/2f"(a)
        f(x) =~ f(a) + f'(a)((f'(x) - f'(a))/f"(a)) + (f'(x) - f'(a))/2
        f(x) =~ f(a) + f'(a)f'(x)/f"(a) - (f'(a)^2)/f"(a)
        Pseudocode: y(0)"""


