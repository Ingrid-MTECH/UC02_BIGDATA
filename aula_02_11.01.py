import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

#Exibindo apenas as informações de delegacia (cisp) e roubo de veículos

df_delegacia = pd.read_csv(endereco_dados,sep=';', encoding='ISO-8859-1')
df_delegacias_roubo = df_delegacia[['cisp','roubo_veiculo']]
print(df_delegacia.head())
print(df_delegacias_roubo.head())

#Exibindo o array da delegacia e do roubo de veículos

array_delegacia = np.array(df_delegacias_roubo["cisp"])
array_roubo = np.array(df_delegacias_roubo["roubo_veiculo"])

#Exibindo a média de roubos por delegacia
media_roubo = np.mean(array_roubo)


#Exibindo a mediana de roubos por delegacia

mediana_roubo = np.median(array_roubo)


#Exibindo a distância entre a média da mediana

distancia_roubo = abs((media_roubo - mediana_roubo) / mediana_roubo ) * 100


#Exibindo máximo e mínimo de roubos por delegacia

maximo_roubo = np.max(df_delegacias_roubo)
minimo_roubo = np.min(df_delegacias_roubo)

# Exibindo a amplitude do máximo e do mínimo de roubos

amplitude_roubo = maximo_roubo - minimo_roubo

#Obtendo os quartis do número de roubos

q1_roubos = np.quantile(array_roubo,0.25,method='weibull')
q2_roubos = np.quantile(array_roubo,0.50,method='weibull')
q3_roubos = np.quantile(array_roubo,0.75,method='weibull')
iqr_roubo = q3_roubos - q1_roubos




