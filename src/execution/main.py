#!shebang

import typing
#import multiprocessing
import sqlalchemy
from sqlalchemy import create_engine
#import pymysql
import pandas as pd
import numpy as np
import torch
import networkx

#import sys
#sys.path.append("../lib/")
#sys.path.append("../test/")

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


#Put into lib/data after 11/7/2024
class Database_Accessor:
    
    def __init__(self, sql_access_file_name = "SPDI_Data_Access.txt"):
        #print(f"Using access file {sql_access_file_name}\n")
        sql_access_file = open(sql_access_file_name, "r")
        con_string = sql_access_file.readline()
        con_string = con_string.replace("\n", "") #For some reason a newline character gets added to the database name and it is causing errors.
        sql_access_file.close()
        #print(f"Connection String {con_string}\n")
        self.sqla_engine = create_engine(con_string)

    def get_entry(self, entry, table_name):
        query = f"SELECT {entry} FROM {table_name}"
        entry = pd.read_sql(query, self.sqla_engine)
        return entry

    def get_table(self, table_name):
        table = self.get_entry("*", table_name)
        return table
    
    def __del__(self):
        self.sqla_engine.close()

#Put Game theory Modeler after 11/7/2024
def simulate_election(candidates, legislators, influencers):
    results = pd.DataFrame(columns = ["Name", "Win Chances")
    for index, candidate in candidates.iterrows():
        endorsement_count = -1
        total_endorsements = []

        for index, legislator in legislators:
            endorsement = (candidate["Ideology Score"] - legislator["Ideology Score"]) * 10
            if legislator["Endorsed Candidate"] == candidate["Name"]:
                endorsement += 15
            if legislator["Condemned Candidate"] == candidate["Name"]:
                endorsement += -15
            print(f"The legislator {legislator} supports {candidate} {endorsement}%\n")
            total_endorsements.append(endorsement)

        for index, influencer in influencers:
            endorsement = (candidate["Ideology Score"] - influencer["Ideology Score"]) * 10
            if influencer["Endorsed Candidate"] == candidate["Name"]:
                endorsement += 15
            if influencer["Condemned Candidate"] == candidate["Name"]:
                endorsement += -15
            print(f"The legislator {influencer} supports {candidate} {endorsement}%\n")
            total_endorsements.append(endorsement)
        print(f"The mean endorsement for {candidate} is {mean_endorsement}%\n")


if __name__ == "__main__":
    main()

