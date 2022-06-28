import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
%matplotlib inline 

#CSV-Datei auslesen
dataInput = pd.read_csv('data.csv') 

print(type(dataInput))

print(dataInput)

print(dataInput.columns)

#Plotten der Verteilung
dataInput.hist('LSTAT')

dataInput.boxplot('LSTAT', showmeans=True)

#Imputation fehlender Werte in allen Spalten durch den Mittelwert der jeweiligen Spalte
dataInput=dataInput.fillna(dataInput.mean())

#Alle Stellen im Dataframe auf 2 Nachkommastellen runden
dataInput=dataInput.round(2)

#neue CSV Datei erstellen
dataInput.to_csv('dataNewMittelwert.csv')