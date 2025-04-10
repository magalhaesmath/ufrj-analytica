import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Importando o .csv:
df = pd.read_csv("temperatura.csv")

# Criando o gráfico de dispersão:
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["2004"], y=df["2024"], hue=df["estação"], palette="viridis", s=100)

# Adicionando linha de tendência:
sns.regplot(x=df["2004"], y=df["2024"], scatter=False, color="red", label="Linha de Tendência")

# Título e legendas:
plt.title("Relação entre Temperaturas de 2004 e 2024 por Estação")
plt.xlabel("Temperatura em 2004 (ºC)")
plt.ylabel("Temperatura em 2024 (ºC)")
plt.legend(title="Estação")
plt.grid(True)

# Exibindo o gráfico:
plt.show()