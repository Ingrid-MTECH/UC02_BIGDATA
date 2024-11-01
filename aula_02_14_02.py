import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados,sep=';',encoding='iso-8859-1')
df_roubo_veiculo = df_ocorrencias[['cisp','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['cisp']).sum(['roubo_veiculo']).reset_index()

df_roubo_veiculo_culposo = df_ocorrencias[['cisp','roubo_veiculo','furto_veiculos']]
df_roubo_veiculo_culposo = df_roubo_veiculo_culposo.groupby(['cisp']).sum(['roubo_veiculo','furto_veiculos']).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_roubo_veiculo.head())

# Criando o array dos roubos de veiculos
array_roubo_veiculo = np.array(df_roubo_veiculo["roubo_veiculo"])

# Obtendo a média dos roubos de veiculos
media_roubo_veiculo = np.mean(array_roubo_veiculo)

# Obtendo a mediana dos roubos de veiculos
mediana_roubo_veiculo = np.median(array_roubo_veiculo)

# Obtendo a distância entre a média e a mediana dos roubos de veiculos
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

# Obtendo o máximo e o mínimo dos roubos de veiculos
maximo_roubo_veiculo = np.max(array_roubo_veiculo)
minimo_roubo_veiculo = np.min(array_roubo_veiculo)

# Obtendo a amplitude dos roubos de veiculos
amplitude_roubo_veiculo = maximo_roubo_veiculo - minimo_roubo_veiculo

# Obtendo os Quartis dos roubos de veiculos - Método weibull
q1_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubo_veiculo, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers superiores e inferiores dos roubos de veículos
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando o DataFrame roubos de veículos
df_roubo_veiculo_outliers_superiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] > limite_superior_roubo_veiculo]
df_roubo_veiculo_outliers_inferiores = df_roubo_veiculo[df_roubo_veiculo['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Obtendo as medidas de dispersão dos roubos de veículos
variancia_roubo_veiculo = np.var(array_roubo_veiculo)
distancia_var_roubo_veiculo = variancia_roubo_veiculo / (media_roubo_veiculo**2)
desvio_padrao_roubo_veiculo = np.std(array_roubo_veiculo)
coeficiente_var_roubo_veiculo = desvio_padrao_roubo_veiculo / media_roubo_veiculo

# Obtendo a correlação entre os homicídios
# 0,9 a 1,0 (positivo ou negativo): correlação muito forte;
# 0,7 a 0,9 (positivo ou negativo): correlação forte;
# 0,5 a 0,7 (positivo ou negativo): correlação moderada;
# 0,3 a 0,5 (positivo ou negativo): correlação fraca;
# 0,0 a 0,3 (positivo ou negativo): não possui correlação.
correlacao_hom = np.corrcoef(df_roubo_veiculo_culposo['roubo_veiculo'],df_roubo_veiculo_culposo['furto_veiculos'])[0,1]

# Exibindo os dados sobre os roubos de veiculos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS roubos -----------")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média dos roubos é {media_roubo_veiculo:.0f}")
print(f"A mediana dos roubos é {mediana_roubo_veiculo:.0f}")
print(f"A distância entre a média e a mediana é dos roubos é {distancia_roubo_veiculo:.2f} %")
print(f"O menor valor dos roubos é {minimo_roubo_veiculo:.0f}")
print(f"O maior valor dos roubos é {maximo_roubo_veiculo:.0f}")
print(f"A amplitude dos valores dos roubos é {amplitude_roubo_veiculo:.0f}")
print(f"O valor do q1 - 25% dos roubos é {q1_roubo_veiculo:.0f}")
print(f"O valor do q2 - 50% dos roubos é {q2_roubo_veiculo:.0f}")
print(f"O valor do q3 - 75% dos roubos é {q3_roubo_veiculo:.0f}")
print(f"O valor do iqr = q3 - q1 dos roubos é {iqr_roubo_veiculo:.0f}")
print(f"O limite inferior dos roubos é {limite_inferior_roubo_veiculo:.0f}")
print(f"O limite superior dos roubos é {limite_superior_roubo_veiculo:.0f}")
print(f"A variância dos roubos é {variancia_roubo_veiculo:.0f}")
print(f"A distância da variância X média dos roubos é {distancia_var_roubo_veiculo:.0f}")
print(f"O desvio padrão dos roubos é {desvio_padrao_roubo_veiculo:.0f}")
print(f"O coeficiente de variação dos roubos é {coeficiente_var_roubo_veiculo:.0f}")
print(f"A correlação dos homicídios é {correlacao_hom:.1f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_roubo_veiculo_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_roubo_veiculo_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_roubo_veiculo_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_roubo_veiculo_outliers_superiores)

# Visualizando os dados sobre os roubos de veículos
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2,2,figsize=(16,7))
plt.suptitle('Análise dos Dados sobre roubos')

# posição 01: Gráfico dos Roubos de Veículos
plt.subplot(2,2,1)
plt.title('BoxPlot dos roubos')
plt.boxplot(array_roubo_veiculo,vert=False,showmeans=True)

# posição 02: Histograma dos Roubos de Veículos
plt.subplot(2,2,2)
plt.title('Comparativo roubos e Culposos')
plt.scatter(df_roubo_veiculo_culposo['roubo_veiculo'],df_roubo_veiculo_culposo['furto_veiculos'])
plt.xlabel('Roubos')
plt.ylabel('Furtos')

# posição 03: Medidas descritivas das passagens
plt.subplot(2,2,3)
df_roubo_veiculo_outliers_superiores_order = df_roubo_veiculo_outliers_superiores.sort_values(by='roubo_veiculo',ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_roubo_veiculo_outliers_superiores_order['cisp'].astype(str),df_roubo_veiculo_outliers_superiores_order['roubo_veiculo'])

# posição 04: Medidas descritivas dos Roubos de Veículos
plt.subplot(2,2,4)
plt.title('Medidas Descritivas dos roubos')
plt.axis('off')
plt.text(0.1,0.9,f'Média dos roubos: {media_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.8,f'Mediana dos roubos: {mediana_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.7,f'Distância entre Média e Mediana dos roubos: {distancia_roubo_veiculo:.2f}%',fontsize=12)
plt.text(0.1,0.6,f'Maior valor dos roubos: {maximo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.5,f'Menor valor dos roubos: {minimo_roubo_veiculo:.0f}',fontsize=12)
plt.text(0.1,0.4,f'Distância entre a Variância e Média dos dos roubos: {distancia_var_roubo_veiculo:.2f}',fontsize=12)
plt.text(0.1,0.3,f'Coeficiente de variação dos roubos: {coeficiente_var_roubo_veiculo:.2f}',fontsize=12)
plt.text(0.1,0.2,f'Correlação entre os Homicídios: {correlacao_hom:.2f}',fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()