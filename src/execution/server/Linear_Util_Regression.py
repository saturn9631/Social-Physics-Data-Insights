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
    def __init__(self, terms, center):
        """Parameters: 
        terms (int): How many terms does the Taylor polynomial have.
        center (float): The value of the center of approximation."
        """
        self.coefficients = np.zeros(terms)
        self.center = center

    def evaluate (self, input):
        """Returns the value of the Taylor polynomial at the \"input\" variable.
        Parameters:
        input (float): The value at which the Taylor polynomial is evaluated at.
        Returns: The value of the Taylor polynomial at the input.
        """
        result = 0
        index = 0
        for coefficient in self.coefficients:
            result += (coefficient / smp.factorial(index)) * (input - center) ** index
            index += 1
        return result

    #Cuda tag
    def forward ():
        pass
        #Forward is supposed to evaluate across an array and use cuda

    #Cuda tag
    def backward (self, data : np.ndarray):
        """"""
        pass

    def getTaylorPolynomial (self, variable = smp.symbols("x")):
        """Returns the Taylor polynomial as a sympy object. E.g.: getTaylorPolynomial (sympy.symbols("s")) -> a + b(s-q) + c(s-q) + ..., where a, b, c are the Taylor coefficients, and q is the center.
        Parameters:
        variable (sympy Symbol): the input variable for the Taylor polynomial. 
        Return:
        (sympy Sum): Returns the Taylor polynomial with \"variable\" as the input."""
        for count in range(terms):
            result = (self.coefficients[count] / smp.factorial(count)) * (variable - self.center) ** count
        return (result, variable)

    def convert_to_diff_eq (self):
        """"""
        pass
        """
        Pseudocode:
        result returned for order=2 should be: smp.Eq(f(x)*self.coefficients[2]*d^2*y/dx^2, g(x)*self.coefficients[1]*dy/dx + h(x)*self.coefficients[0]*y
        order
        """


