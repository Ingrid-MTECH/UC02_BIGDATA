import pandas as pd 

alunos = [
    ['João',18,100],
    ['Maria', 15,80],
    ['Erika',20,60],
    ['Pedro',16,10]
]

colunas = ['Nome', 'Idade', 'Média']

df_alunos = pd.DataFrame(alunos, columns = colunas, index = ['Jan', 'Fev', 'Mar','Abr'])


soma_idade = df_alunos['Idade'].sum(axis=0)
media_idade = df_alunos['Idade'].mean(axis=0)
maior_idade = df_alunos['Idade'].max(axis=0)
menor_idade = df_alunos['Idade'].min(axis=0)
maior_nome = df_alunos[df_alunos['Idade'] == maior_idade]['Nome']
menor_nome = df_alunos[df_alunos['Idade'] == menor_idade]['Nome']


soma_media = df_alunos['Média'].sum(axis=0)
soma_media = df_alunos['Média'].mean(axis=0)
maior_media = df_alunos['Média'].max(axis=0)
menor_media = df_alunos['Média'].min(axis=0)
maior_media_nome = df_alunos[df_alunos['Média'] == maior_media]['Nome']
menor_media_nome = df_alunos[df_alunos['Média'] == menor_media]['Nome']


print(f"A menor idade é de {maior_nome.values[0]}")
print(f"A menor idade é de {menor_nome.values[0]}")

print("\n -- Informações sobre as Idades dos Alunos --")
print(f"A soma das idades é de {soma_idade:.2f}")
print(f"A media das idades é de {media_idade:.2f}")
print(f"A maior idade é de {maior_idade:.2f}")
print(f"A menor idade é de {maior_nome.values[0]}")
print(f"A menor idade é de {menor_nome.values[0]}")
print(f"A menor media é de {maior_media_nome.values[0]}")
print(f"A menor media é de {menor_media_nome.values[0]}")