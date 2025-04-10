# Autor: Matheus Magalhães

import pandas as pd
import matplotlib.pyplot as plt

# Importando o .csv e definindo o DataFrame:
df = pd.read_csv("vendas.csv")

# Calculando a média global de vendas ao longo dos meses:
df["Média Global"] = df[["Produto A", "Produto B", "Produto C"]].mean(axis=1)

# Criando o gráfico de linhas com os três produtos e a média:
plt.plot(df["Mês"], df["Produto A"], label="Produto A")
plt.plot(df["Mês"], df["Produto B"], label="Produto B")
plt.plot(df["Mês"], df["Produto C"], label="Produto C")
plt.plot(df["Mês"], df["Média Global"], label="Média Global", linestyle="dashed", color="black")  # Linha pontilhada para destaque

# Definindo título e legendas:
plt.title("Vendas dos produtos ao longo dos meses")
plt.xlabel("Meses")
plt.ylabel("Vendas")

# Adicionando legenda para identificar cada linha
plt.legend()

# Exibindo o gráfico
plt.show()
