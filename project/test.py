import csv
import pandas as pd
import numpy as np
import sys

class aplication():
    
    def __init__(self, name):
        self.name = name
        self.read_excel()

    def read_excel (self):
        excel = pd.read_excel('issf.xlsx', sheet_name = ['1 Datos Ubic ','2 Valoración'])
        print(excel)
        one = excel['1 Datos Ubic ']
        dos =  excel['2 Valoración']
        one.to_csv('one.csv', index=False,sep=',')
        dos.to_csv('dos.csv', index=False,sep=',')





if __name__ == "__main__": 

    app = aplication("Jazz")