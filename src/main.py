#!shebang
import typing
import sys
sys.path.append("lib/")
sys.path.append("test/")
import Actor_Tensor
import pandas as pd
import sympy as smp
import torch as pt

RUNNING = 0
FINNISHED = 1
def main ():
    data = initialization()
    loop_status = RUNNING
    while loop_status == RUNNING:
        loop_status = update()
    deinitialization()

def initialization():
    data = pd.read_csv(input("input the path to the data: "))
    return data

def deinitialization():
    print ("Good bye")

def update():
    pass


if __name__ == "__main__":
    main()
