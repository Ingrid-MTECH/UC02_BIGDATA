#Lista com os anos e quantiade de homicidio doloso

# import pandas as pd  

# exercicio_csv = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# df_homicidio = pd.read_csv(exercicio_csv, sep=';', encoding='ISO-8859-1')


# homicidio = df_homicidio[['ano', 'hom_doloso']]
# homicidio = homicidio.groupby(['ano']).sum(['hom_doloso']).reset_index()

# print(homicidio.head())


# Lista das delegacias (CISP), número de registro de homicidio doloso e culposo

import pandas as pd

registro_csv = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

df_registro = pd.read_csv(registro_csv, sep=';', encoding='ISO-8859-1')

df_delegacias = df_registro[['cisp', 'hom_doloso', 'hom_culposo']]
df_delegacias = df_delegacias.groupby(['cisp']).sum(['hom_doloso','hom_culposo']).reset_index() #Reset.index organiza os dados por ordem alfabética

print(df_delegacias.head())

