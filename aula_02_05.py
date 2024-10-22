# pip install xlrd - Biblioteca para manipular arquivos xlsx
#pip isntall openpyxl - Biblioteca para manipular arquivos excel

import pandas as pd 

endereco_dados = 'BASES\ENEM_2020_2023.xlsx'

df_enem = pd.read_excel(endereco_dados)

print('----- BASE DE DADOS ENEM--------')
print(df_enem.head())