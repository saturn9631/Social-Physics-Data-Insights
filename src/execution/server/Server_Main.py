import pandas as pd
import numpy as np
import scipy as sc
import sympy as smp
import networkx as nx
import torch

def main ():
    pass

class PDR_Server:
    def __init__ (self, database):
        #Fill in logic to find data for the fields
        self.dataBase = database #Use dependency injection to allow the database to change, maybe wrap the database in a class that abstracts away the access syntax.
        #self.data = pd.DataFrame({})
        pass
    def update (self):
        pass
    def __del__(self):
        pass

if __name__ == "__main__":
    main()
