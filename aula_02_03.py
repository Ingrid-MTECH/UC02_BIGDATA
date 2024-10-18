# 1 – O Ministro da Saúde, entrou em contato com você e te solicitou um auxílio, para obter as seguintes informações
# sobre os dados da vacinação da covid nos últimos quatro anos:
# - O total e a média de pessoas vacinadas no período.
# - O total e a média da população do Brasil.
# - A taxa de vacinação anual, dos últimos 4 anos, sabendo que para se chegar a esse número, deve-se dividir a quantidade
# de vacinados pela quantidade da população.
# Ele te enviou os seguintes dados:
# ● População Vacinada: 30000000, 25000000, 10000000, 5000000
# ● População Total: 213317639, 214477744, 215574303, 216687971
# E pediu para apresentar na tela o resultado das informações solicitadas.

import pandas as pd

def formatar(valor):
    return "{:.2f}%".format(valor)

vacinadas = pd.Series([30000000,25000000,10000000,5000000])
populacao = pd.Series([213317639,214477744,215574303,216687971 ])
tx_vacinacao = ((vacinadas / populacao) * 100).apply(formatar)

print("\n---- Dados da vacinação ---")
print(f"Total das pessoas vacinadas: {vacinadas.sum():.1f}")
print("\n---- Média dos vacinados ---")
print(f"Média das pessoas vacinadas: {vacinadas.mean():.1f}")
print("\n---- Dados da população ---")
print(f"Total da população do Brasil: {populacao.sum():.1f}")
print("\n---- Total da população ---")
print(f"Média da população do Brasil: {populacao.mean():.1f}")
print(f"Taxa de vacinação anual dos últimos 4 anos:") 
print("\n---- Taxa de vacinação ---")
print(f"{tx_vacinacao}")


# 2 - O Delegado responsável pela Delegacia de roubos e furtos de automóveis, entrou em contato com você e te
# solicitou um auxílio, para obter duas informações:
# - A quantidade de roubos de automóveis + furto de automóveis diária, dos últimos 7 dias.
# - A taxa de recuperação de automóveis diária, dos últimos 7 dias, sabendo que para se chegar a esse número, deve-se
# dividir a quantidade de recuperação de automóveis pela quantidade de roubo de automóveis.
# Ele te enviou os seguintes dados:
# ● Roubo de automóveis: 100,90,80,120,110,90,70
# ● Furto de automóveis: 80,60,70,60,100,50,30
# ● Recuperação de automóveis: 70,50,90,80,100,70,50
# E pediu para apresentar na tela o resultado das informações solicitadas

import pandas as pd
def formatar(valor):
    return "{:.2f}%".format(valor)

roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
recuperacao = pd.Series([70,50,90,80,100,70,50])
tx_recuperacao = ((recuperacao / roubo) * 100).apply(formatar)
roubo_furto = roubo + furto
print("\n---- Dados da quantidade de roubos  ---")
print("A quantidade de roubos de automóveis + furto de automóveis diária, dos últimos 7 dias")
print(roubo + furto)
print("\n---- Dados da recuperação de automóveis ---")
print("A taxa de recuperação de automóveis diária, dos últimos 7 dias:")
print(tx_recuperacao)
print("\n---- Total geral de Roubos ---")
print(f"{roubo_furto.sum()}")

# O Gerente de uma loja pediu o seu auxílio para que a cada 7 dias, calculasse a média do valor vendido, o maior
# valor vendido e o menor valor vendido de seus 3 vendedores/as. Pediu para que fosse algo automatizado, pois como ele está em
# fase de expansão, nos próximos meses mais 4 vendedores serão contratados e sua análise deve estar pronta para isso.
# Ele te passou a venda dos últimos 7 dias, dos/as vendedores/as atuais:
# • Maria: 800,700,1000,900,1200,600,600
# • João: 900,500,1100,1000,900,500,700
# • Manuel: 700,600,900,1200,900,700,400
# Como resultado, ele gostaria de visualizar o Nome do/a vendedor/a e a média de venda, o maior valor vendido e o
# menor valor vendido, dos últimos 7 dias.

# import pandas as pd

# Maria = pd.Series([800,700,1000,900,1200,600,600])
# Joao = pd.Series([900,500,1100,1000,900,500,700])
# Manuel = pd.Series([700,600,900,1200,900,700,400])

# # Media do valor vendidido:
# print("A média do valor vendiddo da Maria é:", Maria.mean())
# print("A média do valor vendido do João é:", Joao.mean())
# print("A média do valor vendido do Manuel é", Manuel.mean())

# #O maior  valor vendido:
# print("O maior valor vendido da Maria é:", Maria.max())
# print("O maior valor vendido do João é:", Joao.max())
# print("O maior valor vendido do Manuel é:", Manuel.max())

# #O menor valor vendido:

# print("O menor valor vendido da Maria é:", Maria.min())
# print("O menor valor vendido do João é:", Joao.min())
# print("O menor valor vendido do Manuel é:", Manuel.min())



