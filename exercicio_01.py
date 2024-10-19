import pandas as pd

dados_vendedores = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana'],
    'Sexo': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Idade': [28, 34, 45, 30, 40, 29, 38, 31, 27, 33],
    'Qtd_Vendas': [120, 150, 110, 95, 130, 140, 105, 125, 100, 135]
}

df_vendedores = pd.DataFrame(dados_vendedores)
print(df_vendedores)
print("\n -- Informações total de vendas -- " )

total_vendas = df_vendedores['Qtd_Vendas'].sum(axis=0)
print(f"O total de vendas é de R${total_vendas:.2f}")

print("\n -- Informações média de vendas -- " )

media_vendas = df_vendedores['Qtd_Vendas'].mean(axis=0)
print(f"A média de vendas é de R${media_vendas:.2f}")

print("\n -- Informações idade vendedores -- " )

media_idades = df_vendedores['Idade'].mean(axis=0)
print(f"A média das idades é de:{media_idades:.2f}")

maior_idade = df_vendedores['Idade'].max(axis=0)
print(f"A maior idade é de:{maior_idade:.0f}")

menor_idade = df_vendedores['Idade'].min(axis=0)
print(f"A menor idade é de:{menor_idade:.0f}")

print("\n -- Vendedor com maior venda -- " )

maior_venda = df_vendedores['Qtd_Vendas'].max(axis=0)

nome_maior = df_vendedores[df_vendedores['Qtd_Vendas'] == maior_venda ] ['Nome']
print("O vendedor com maior venda é o:",nome_maior)

print("\n -- Vendedor com menor quantidade de venda -- " )

menor_venda = df_vendedores['Qtd_Vendas'].min(axis=0)

nome_menor = df_vendedores[df_vendedores['Qtd_Vendas'] == menor_venda]['Nome']
print("O vendedor com a menor venda é o:",nome_menor)


print("\n -- A quantidade de vendas por sexo  -- " )
sexo_f = df_vendedores[df_vendedores['Sexo'] == 'F']['Qtd_Vendas'].sum(axis=0)

print("A quantidade de vendas do sexo feminino é R$",sexo_f)

sexo_m = df_vendedores[df_vendedores['Sexo'] == "M"]['Qtd_Vendas'].sum(axis=0)
print("A quantidade de vendas do sexo masculino é R$",sexo_m)
