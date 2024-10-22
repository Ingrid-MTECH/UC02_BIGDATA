# import pandas as pd 

# #Importando base de Dados
# endereco_dados = 'BASES/ENEM_2020_2023.xlsx'

# #Criando o DataFrame
# df_financeira = pd.read_csv(endereco_dados,sep=';', encoding='iso-8859-1')  #Iso-8859-1 é para que ele entenda os caracters especiais

# # Exibindo os dados cabeçalho
# print(df_financeira.head())

import pandas as pd 

dados_rio = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df = pd.read_csv(dados_rio, sep=';', encoding='ISO-8859-1')
print(df.head())