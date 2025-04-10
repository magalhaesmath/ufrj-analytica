# Autor: Matheus Magalhães

import pandas as pd 

# Importando os DataFrames:
bus_data = pd.read_csv("bus_data.csv", sep="|")
company_data = pd.read_csv("company_data.csv", sep=";")

# Preenchendo valores nulos em 'driver_name' e 'bus_route':
bus_data.fillna({'driver_name': "motorista não atribuído", 'bus_route': "rota não atribuída"}, inplace=True)

# Padronizando datas, ignorando erros:
bus_data['bus_built_date'] = pd.to_datetime(bus_data['bus_built_date'], errors='coerce')

# Fazendo o merge com 'bus_line_id' e 'id':
merge = pd.merge(bus_data, company_data, left_on='bus_line_id', right_on='id', how='inner')

# Convertendo 'bus_integrity' para numérico e tratando valores inválidos:
merge['bus_integrity'] = pd.to_numeric(merge['bus_integrity'], errors='coerce')
merge['bus_integrity'] = merge['bus_integrity'].fillna(merge['bus_integrity'].mean())  # <- Corrigido

# Renomeando a coluna 'bus_price(R$)' para evitar problemas:
merge.rename(columns={'bus_price(R$)': 'bus_price'}, inplace=True)

# Criando um DataFrame com a média da integridade por rota:
media_integridade = merge.groupby('bus_route')['bus_integrity'].mean().reset_index()

print(media_integridade.head())
