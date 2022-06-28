import pandas as pd
import matplotlib.pyplot as plt

dataInput = pd.read_csv('data.csv', header=None) 

print(type(dataInput))

print(dataInput.columns)

#erste Variante: listenweiser Ausschluss, d.h. Entfernen von Datenreihen, bei denen mindestens ein Wert NaN ist
#hier habe ich beispielhaft alle fehlenden Werte in der Spalte 12 samt ihrer Reihe eliminiert
dataInput.dropna(subset = [12], inplace=True)

dataInput.to_csv('dataListwise.csv')


#probiere einen json file zu erstellen
csv_file = 'dataListwise.csv'
csv_file.to_json("ersterListwise.json")
print('hi')


