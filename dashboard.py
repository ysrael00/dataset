import pandas as pd

# importanto dados
data = pd.read_excel("dataset/VendaCarros.xlsx")
print (data)
# lista os primeiros registros
print(data.head())

# lista os ultimos registro
print(data.tail())

# contagem de valores por fabricante
print(data["Fabricante"].value_counts())



