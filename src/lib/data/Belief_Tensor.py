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



def unit_test():

    response = input("Do you want to load data (l) or input data (i). Please input only"
        + " the options listed: ")
    data = 0; #placeholder
    if response == "l":
        data = pd.read_csv(input("please input the file (full path if it in a different directory): "))
    elif response == "i":
        data = get_data_from_usr()
    else:
        print("You are really good at following directions, so am I")
        exit(132)
        return
    print("This is the data you inputted: " + data)




def get_data_from_usr():
    data = {"Person": [], "Age": [], "Gender": [], "Race": [], "Ethinicity": [],
                "State": [], "Subdivision": []}
    index = 0
    while True:
        usr_input = input("Input person, or if your done input \"Done\": ")
        if usr_input == "Done":
            break
        else:
            data["Person"].append(usr_input)
            data["Age"].append(int(input("Please input the person's age (Please don't" +
                " put anything besides pure numbers): ")))
            data["Gender"].append(input("What is the person's gender: "))
            data["Race"].append(input("Input their race: "))
            data["Ethinicity"].append(input("Input the ethinicity: "))
            data["State"].append(input("Input the residing state: "))
            data["Subdivision"].append(input("Is there any meaningful " +
                "subdivision (state/provinces/prefectures): "))
    data = pd.DataFrame(data)
    response = input("Would you like to save this data(y/n): ")
    if response == "y":
        data.to_csv(input("What should be the name of the file: "))
    return data

unit_test()




