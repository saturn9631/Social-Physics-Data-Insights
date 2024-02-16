#!/home/saturnfulcrum/Projects/PoliDataRectifier/src/.env/bin/python3.11

import pandas as pd

def get_data_from_user_input():
    data = pd.DataFrame({"Name": []})
    print("Please tell me the topics we will be dealing with.")
    while True:
        data[input("What is the topic to track: ")] = []
        if "yes" == input("Is that all the topics (type \"yes\" if that is all the topics): "):
            break
    topics = data.columns[1:]
    print(f"The topics inputted are {topics}.\n" +
        "The we are going to now look at what the different people think about the topics.")
    while True:
        row = {}
        row.update({"Name": input("What is the person's name: ")})
        for topic in topics:
            row.update({topic: input(f"what is the person's view on {topic}: ")})
        if "yes" == input("Is that all the people (type \"yes\" if that is all the people): "):
            break
        data.iloc[len(data) + 1,:] = pd.Dataframe(row)
    print(data)

def get_data_from_csv():
    try:
        data = pd.read_csv(input("Please input the relative path or the" +
            " absolute path of the csv file filled with people and there opinions.\n" +
            "(Data should be in a column format [person, topic 1, topic 2, ..., topic n]).\n" +
            "Path: "))
    except(FileNotFoundError):
        print("Sorry bro, I couldn't find that.")
        exit(1)
    print(data)
    return data

