import pandas as pd
import numpy as np

funcionarios_csv = 'BASES/funcionarios.csv'

df_funcionarios = pd.read_csv(funcionarios_csv, sep=',',encoding='ISO-8859-1')
print(df_funcionarios.head())

funcionarios_array = np.array(df_funcionarios['Idade'])
tempo_array = np.array(df_funcionarios['Tempo'])

media_idade = np.mean(funcionarios_array)
mediana_idade = np.median(funcionarios_array)
distancia_idade = ((media_idade - mediana_idade) / mediana_idade) * 100
maior_idade = np.max(funcionarios_array)
menor_idade = np.min(funcionarios_array)
amplitude_idade = (maior_idade - menor_idade)

media_tempo = np.mean(tempo_array)
mediana_tempo = np.median(tempo_array)
distancia_tempo = ((media_tempo - mediana_tempo) / mediana_tempo) * 100
maior_tempo = np.max(tempo_array)
menor_tempo = np.min(tempo_array)
amplitude_tempo = (media_tempo - media_tempo)

("\n --- ANÁLISE SOBRE A IDADE DOS FUNCIONÁRIOS --- ")
print(f"A média de idade entre os funcionários é de: {media_idade:.2f}")
print(f"A mediana de idade entre os funcionários é de: {mediana_idade:.2f}")
print(f"A distância da idade entre os funcionários corresponde a:{distancia_idade:.2f}",'%')
print("A maior idade entre os funcionários é de:", maior_idade)
print("A menor idade entre os funcionários é de:", menor_idade)
print(f"A amplitude da idade é de:{amplitude_idade:.2f}")

print("\n --- ANÁLISE SOBRE O TEMPO DOS FUNCIONÁRIOS --- ")

print(f"A média de tempo entre os funcionários é de: {media_tempo:.2f}")
print(f"A mediana de tempo entre os funcionários é de: {mediana_tempo:.2f}")
print(f"A distância de tempo entre os funcionários corresponde a:{distancia_tempo:.0f}")
print("o maior tempo entre os funcionários é de:", maior_tempo)
print("o menor tempo entre os funcionários é de:", menor_tempo)
print(f"A amplitude do tempo é de:{amplitude_tempo:.2f}")

# Com base nos dados analisados, é possível constatar que a idade dos funcionários é simétrica pois não há uma discrepância muito grande entre os valores da amplitude e a mediana apresentadas.

