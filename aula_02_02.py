# #Código usando séries
# import pandas as pd

# media = pd.Series([80,90,10,20,30,40,70,100,30,50])
# ap = media[media >= 70]
# rp = media[media < 70]
# print(ap)
# print(rp)


# 1 - Faça um programa que leia duas séries com 10 números inteiros cada e ao final mostre a soma, a subtração, a multiplicação e a divisão entre elas

# import pandas as pd
# nota_01 = pd.Series([100,50,40,30,80,10,75,60,90,45])
# nota_02 = pd.Series([60,20,90,40,10,50,70,100,88,75])

# soma = (nota_01 + nota_02)
# subtracao = (nota_01 - nota_02)
# multiplicacao = (nota_01 * nota_02)
# divisao = (nota_01 / nota_02)

# print(soma)
# print(subtracao)
# print(multiplicacao)
# print(divisao)

# Duas séries com 2 temperaturas (Máxima e mínima) e a diferença entre as duas. Média da temperatura máxima e a média da mínima.
import pandas as pd

temperatura_maxima = pd.Series([38,40,42,45,60,50,48])
temperatura_minima = pd.Series([20,17,10,15,25,23,13])

media_max= temperatura_maxima.mean()
media_min = temperatura_minima.mean()

print("Diferença entre temperaturas:", temperatura_maxima - temperatura_minima)
print(f"Média da temperatura máxima:{media_max:.1f}")
print(f"Média da temperatura mínima:{ media_min:.1f}")
