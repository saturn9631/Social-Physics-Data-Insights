#!shebang

import typing
#import multiprocessing
from faker import Faker
import pandas as pd
import random
import sys
sys.path.append("../lib/")
sys.path.append("../test/")

def main ():
    unit_test()

def unit_test():
    people_number = int(input("How many people do you want?: "))
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
    data_num = data.replace("Male", 20)
    data_num = data_num.replace("Female", -20)
    data_num = data_num.replace("Non-Binary", -50)
    data_num = data_num.replace("Unknown", 0)
    print(f"The scores of the people are\n{data_num}")

if __name__ == "__main__":
    main()
