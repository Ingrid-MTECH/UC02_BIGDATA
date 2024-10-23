import pandas as pd

funcionarios_csv = 'BASES/funcionarios.csv'

df_funcionarios = pd.read_csv(funcionarios_csv,sep=',',encoding='ISO-8859-1')

print(df_funcionarios)

print('\n---- A média salarial --- ')

media_salario = df_funcionarios['Salário'].mean(axis=0)
print(f"A média salarial é de:",media_salario)

print('\n---- Qual a média de idade --- ')

media_idade = df_funcionarios['Idade'].mean(axis=0)
print(f"A média de idade é de:",media_idade)

print('\n---- Qual o maior e menor tempo de casa, bem como a diferença entre eles? --- ')

menor = df_funcionarios['Idade'].min(axis=0)
print(f"A menor idade é de:",menor)

maior = df_funcionarios['Idade'].max(axis=0)
print(f"A maior idade é de:",maior)

print("A diferença de idade entre eles é de:", maior - menor, "anos")

total = df_funcionarios['Nome'].count()
print("O total de funcionários é de:", total)


print('\n---- Qual o nome do funcionário com maior salário --- ')
maior = df_funcionarios['Salário'].max(axis=0)
maior_salario = df_funcionarios[df_funcionarios['Salário'] == maior]['Nome']
print("O nome do funcionário com maior salário é:", maior_salario.to_string(index=(False)))

menor = df_funcionarios['Salário'].min(axis=0)
menor_salario = df_funcionarios[df_funcionarios['Salário'] == menor]['Nome']
print("O nome do funcionário com o menor salário é: ", menor_salario.to_string(index=(False)))

print('\n---- Qual o nome do funcionário com maior tempo de casa? --- ')

maior_tempo = df_funcionarios['Tempo'].max(axis=0)
funcionario_maior = df_funcionarios[df_funcionarios['Tempo']== maior_tempo]['Nome']
print("O funcionário como maior tempo de casa é:", funcionario_maior.to_string(index=(False)))