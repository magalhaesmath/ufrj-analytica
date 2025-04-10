# Autor: Matheus Magalhães

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("notas.csv")

# Criando histogramas para cada turma
plt.figure(figsize=(10, 6))
plt.hist(df[df["Turma"] == "Turma A"]["Nota"], bins=10, alpha=0.5, label="Turma A")
plt.hist(df[df["Turma"] == "Turma B"]["Nota"], bins=10, alpha=0.5, label="Turma B")
plt.hist(df[df["Turma"] == "Turma C"]["Nota"], bins=10, alpha=0.5, label="Turma C")

plt.xlabel("Nota Final")
plt.ylabel("Frequência")
plt.title("Distribuição das Notas Finais por Turma")
plt.legend()
plt.show()
