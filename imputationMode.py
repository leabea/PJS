import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

dataInput = pd.read_csv('data.csv') 

print(type(dataInput))

print(dataInput)

dataInput.boxplot('LSTAT', showmeans=True)

#für jede Column durchgehen
for column in dataInput:
    dataInput[column] = dataInput[column].fillna(dataInput[column].mode()[0])

dataInput=dataInput.round(2)

dataInput.to_csv('dataNewMode.csv')