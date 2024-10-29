import pandas as pd
import numpy as np
import torch

class Classifier:
    def __init__(self, criteria):
        """param(Criteria): a dataframe that tells the criteria to classify"""
        if type(criteria) == pd.DataFrame:
            self.criteria = criteria
        elif type(criteria) == dict:
            self.criteria = pd.DataFrame(criteria)
        else:
            self.criteria = pd.DataFrame({"N/A": [{"N/A": "N/A"}, {"N/A": "N/A"}]})

    def classify(self, data):
        scores = data.copy()

    def __del__(self):
        pass

def test():
