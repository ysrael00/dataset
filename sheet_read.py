from openpyxl import load_workbook

# ler pasta de trabalho e planilha
wb = load_workbook("dataset/pivot_table.xlsx")
sheet = wb["relatorio"]

# acessando valor um valor especifico
print(sheet["A3"].value)
print(sheet["B3"].value)

# iterando valores por meio de loop pegando a coluna e linha A2 ate a linha 5 na planilha
for i in range (2,6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["c%s" %i].value
    print("{0} o aston martin vendeu {1} e o bentley vendeu {2}".format(ano, am, bt))