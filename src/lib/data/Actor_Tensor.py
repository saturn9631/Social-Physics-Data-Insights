import typing
import pandas as pd

class Actor(object):
    def __init__ (self, name : str):
        self.name = name
        self.__opinions = {}

class Actor_Manager(object):
    def __init__(self):
        self.__actors = []

    def make_actors_from_data(self, data : pd.DataFrame):
        """:param data: the data in the format data name, opinion_1, opinion_2, ... opinion_n"""
        for row in data.iloc:
            entity : Actor = Actor(row["name"])
            for entry in data.columns[1:]:
                entity.opinion.update({entry : row[entry]})
            self.__actors.append(entity)
