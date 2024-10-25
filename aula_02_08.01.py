import pandas as pd 
import numpy as np

funcionarios_csv = 'BASES/Funcionarios.csv'

df_funcionarios = pd.read_csv(funcionarios_csv,sep=',', encoding='ISO-8859-1')

funcionarios_array = np.array(df_funcionarios['Salário'])

media_salario = np.mean(funcionarios_array)

mediana_salario = np.median(funcionarios_array)

distancia_salario = (( media_salario - mediana_salario) / mediana_salario) * 100

maior_salario = np.max(funcionarios_array)
menor_salario = np.min(funcionarios_array)

amplitude_salario = maior_salario - menor_salario

("\n --- ANÁLISE SOBRE OS SALÁRIOS ---- ")

print(f"A média de salário de funcionários é de R$ :{media_salario:.2f}")

print(f"A mediana dos salários dos funcionários é de R$:{mediana_salario:.2f}")

print(f"A distância entre a média e a mediana é de:{distancia_salario:.2f}",'%')



print(f"O maior salário entre os funcionários é de: R$ {maior_salario:.2f}")

print(f"O menor salário entre os funcionários é de: R$ {menor_salario:.2f}")

print(f"A amplitude entre o maior e o menor salário é de: R$ {amplitude_salario:.2f}")


# Conforme os dados apresentados, essa é uma empresa que paga altos salários para seus funcionários.Tendo em vista que mesmo o menor salário pago pela empresa sendo de R$ 3.100,00, ainda assim, está acima do salário mínimo. E pela distância entre a mediana e o maior salário, há mais salários altos do que baixos e mesmo assim os salários são simétricos por causa da diferença entre a amplitude e a mediana.



