#!shebang

import typing
#import multiprocessing
#import pymysql
import pandas as pd
import numpy as np
import torch
import networkx

import sys
#For importing modules from the lib folder
#sys.path.insert(0,"")
sys.path.insert(0,"../lib/data")
sys.path.insert(0,"../lib/game")
sys.path.insert(0,"../lib/institution")
sys.path.insert(0,"../lib/psychology")
import sql_accessor
import election


def main ():
    accessor = Database_Accessor()
    legislators = accessor.get_table("Legislator_Table")
    print(f"Here is the legislator data: {legislators}\n")
    candidates = accessor.get_table("Presidential_Candidates_Table")
    print(f"Here is the presidential candidates: {candidates}\n")
    influencers = accessor.get_table("Influencers_Table")
    print(f"Here is the influencers and celebrities that will influence voters {influencers}\n")

    print("Running election simulation\n")
    simulate_election(candidates, legislators, influencers)



if __name__ == "__main__":
    main()

