import pandas as pd

dados_municipios = {
    'Município': ['Rio de Janeiro', 'Niterói', 'São Gonçalo', 'Duque de Caxias', 'Nova Iguaçu', 'Belford Roxo',
                  'São João de Meriti', 'Petrópolis', 'Volta Redonda', 'Campos dos Goytacazes'],
    'Habitantes': [6775561, 515317, 1091737, 924624, 821128, 513118, 472906, 306678, 273988, 507548],
    'Roubos a Pedestres': [35000, 2500, 15000, 12000, 10000, 9000, 8500, 1000, 2000, 4000]
}

df = pd.DataFrame(dados_municipios)
print(df)
print("\n-- Total e a média de roubos no Rio de janeiro: -- ")
print("\n")
total_roubos = df[df['Município'] == 'Rio de Janeiro']['Roubos a Pedestres'].sum(axis=0)
print("O total de roubos no município do Rio de janeiro é de:",total_roubos)

media_roubos = df[df['Município'] == 'Rio de janeiro']['Roubos a Pedestres'].mean(axis=0)
print("A média de roubos no município do Rio de janeiro é de:",media_roubos)

print("\n-- Total e a média da população no Rio de janeiro: -- ")
print("\n")
populacao_total = df[df['Município'] == 'Rio de Janeiro']['Habitantes'].sum(axis=0)
print("O total da população domunicípio do Rio de janeiro é de:",populacao_total)

populacao_media = df[df['Município'] == 'Rio de Janeiro']['Habitantes'].mean(axis=0)
print("A média da população no município do Rio de janeiro é de:",populacao_media)

print("\n-- Menor e maior população no Rio de janeiro: -- ")
print("\n")
populacao_maior = df['Habitantes'].max(axis=0)
print(populacao_maior)

