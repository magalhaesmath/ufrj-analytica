# 🚗 Previsão de Preços de Carros Usados com Regressão Linear

Este projeto tem como objetivo prever o **preço de venda de carros usados** com base em dados reais do marketplace CarDekho. Foram aplicadas técnicas de regressão linear tradicional e polinomial, com diferentes estratégias de pré-processamento, limpeza, normalização e validação, avaliando seus impactos sobre o desempenho final do modelo.

---

## 📌 Objetivo

Desenvolver um modelo preditivo de **regressão supervisionada** que estime com boa acurácia o preço de carros usados utilizando variáveis como quilometragem, idade do carro, tipo de combustível, número de donos anteriores, marca, modelo e outros.

---

## 📊 Conjunto de Dados

- Total de registros: ~4.000
- Variáveis disponíveis: `year`, `km_driven`, `fuel`, `seller_type`, `transmission`, `owner`, `car_brand`, `car_model`, `selling_price`

---

## ⚙️ Técnicas Utilizadas

### 📌 Pré-processamento
- Remoção de duplicatas
- Padronização de texto (`str.strip().lower().capitalize()`)
- Extração de marca e modelo da coluna `name`
- Redução de cardinalidade para `car_model`
- Mapeamento ordinal da coluna `owner`
- Criação da variável **`car_age` = 2025 - year**
- Detecção e remoção de outliers via **técnica de IQR**

### 📌 Transformações
- One-Hot Encoding para variáveis categóricas
- Teste com múltiplos scalers:
  - `StandardScaler` (padrão)
  - `RobustScaler`
- Criação de pipelines com `Pipeline` e `ColumnTransformer`

### 📌 Regressão
- `LinearRegression` básica
- `PolynomialFeatures + LinearRegression` para teste de modelos polinomiais
- K-Fold Cross Validation com 5 folds

---

## 📈 Resultados Finais

### 🔹 Regressão Linear com `StandardScaler` e tratamento de outliers:
- **MSE médio**: `23.702.409.432`
- **RMSE médio**: `153.931`
- **Preço médio real (`selling_price`)**: `~393.000`
- **Erro percentual médio aproximado**: `~41%`

### 🔹 Regressão Polinomial (grau 2):
- **RMSE médio**: `143.884`
- **Leve melhora**, porém tendência a overfitting detectada para graus > 2

---

## 🔍 Análises Complementares

- **Distribuições analisadas** com histogramas e curvas de densidade
- **Verificação de normalidade** dos atributos numéricos
- Análise de **correlação** entre variáveis
- Análise de desempenho de modelos com e sem variáveis como `year`

---

## 🧪 Testes Manuais

# Teste:

```python

novo_carro = pd.DataFrame([{
    'year': 2016,
    'km_driven': 11958,
    'fuel': 'Petrol',
    'seller_type': 'Dealer',
    'transmission': 'Manual',
    'owner': 1,
    'car_brand': 'Honda',
    'car_model': 'Amaze S i-VTEC'
}])

preco_previsto = pipeline.predict(novo_carro)
print(f"Preço previsto: R$ {preco_previsto[0]:,.2f}")


