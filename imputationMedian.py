import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

dataInput = pd.read_csv('data.csv') 

print(type(dataInput))

print(dataInput)

dataInput.boxplot('LSTAT', showmeans=True)

dataInput=dataInput.fillna(dataInput.median())

dataInput=dataInput.round(2)

dataInput.to_csv('dataNewMedian.csv')