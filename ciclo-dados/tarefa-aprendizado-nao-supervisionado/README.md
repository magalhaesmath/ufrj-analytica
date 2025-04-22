# Autor: Matheus Magalhães

# 🧠 Análise de Segmentação de Clientes Bancários com PCA e K-Means

Este projeto aplica técnicas de **redução de dimensionalidade** e **aprendizado não supervisionado** para analisar e segmentar clientes de um banco com base em seu comportamento e perfil financeiro. O objetivo é fornecer **insights estratégicos** que podem ser utilizados para melhorar campanhas de marketing, atendimento ao cliente e alocação de recursos nos canais de comunicação.

---

## 📊 Técnicas Utilizadas

- **Análise Exploratória de Dados (EDA)** com `pandas`, `matplotlib` e `seaborn`
- **Redução de Dimensionalidade** com **PCA (Principal Component Analysis)**
- **Clusterização** com **K-Means**
- **Elbow Method** para definição do número ótimo de clusters
- Visualizações 2D dos clusters reduzidos por PCA

---

## 📁 Estrutura do Projeto

📦 tarefa-aprendizado-nao-supervisionado 
  ├── 📊 credit_card_customer_data.csv # Dataset com informações dos clientes.
  ├── 📈 aprendizado-nao-supervisionado.ipynb # Notebook com EDA, PCA, K-Means e visualizações. 
  ├── 📃 README.md # Documentação do projeto.
  ├── 📊 perfil dos clusters.png # Perfil dos clusters formados.
  └── 📊 clusterização dos clientes.png # Gráfico com visualização dos clusters (exemplo).

---

## 🧪 Variáveis Analisadas

- `Avg_Credit_Limit` – Média de limite de crédito
- `Total_Credit_Cards` – Total de cartões de crédito
- `Total_visits_bank` – Visitas ao banco (presencial)
- `Total_visits_online` – Acessos online
- `Total_calls_made` – Chamadas telefônicas

---

## 🎯 Principais Resultados

- **3 clusters principais** com base no limite de crédito: baixo, médio e alto.
- **Correlação direta** entre limite de crédito e número de cartões.
- Cada cluster tem **um canal preferencial de comunicação**:
  - Baixo crédito → telefone
  - Médio crédito → presencial
  - Alto crédito → online

---

## 💡 Aplicações Estratégicas

- Foco em **campanhas de marketing personalizadas**
- **Otimização de recursos** nos canais de atendimento
- Alinhamento do atendimento com os **interesses e expectativas** de cada grupo de clientes

---