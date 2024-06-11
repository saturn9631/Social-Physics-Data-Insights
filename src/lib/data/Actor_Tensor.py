import typing
import pandas as pd

class Actor(object):
    def __init__ (self, name : str):
        self.name = name
        self.__opinions = {}

class Actor_Manager(object):
    def __init__(self):
        self.__actors = []

    def __getitem__(self, index):
        """An override that allows the instance to be indexed like a list by passing the index into the owned list of Actors.
        Parameters: index: any list indexing parameter.Parameters: index: any list indexing parameter.
        Returns:
        Actor: The indexed actor."""
        result = self.__actors[index]
        return result

    def __len__():
        """An override that allows gives the amount of Actors managed by this instance.
        Returns:
        int: The amount of Actors contained within this manager."""
        result = len(self.__actors)
        return result

    def make_actors_from_data(self, data : pd.DataFrame):
        """Parameters: data (panda.DataFrame): the data in the format data name, opinion_1, opinion_2, ... opinion_n to be parsed into Actors."""
        for row in data.iloc:
            entity : Actor = Actor(row["name"])
            for entry in data.columns[1:]:
                entity.opinion.update({entry : row[entry]})
            self.__actors.append(entity)
