#!shebang
import Actor_Tensor
import numpy as np
import pandas as pd
import sympy as smp
import scipy as scp
import torch as tc
import transformers as facehugger

RUNNING = 0
FINNISHED_SUCCESFULLY = 1
ERROR = 2
CODE_OFFSET = -1

class Calculator_Interface(object):
    def __init__(self):
        self.data = pd.read_csv(input("input the path to the data: "))

    def run ():
        loop_status = RUNNING
        while loop_status == RUNNING:
            loop_status = update()

    def update():
        exit = 0
        if exit == 0:
            if True: #Placeholder condition
                code = RUNNING
            elif False: #Placeholder condition
                code = FINNISHED_SUCCESFULLY
        else:
            code = ERROR
        return code

    def __del__():
        print ("Good bye")
