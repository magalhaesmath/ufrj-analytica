Dashboard Interativo de Dados do SAT

Este repositório contém um dashboard interativo desenvolvido com Streamlit para a análise de dados do SAT.

📌 Funcionalidades

Upload de Dados: Permite o envio de arquivos CSV contendo os dados do SAT.

Análise de Dados: Visualização tabular dos dados, com opção de filtragem de atributos.

Visualização de Gráficos: Gera histogramas e gráficos de barras baseados nos atributos selecionados.

Download de Dados Filtrados: Permite baixar a tabela filtrada em formato CSV.

🚀 Como Executar

Clone este repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Instale as dependências necessárias:

pip install -r requirements.txt

Execute o aplicativo Streamlit:

streamlit run app.py

📊 Estrutura do Dashboard

1️⃣ Página Inicial 🏛️

Introdução ao dashboard e instruções de uso.

2️⃣ Upload de Dados ⬆️

Permite ao usuário carregar um arquivo CSV contendo os dados do SAT.

Exibe mensagens de sucesso ou erro ao processar o arquivo.

3️⃣ Análise de Dados 🔎

Mostra uma amostra da tabela carregada.

Permite filtrar os atributos: "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean" e "Writing Mean".

Oferece a opção de download do conjunto de dados filtrado.

4️⃣ Visualização de Gráficos 📊

Gera histogramas baseados em atributos selecionados.

Apresenta um gráfico de barras com as médias dos principais atributos.

🛠️ Tecnologias Utilizadas

Python

Streamlit

Pandas

Matplotlib