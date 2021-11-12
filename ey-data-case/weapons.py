import pandas as pd
import os

print(os.getcwd())

weapons = pd.read_csv("datacase-data/weapons.csv", sep=";")
print(weapons.describe())
# print(weapons.head())

print("samples: \n")
samples = pd.read_csv("datacase-data/murderdata.csv", sep=";")
print(samples.describe())
# vettel = d1[]

weaponnames = ["Revolver", "Knife"] # , "Lead Pipe"]# ["Revolver", "Knife", "Lead Pipe", "Wrench", "Candlestick"]
for name in weaponnames:
    tmp = weapons[weapons["Type"] == name]
    print(name, end=": \n")
    print(tmp.describe())