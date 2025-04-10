# 📊 Análise Exploratória de Dados - Frotas de Ônibus

Este notebook realiza uma análise exploratória de dados (EDA) com o objetivo de investigar possíveis relações entre atributos de uma frota de ônibus, como preço, integridade, capacidade e horário de início das rotas.

## 🔍 Objetivo

Explorar o conjunto de dados de ônibus para responder perguntas como:
- Existe alguma relação entre o preço do ônibus e sua integridade ou capacidade?
- A integridade dos ônibus varia de acordo com o horário das rotas (diurno vs noturno)?
- Existem padrões relevantes ou insights nos dados que podem ser utilizados para tomada de decisão?

---

## 🧼 1. Limpeza e Tratamento de Dados

As etapas iniciais envolvem:
- Tratamento de valores ausentes
- Conversões e ajustes de colunas temporais
- Extração da hora do campo `hora_inicio` para análises posteriores

---

## 📈 2. Análises Estatísticas e Visuais

### Relações Numéricas
- **`bus_price` vs `bus_integrity`**: Sem correlação linear clara.
- **`bus_price` vs `bus_capacity`**: Também sem relação linear evidente.
- **`bus_price` vs `bus_built_date`**: Sem padrão identificável.

### Distribuição de Colunas
- Análise gráfica com histogramas para entender a distribuição de atributos como `bus_price` e `bus_integrity`.

---

## 🌗 3. Análise por Período do Dia

Os dados são segmentados em dois grupos:

- **Turno Diurno**: das 6h às 18h
- **Turno Noturno**: das 18h às 6h

### Comparação de Integridade
- Histograma da integridade dos ônibus por período do dia.
- Resultado: as distribuições são bastante semelhantes, indicando que o **turno não afeta significativamente a integridade** dos veículos.

---

## ✅ Conclusões

- As análises não encontraram relações lineares relevantes entre as principais variáveis numéricas.
- A integridade dos ônibus não é influenciada de forma significativa pelo horário de operação.

---

## 🛠️ Requisitos

- Python 3.8+
- Bibliotecas:
  - pandas
  - matplotlib
  - seaborn

Instale os pacotes necessários com:

```bash
pip install pandas matplotlib seaborn
