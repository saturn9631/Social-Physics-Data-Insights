import pandas as pd
import random
from faker import Faker

import sys
#sys.path.append("../lib/game")
#sys.path.append("../lib/institution")
#sys.path.append("../lib/psychology")
#sys.path.append("../lib/data")
import election
import data_filters



def election_test():
    candidate_number = int(input("How many candidates are running?: "))
    candidates = make_people(candidate_number)
    candidates = data_filters.remove_unknown_people(candidates)
    popularity = []
    print(f"The type of candidates is {type(candidates)}\n")
    for candidate in candidates.iterrows():
        popularity.append(random.randrange(0,11))
    candidates["Popularity"] = popularity

    influencer_number = int(input("How many influencers are interested in the election?: "))
    influencers = make_people(influencer_number)
    influeuncers = data_filters.remove_unknown_people(influencers)
    popularity = []
    for influencer in influencers.iterrows():
        popularity.append(random.randrange(0,11))
    influencers["Popularity"] = popularity

    print(f"Here are the candidates:\n{candidates}\n Here are the influencers:\n{influencers}\n")

def make_people(people_number):
    data = {};
    faking = Faker()
    genders = []
    names = []
    addresses = []
    for i in range(people_number):
        gender = random.randrange(4)
        if gender == 0:
            genders.append("Unknown")
            names.append("N/A")
        elif gender == 1:
            genders.append("Non-Binary")
            names.append(faking.name_nonbinary())
        elif gender == 2:
            genders.append("Female")
            names.append(faking.name_female())
        else:
            genders.append("Male")
            names.append(faking.name_male())
        addresses.append(faking.address())
    data.update({ "name" : names, "gender" : genders, "Address" : addresses })
    data = pd.DataFrame(data)
    print(f"Here is the resulting data\n{data}")
    #ideaology_classifier = Classifier(pd.DataFrame({
        #"Gender": {"Male": 20, "Female": -20, "Non-Binary": 45},
    #}))
    return data
