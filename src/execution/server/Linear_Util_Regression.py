import typing
import pandas as pd
import numpy as np
import sympy as smp
import networkx as nx
import torch as tc
from torch import nn
from torch.utils.data import DataLoader

import sys
sys.path.append("../../lib/")
sys.path.append("../../test/")

import Actor_Tensor

#Continuation Note: Create a loss function that is the sum of the data loss and the loss determined by how much the output deviates from taylor series. The outputs of the neural net should be the coefficients of the taylor polynomial.
class Taylor_Model(nn.Module):
    """Encapsulates a best fit model based on Taylor's series."""
    def __init__(self, terms, center, data_points_window = 20):
        """Parameters: 
        terms (int): How many terms does the Taylor polynomial have.
        center (float): The value of the center of approximation."
        data_points_window (int): The amount of points the neural network takes a a time.
        """
        self.coefficients = np.zeros(terms)
        self.center = center
        hidden_layer_width = terms * 2
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(data_points_window, hidden_layer_width),
            nn.ReLu(),
            nn.Linear(hidden_layer_width,  hidden_layer_width),
            nn.ReLu(),
            nn.Linear(hidden_layer_width,  hidden_layer_width),
            nn.ReLu(),
            nn.Linear(hidden_layer_width,  hidden_layer_width),
            nn.ReLu(),
            nn.Linear(hidden_layer_width, terms)
        )
    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

    def loss (self):
        pass

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

        #Forward is supposed to evaluate across an array and use cuda
    def getTaylorPolynomial (self, variable = smp.symbols("x")):
        """Returns the Taylor polynomial as a sympy object. E.g.: getTaylorPolynomial (sympy.symbols("s")) -> a + b(s-q) + c(s-q)**2 + ..., where a, b, c, ... are the Taylor coefficients, and q is the center.
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
