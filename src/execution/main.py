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
    people_amount = int(input())
    data = unit_test(people_amount)

def unit_test(people_number = 10):
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
    return data

if __name__ == "__main__":
    main()
