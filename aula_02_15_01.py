import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_lesao_corp_dolosa = df_ocorrencias[['cisp','lesao_corp_dolosa','lesao_corp_culposa', 'ano']]
df_lesao_corp_dolosa = df_lesao_corp_dolosa[df_lesao_corp_dolosa ['ano'].isin([2022,2023,2024])]
df_lesao_corp_dolosa = df_lesao_corp_dolosa.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()

df_lesao_corp_dolosa_culposo = df_ocorrencias[['cisp','lesao_corp_dolosa','lesao_corp_culposa']]
df_lesao_corp_dolosa_culposo = df_lesao_corp_dolosa_culposo.groupby(['cisp']).sum(['lesao_corp_dolosa','lesao_corp_culposa']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesao_corp_dolosa.head())

# Criando o array dos roubos de veiculos
array_lesao_corp_dolosa = np.array(df_lesao_corp_dolosa["lesao_corp_dolosa"])

# Obtendo a média dos roubos de veiculos
media_lesao_corp_dolosa = np.mean(array_lesao_corp_dolosa)

# Obtendo a mediana dos roubos de veiculos
mediana_lesao_corp_dolosa = np.median(array_lesao_corp_dolosa)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_lesao_corp_dolosa = abs((media_lesao_corp_dolosa - mediana_lesao_corp_dolosa) / mediana_lesao_corp_dolosa) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_lesao_corp_dolosa = np.max(array_lesao_corp_dolosa)
minimo_lesao_corp_dolosa = np.min(array_lesao_corp_dolosa)

# Obtendo a amplitude dos roubos de veiculos
amplitude_lesao_corp_dolosa = maximo_lesao_corp_dolosa - minimo_lesao_corp_dolosa

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.25, method='weibull')
q2_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.50, method='weibull')
q3_lesao_corp_dolosa = np.quantile(array_lesao_corp_dolosa, 0.75, method='weibull')
iqr_lesao_corp_dolosa = q3_lesao_corp_dolosa - q1_lesao_corp_dolosa

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_lesao_corp_dolosa = q3_lesao_corp_dolosa + (1.5 * iqr_lesao_corp_dolosa)
limite_inferior_lesao_corp_dolosa = q1_lesao_corp_dolosa - (1.5 * iqr_lesao_corp_dolosa)

# Filtrando o DataFrame roubos de veículos
df_lesao_corp_dolosa_outliers_superiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] > limite_superior_lesao_corp_dolosa]
df_lesao_corp_dolosa_outliers_inferiores = df_lesao_corp_dolosa[df_lesao_corp_dolosa['lesao_corp_dolosa'] < limite_inferior_lesao_corp_dolosa]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_lesao_corp_dolosa = np.var(array_lesao_corp_dolosa)
distancia_var_lesao_corp_dolosa = variancia_lesao_corp_dolosa / (media_lesao_corp_dolosa**2)
desvio_padrao_lesao_corp_dolosa = np.std(array_lesao_corp_dolosa)
coeficiente_var_lesao_corp_dolosa = desvio_padrao_lesao_corp_dolosa / media_lesao_corp_dolosa

# Obtendo a correlação entre os homicídios
# 0,9 a 1,0 (positivo ou negativo): correlação muito forte;
# 0,7 a 0,9 (positivo ou negativo): correlação forte;
# 0,5 a 0,7 (positivo ou negativo): correlação moderada;
# 0,3 a 0,5 (positivo ou negativo): correlação fraca;
# 0,0 a 0,3 (positivo ou negativo): não possui correlação.
correlacao_hom = np.corrcoef(df_lesao_corp_dolosa['lesao_corp_dolosa'],df_lesao_corp_dolosa['lesao_corp_culposa'])[0,1]

# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS HOMICÍDIOS DOLOSOS -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos homicídios dolosos é {media_lesao_corp_dolosa:.0f}")
print(f"A mediana dos homicídios dolosos é {mediana_lesao_corp_dolosa:.0f}")
print(f"A distância entre a média e a mediana é dos homicídios dolosos é {distancia_lesao_corp_dolosa:.2f} %")
print(f"O menor valor dos homicídios dolosos é {minimo_lesao_corp_dolosa:.0f}")
print(f"O maior valor dos homicídios dolosos é {maximo_lesao_corp_dolosa:.0f}")
print(f"A amplitude dos valores dos homicídios dolosos é {amplitude_lesao_corp_dolosa:.0f}")
print(f"O valor do q1 - 25% dos homicídios dolosos é {q1_lesao_corp_dolosa:.0f}")
print(f"O valor do q2 - 50% dos homicídios dolosos é {q2_lesao_corp_dolosa:.0f}")
print(f"O valor do q3 - 75% dos homicídios dolosos é {q3_lesao_corp_dolosa:.0f}")
print(f"O valor do iqr = q3 - q1 dos homicídios dolosos é {iqr_lesao_corp_dolosa:.0f}")
print(f"O limite inferior dos homicídios dolosos é {limite_inferior_lesao_corp_dolosa:.0f}")
print(f"O limite superior dos homicídios dolosos é {limite_superior_lesao_corp_dolosa:.0f}")
print(f"A variância dos homicídios dolosos é {variancia_lesao_corp_dolosa:.0f}")
print(f"A distância da variância X média dos homicídios dolosos é {distancia_var_lesao_corp_dolosa:.0f}")
print(f"O desvio padrão dos homicídios dolosos é {desvio_padrao_lesao_corp_dolosa:.0f}")
print(f"O coeficiente de variação dos homicídios dolosos é {coeficiente_var_lesao_corp_dolosa:.0f}")
print(f"A correlação dos homicídios é {correlacao_hom:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_lesao_corp_dolosa_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesao_corp_dolosa_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_lesao_corp_dolosa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_lesao_corp_dolosa_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre Homicídios Dolosos')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot de lesoes')
plt.boxplot(array_lesao_corp_dolosa,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Comparativo das Lesões Dolosas e Culposas')
plt.scatter(df_lesao_corp_dolosa['lesao_corp_dolosa'], df_lesao_corp_dolosa['lesao_corp_culposa'], color='purple')  
plt.xlabel('Lesões Corporais Dolosas')
plt.ylabel('Lesões Corporais Culposas')


# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_lesao_corp_dolosa_outliers_superiores_order = df_lesao_corp_dolosa_outliers_superiores.sort_values(by='lesao_corp_dolosa',ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_lesao_corp_dolosa_outliers_superiores_order['cisp'].astype(str),df_lesao_corp_dolosa_outliers_superiores_order['lesao_corp_dolosa'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas das Lesoes')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos Homicídios Dolosos: {media_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos Homicídios Dolosos: {mediana_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos Homicídios Dolosos: {distancia_lesao_corp_dolosa:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos Homicídios Dolosos: {maximo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos Homicídios Dolosos: {minimo_lesao_corp_dolosa:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos dos Homicídios Dolosos: {distancia_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos Homicídios Dolosos: {coeficiente_var_lesao_corp_dolosa:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre os Homicídios: {correlacao_hom:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
	
