import pandas as pd
import matplotlib.pyplot as plt

dataInput = pd.read_csv('data.csv', header=None) 

print(type(dataInput))

print(dataInput.columns)

#erste Variante: listenweiser Ausschluss, d.h. Entfernen von Datenreihen, bei denen mindestens ein Wert NaN ist
dataInput.dropna(subset = [12], inplace=True)

dataInput.to_csv('dataListwise.csv')



