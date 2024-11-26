import typing
import pandas as pd

class Actor(object):
    def __init__ (self, name : str):
        self.name = name
        self.__opinions = {}

