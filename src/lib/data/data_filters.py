import pandas as pd
import numpy as np
import torch

def remove_unknown_people(data):
    filter = data["Name"] != "N/A"
    result = data.loc[filter]
    return result

