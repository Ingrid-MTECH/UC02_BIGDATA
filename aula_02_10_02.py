import pandas as pd 
import numpy as np


titanic_csv = 'BASES/Titanic.csv'

df_tarifas = pd.read_csv(titanic_csv, sep=';', encoding='ISO- 8859-1')

print(df_tarifas.head())

("\n ---- TITANIC ----")

array_tarifa = np.array(df_tarifas['Fare'])
array_tarifa_mediana = np.array(df_tarifas['Fare'])
array_idade = np.array(df_tarifas['Age'])


# Obtendo os Quartis da idade - Método weibull

q1_idade = np.quantile(array_idade,0.25,method='weibull')
q2_idade = np.quantile(array_idade,0.50,method='weibull')
q3_idade = np.quantile(array_idade,0.75,method='weibull')
iqr_idade = q3_idade - q1_idade

# Obtendo os Quartis da Tarifa - Método weibull

q1_tarifa = np.quantile(array_tarifa,0.25,method='weibull')
q2_tarifa = np.quantile(array_tarifa,0.50,method='weibull')
q3_tarifa = np.quantile(array_tarifa,0.75,method='weibull')
iqr_tarifa = q3_tarifa - q1_tarifa

# Identificando os outliers superiores e inferiores da idade dos passageiros
limite_superior_idade = q3_idade + (1.5 * iqr_idade)
limite_inferior_idade = q1_idade - (1.5 * iqr_idade)
limite_superior_tarifa = q3_tarifa + (1.5 * iqr_tarifa)
limite_inferior_tarifa = q1_tarifa - (1.5 * iqr_tarifa)


# Filtrando o DataFrame financeira
df_financeira_idade_outliers_superiores = df_tarifas[df_tarifas['Age'] > limite_superior_idade]
df_financeira_idade_outliers_inferiores = df_tarifas[df_tarifas['Age'] < limite_inferior_idade]
df_financeira_tarifa_outliers_superiores = df_tarifas[df_tarifas['Fare'] > limite_superior_tarifa]
df_financeira_tarifa_outliers_inferiores = df_tarifas[df_tarifas['Fare'] < limite_inferior_tarifa]

("\n ---- MÉDIA TARIFA PAGAS TITANIC ----")
media_tarifa = np.mean(array_tarifa)
print(f"A média da tarifa do titanic é de R$: {media_tarifa:.2f}")

("\n ---- MEDIANA DAS TARIFAS PAGAS TITANIC ----")
mediana_tarifa = np.median(array_tarifa_mediana)
print(f"A mediana da tarifa do titanic é de R$: {mediana_tarifa:.2f}")


media_idade = np.mean(array_idade)


#Obtendo o máximo e o mínimo medida do valor da passagem

distancia_fare = abs((media_tarifa - mediana_tarifa) / mediana_tarifa ) * 100

print(f"A distância entre a média e a mediana é de:{distancia_fare:.2f}",'%')


#Obtento o máximo e o mínimo do valor da passagem e da idade

maximo_fare = np.max(array_tarifa)
minimo_fare = np.min(array_tarifa)


#Obtendo a amplitude do valor da passagem e da idade

amplitude_fare = maximo_fare - minimo_fare

#Obtendo as medidas de dispersão da renda e do valor emprestado

variancia_idade = np.var(array_idade)
distancia_var_idade = variancia_idade / (media_idade**2)
desvio_padrao_idade = np.std(array_idade)
coeficiente_var_idade = desvio_padrao_idade / media_idade

variancia_tarifa = np.var(array_tarifa)
distancia_var_tarifa = variancia_tarifa / (media_tarifa**2)
desvio_padrao_tarifa = np.std(array_tarifa)
coeficiente_tarifa = desvio_padrao_tarifa / media_tarifa



print(f"O maior valor de passagem paga é de:{maximo_fare:.2f}")
print(f"O menor valor de passagem paga é de:{minimo_fare:.2f} ")
print(f"A amplitude em relação ao valor de passagem é de:{amplitude_fare:2f}")

print('\nMedidas de Tendência Central Idade')

print(f"O valor do q1 - 25% da idade é  {q1_idade}")
print(f"O valor do q2 - 50% da idade é  {q2_idade}")
print(f"O valor do q3 - 75% da idade é  {q3_idade}")
print(f"O valor do iqr = q3 - q1 da idade é {iqr_idade}")
print(f"O limite inferior da idade é {limite_inferior_idade}")
print(f"O limite superior da idade é {limite_superior_idade}")
print(f"A variancia das idades dos clientes é {variancia_idade:.2f}")
print(f"A distancia da variância x média das idades é {distancia_var_idade:.2f}")
print(f"O desvio padrão das idades é R$ {desvio_padrao_idade:.2f}")
print(f"O coeficiente de variação da idades é {coeficiente_var_idade:.2f}")


print('\nMedidas de Tendência Central Tarifa')

print(f"O valor do q1 - 25% da renda é R$ {q1_tarifa}")
print(f"O valor do q2 - 50% da renda é R$ {q2_tarifa}")
print(f"O valor do q3 - 75% da renda é R$ {q3_tarifa}")
print(f"O valor do iqr = q3 - q1 da renda é R$ {iqr_tarifa}")
print(f"O limite inferior da tarifa é R$ {limite_inferior_tarifa}")
print(f"O limite superior da tarifa é R$ {limite_superior_tarifa}")
print(f"A variancia da tarifa dos clientes é R$ {variancia_tarifa:.2f}")
print(f"A distancia da variância x média das tarifas é de: {distancia_var_tarifa:.2f}")
print(f"O desvio padrão da tarifa é R$ {desvio_padrao_tarifa:.2f}")
print(f"O coeficiente de variação da tarifa é {coeficiente_tarifa:.2f}")

print('\n- Verificando a existência de outliers inferiores -')

if len(df_financeira_idade_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_idade_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')

if len(df_financeira_tarifa_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_idade_outliers_superiores)


    