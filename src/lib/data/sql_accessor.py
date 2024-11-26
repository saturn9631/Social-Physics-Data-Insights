import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
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
