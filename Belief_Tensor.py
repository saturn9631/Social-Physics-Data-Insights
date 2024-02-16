#!shebang

import numpy as np
import scipy as sc
import pandas as pd
import torch as tc

class Belief_Tensor(object):
    pass

class Payoff_Vector(Belief_Tensor):
    def __init__(self, actor):
        self.owner = actor
