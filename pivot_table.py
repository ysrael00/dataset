import pandas as pd

# importanto dados
data = pd.read_excel("dataset/VendaCarros.xlsx")
# print(type(data))

# selecionando coluna espeficas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

# criando a tabela pivo
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

# exportando tabela pivo em arquivo excel
pivot_table.to_excel("dataset/pivot_table.xlsx", "relatorio")
