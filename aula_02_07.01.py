import pandas as pd
import numpy as np  

print("--- OBTENDO DADOS ---")

endereco_dados = 'BASES/Financeira.csv'

df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

print(df_financeira.head())

array_financeira_renda = np.array(df_financeira['Renda'])
array_financeira_vlr_emprestado = np.array(df_financeira['Vlr_emprestado'])
media_renda = np.mean(array_financeira_renda) 
media_Vlr_emprestado = np.mean(array_financeira_vlr_emprestado)

mediana_renda = np.median(array_financeira_renda) 
mediana_Vlr_emprestado = np.median(array_financeira_vlr_emprestado)

distancia_renda =abs((media_renda - media_renda) / mediana_renda) * 100
distancia_Vlr_emprestado =abs((media_Vlr_emprestado - mediana_Vlr_emprestado) / mediana_Vlr_emprestado) * 100

maior_renda = np.max(array_financeira_renda) 
maior_Vlr_emprestado = np.max(array_financeira_vlr_emprestado)

menor_renda = np.min(array_financeira_renda) 
menor_Vlr_emprestado = np.min(array_financeira_vlr_emprestado)

amplitude_renda = maior_renda - menor_renda
amplitude_Vlr_emprestado = maior_Vlr_emprestado - menor_Vlr_emprestado

print("\n--- OBTENDO INFORMAÇÕES SOBRE RENDA E EMPRÉSTIMOS ---")
print(f"A média das rendas dos clientes é R$ {media_renda:.2f}")
print(f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}")
print(f"A média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}")
print(f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}")
print(f"A distância da média da renda é de: {distancia_renda:.2f} % ")
print(f"A distância do renda do valor emprestado é de:{distancia_Vlr_emprestado:.2f} %")
print(f"A maior renda é de R$ {maior_renda:.2f}")
print(f"O maior valor emprestado é de R$ {maior_Vlr_emprestado:.2f}")
print(f"A menor renda é de:{menor_renda:.2f}")
print(f"O menor valor emprestado é de R$:{menor_Vlr_emprestado:.2f}")
print(f"A amplitude da renda é de:{amplitude_renda:.2f}")
print(f"A amplitude do valor emprestado é de:{amplitude_Vlr_emprestado:.2f}")
