import pandas as pd 

#Importando base de Dados
endereco_dados = 'BASES/financeira.csv'

#Criando o DataFrame
df_financeira = pd.read_csv(endereco_dados,sep=',', encoding='iso-8859-1')  #Iso-8859-1 é para que ele entenda os caracters especiais

# Exibindo os dados cabeçalho
print(df_financeira.head())