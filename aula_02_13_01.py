import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_recuperacao_veiculo = df_ocorrencias[['aisp','ano','recuperacao_veiculos','cvli']]
df_recuperacao_veiculo = df_recuperacao_veiculo[df_recuperacao_veiculo['ano'].isin([2022,2023])]
df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['aisp']).sum(['recuperacao_veiculos']).reset_index()
df_recuperacao_veiculo = df_recuperacao_veiculo.groupby(['aisp']).sum(['cvli']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_recuperacao_veiculo.head())

# Criando o array dos recuperacao de veiculos
array_recuperacao_veiculo = np.array(df_recuperacao_veiculo["recuperacao_veiculos"])
array_cvli = np.array(df_recuperacao_veiculo["cvli"])

# Obtendo a média dos recuperacao de veiculos
media_recuperacao_veiculo = np.mean(array_recuperacao_veiculo)
media_cvli = np.mean(array_cvli)

# Obtendo a mediana dos recuperacao de veiculos
mediana_recuperacao_veiculo = np.median(array_recuperacao_veiculo)
mediana_cvli = np.median(array_cvli)

# Obtendo a distância entre a média e a mediana dos recuperacao de veiculos
distancia_recuperacao_veiculo = abs((media_recuperacao_veiculo - mediana_recuperacao_veiculo) / mediana_recuperacao_veiculo) * 100
distancia_cvli = abs((media_cvli - mediana_cvli) / mediana_cvli) * 100

# Obtendo o máximo e o mínimo dos recuperacao de veiculos
maximo_recuperacao_veiculo = np.max(array_recuperacao_veiculo)
minimo_recuperacao_veiculo = np.min(array_recuperacao_veiculo)
maximo_cvli = np.max(array_cvli)
minimo_cvli = np.min(array_cvli)

# Obtendo a amplitude dos recuperacao de veiculos
amplitude_recuperacao_veiculo = maximo_recuperacao_veiculo - minimo_recuperacao_veiculo
amplitude_cvli = maximo_cvli - minimo_cvli

# Obtendo os Quartis dos recuperacao de veiculos - Método weibull
q1_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.25, method='weibull')
q2_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.50, method='weibull')
q3_recuperacao_veiculo = np.quantile(array_recuperacao_veiculo, 0.75, method='weibull')
iqr_recuperacao_veiculo = q3_recuperacao_veiculo - q1_recuperacao_veiculo

q1_cvli = np.quantile(array_cvli, 0.25, method='weibull')
q2_cvli = np.quantile(array_cvli, 0.50, method='weibull')
q3_cvli = np.quantile(array_cvli, 0.75, method='weibull')
iqr_cvli = q3_cvli - q1_cvli


# Identificando os outliers superiores e inferiores dos recuperacao de veículos
limite_superior_recuperacao_veiculo = q3_recuperacao_veiculo + (1.5 * iqr_recuperacao_veiculo)
limite_inferior_recuperacao_veiculo = q1_recuperacao_veiculo - (1.5 * iqr_recuperacao_veiculo)

limite_superior_cvli = q3_cvli + (1.5 * iqr_cvli)
limite_inferior_cvli = q1_cvli - (1.5 * iqr_cvli)

# Filtrando o DataFrame recuperacao de veículos
df_recuperacrao_veiculo_outliers_superiores = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] > limite_superior_recuperacao_veiculo]
df_recuperacao_veiculo_outliers_inferiores = df_recuperacao_veiculo[df_recuperacao_veiculo['recuperacao_veiculos'] < limite_inferior_recuperacao_veiculo]
df

# Obtendo as medidas de dispersão dos recuperacao de veículos
variancia_recuperacao_veiculo = np.var(array_recuperacao_veiculo)
distancia_var_recuperacao_veiculo = variancia_recuperacao_veiculo / (media_recuperacao_veiculo**2)
desvio_padrao_recuperacao_veiculo = np.std(array_recuperacao_veiculo)
coeficiente_var_recuperacao_veiculo = desvio_padrao_recuperacao_veiculo / media_recuperacao_veiculo



# Exibindo os dados sobre os recuperacao de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS recuperacao DE VEÍCULOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos recuperacao de veículos é {media_recuperacao_veiculo:.0f}")
print(f"A mediana dos recuperacao de veículos é {mediana_recuperacao_veiculo:.0f}")
print(f"A distância entre a média e a mediana é dos recuperacao de veículos é {distancia_recuperacao_veiculo:.2f} %")
print(f"O menor valor dos recuperacao de veículos é {minimo_recuperacao_veiculo:.0f}")
print(f"O maior valor dos recuperacao de veículos é {maximo_recuperacao_veiculo:.0f}")
print(f"A amplitude dos valores dos recuperacao de veículos é {amplitude_recuperacao_veiculo:.0f}")
print(f"O valor do q1 - 25% dos recuperacao de veículos é {q1_recuperacao_veiculo:.0f}")
print(f"O valor do q2 - 50% dos recuperacao de veículos é {q2_recuperacao_veiculo:.0f}")
print(f"O valor do q3 - 75% dos recuperacao de veículos é {q3_recuperacao_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 dos recuperacao de veículos é {iqr_recuperacao_veiculo:.0f}")
print(f"O limite inferior dos recuperacao de veículos é {limite_inferior_recuperacao_veiculo:.0f}")
print(f"O limite superior dos recuperacao de veículos é {limite_superior_recuperacao_veiculo:.0f}")
print(f"A variância dos recuperacao de veículos é {variancia_recuperacao_veiculo:.0f}")
print(f"A distância da variância X média dos recuperacao de veículos é {distancia_var_recuperacao_veiculo:.0f}")
print(f"O desvio padrão dos recuperacao de veículos é {desvio_padrao_recuperacao_veiculo:.0f}")
print(f"O coeficiente de variação dos recuperacao de veículos é {coeficiente_var_recuperacao_veiculo:.0f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_recuperacao_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_recuperacao_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_recuperacrao_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_recuperacao_veiculo_outliers_superiores)

# Visualizando os dados sobre os recuperacao de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre recuperacao de Veículos')

# posição 01: Gráfico dos recuperacao de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot dos recuperacao de Veículos')
plt.boxplot(array_recuperacao_veiculo,vert=False,showmeans=True)

# posição 02: Histograma dos recuperacao de Veículos
plt.subplot(2,2,2)
plt.title('Histograma dos recuperacao de Veículos')
plt.hist(array_recuperacao_veiculo,bins=100,edgecolor='black')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_recuperacao_veiculo_outliers_superiores_order = df_recuperacao_veiculo_outliers_superiores.sort_values(by='recuperacao_veiculos',ascending=True)
plt.title('Ranking das Delegacias com Outliers Superiores')
plt.barh(df_recuperacao_veiculo_outliers_superiores_order['aisp'].astype(str),df_recuperacao_veiculo_outliers_superiores_order['recuperacao_veiculos'] )

# posição 04: Medidas descritivas dos recuperacao de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos recuperacao de Veículos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos recuperacao de Veículos {media_recuperacao_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos recuperacao de Veículos {mediana_recuperacao_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos recuperacao de Veículos {distancia_recuperacao_veiculo:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos recuperacao de Veículos {maximo_recuperacao_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos recuperacao de Veículos {minimo_recuperacao_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos recuperacao de Veículos {distancia_var_recuperacao_veiculo:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos recuperacao de Veículos {coeficiente_var_recuperacao_veiculo:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()