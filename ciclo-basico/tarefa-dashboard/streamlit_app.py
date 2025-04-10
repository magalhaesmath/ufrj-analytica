import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.title('*Dashboard* interativo de dados do SAT 📊')

# Subtítulo:
st.subheader('Autor: Matheus Magalhães')

# Lista de funcionalidades (páginas)
paginas = ["Página Inicial 🏛️", "*Upload* dos dados ⬆️", "Análise de Dados 🔎", "Visualização de Gráficos 📊"]

# Barra lateral para navegação
st.sidebar.title("Navegação")
selecao = st.sidebar.radio("Ir para", paginas)

# Exibir conteúdo com base na seleção
if selecao == "Página Inicial 🏛️":
    st.markdown('''
    <div style="text-align: justify">

    ## Autor: Matheus Magalhães

    ### Bem-vindo!

    Este dashboard interativo foi desenvolvido para ajudá-lo a visualizar informações relevantes sobre o SAT de maneira intuitiva e eficiente. Do lado esquerdo, você encontrará a barra de navegação que permite explorar as diversas funcionalidades do aplicativo. Aqui está um breve resumo das seções que você encontrará:

    ### Página Inicial 🏛️

    Na página inicial, você encontrará uma introdução ao dashboard e orientação sobre como começar. Para iniciar sua análise, sugerimos que você vá para a seção de *Upload* dos dados.

    ### *Upload* dos Dados ⬆️

    Nesta seção, você pode fazer o *upload* do seu arquivo no formato CSV contendo os dados do SAT. Após o *upload*, você será notificado do sucesso ou falha da operação. É aqui que seus dados começarão a ganhar vida dentro do nosso dashboard!

    ### Análise de Dados 🔎

    Na seção de Análise de Dados, você poderá visualizar uma amostra da sua tabela e aplicar filtros aos atributos de interesse, como "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean" e "Writing Mean". Com as opções de filtragem, você pode refinar os dados conforme necessário e até fazer o download do conjunto de dados filtrado.

    ### Visualização de Gráficos 📊

    Aqui, você terá acesso a ferramentas para criar gráficos que ajudam a visualizar melhor os dados. Você pode gerar histogramas e gráficos de barras baseados nos atributos selecionados. Além disso, é possível escolher se deseja visualizar a tabela original ou a tabela filtrada.
    </div>
    ''', unsafe_allow_html=True)

elif selecao == "*Upload* dos dados ⬆️":
    arquivo_csv = st.file_uploader("Escolha seu arquivo *.csv* para upload:", type="csv")

    if 'upload_realizado' not in st.session_state:
        st.session_state.upload_realizado = False

    if arquivo_csv is not None:
        try:
            df = pd.read_csv(arquivo_csv)
            st.session_state.df = df
            st.session_state.nome_arquivo = arquivo_csv.name.split(".")[0]
            st.session_state.upload_realizado = True
            st.session_state.df_filtrado = df

            # Resetando os filtros ao fazer upload de um novo arquivo
            st.session_state.filtros_selecionados = []
            st.session_state.intervalos = {}

            st.success("Upload realizado com sucesso! 😁", icon="✅")
        except Exception as e:
            st.error("Algum erro ocorreu durante o upload! 🙁", icon="❌")

    elif st.session_state.upload_realizado:
        st.success("Upload realizado com sucesso! 😁", icon="✅")

elif selecao == "Análise de Dados 🔎":
    st.header("Análise de Dados 🔎")
    if 'df' in st.session_state:
        df = st.session_state.df
        df_filtrado = st.session_state.df_filtrado

        st.write("Uma amostra da sua tabela! 😉")
        st.dataframe(df.head(10))

        filtros = ["Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]

        # Se os filtros ainda não foram armazenados, inicialize-os
        if "filtros_selecionados" not in st.session_state:
            st.session_state.filtros_selecionados = []
        if "intervalos" not in st.session_state:
            st.session_state.intervalos = {}

        # Multiselect com persistência dos filtros já selecionados:
        filtragem = st.multiselect("Selecione os atributos que deseja filtrar:", filtros, default=st.session_state.filtros_selecionados)

        # Atualiza a lista de filtros selecionados no session_state:
        st.session_state.filtros_selecionados = filtragem

        df_temp = df.copy()

        for filtro in filtragem:
            min_val = int(df[filtro].min())  # Sempre pega os valores do DataFrame original (para evitar pontos de não retorno).
            max_val = int(df[filtro].max())

            # Se o intervalo já foi escolhido antes, mantém o valor, senão, usa o mínimo e máximo do original.
            intervalo_inicial = st.session_state.intervalos.get(filtro, (min_val, max_val))

            # Slider com valores armazenados no session_state (para não limitar o slider):
            intervalo = st.select_slider(f"Selecione um intervalo para {filtro}:",
                                         options=range(min_val, max_val + 1),
                                         value=intervalo_inicial)

            # Atualiza o intervalo no session_state:
            st.session_state.intervalos[filtro] = intervalo

            # Filtragem real dos dados:
            df_temp = df_temp[(df_temp[filtro] >= intervalo[0]) & (df_temp[filtro] <= intervalo[1])]

        # Verificando se já existem filtros selecionados:
        if filtragem:
            st.session_state.df_filtrado = df_temp

        st.write(st.session_state.df_filtrado)

        # Função para converter DataFrame em .csv:
        def converte_df_csv(df):
            return df.to_csv(index=False).encode('utf-8')

        # P/ armazenar o nome do arquivo upado:
        nome_arquivo_download = f"{st.session_state.nome_arquivo}_filtrado.csv"

        # Botão de download da tabela já filtraada:
        st.download_button("Aperte para fazer *download* da tabela filtrada ⬇️",
                           converte_df_csv(st.session_state.df_filtrado),
                           nome_arquivo_download,
                           "text/csv")
    else:
        st.warning("Faça o upload dos dados na seção 'Upload dos dados'.", icon="⚠️")

elif selecao == "Visualização de Gráficos 📊":
    st.header("Visualização de Gráficos 📊")
    if 'df' in st.session_state:
        st.write("""
        ## Explore seus dados através de gráficos interativos!  

        Nesta seção, você pode criar histogramas e gráficos de barras para analisar os atributos do conjunto de dados do SAT.  

        ### Passo 1: Escolha a Tabela  
        Selecione se você deseja visualizar a tabela original ou a tabela filtrada para a geração dos gráficos.  

        ### Passo 2: Crie Histogramas  
        Escolha um atributo para criar um histograma que representa a distribuição de valores desse atributo.  

        ### Passo 3: Visualize Gráficos de Barras  
        Veja as médias dos principais atributos através de gráficos de barras.  

        Aproveite estas ferramentas para obter insights valiosos sobre seus dados!  
        """)

        df = st.session_state.df
        df_filtrado = st.session_state.df_filtrado

        # Histograma:
        filtros_histograma = ["Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]

        # Escolha da tabela que o usuário quer analisar:
        st.header("Escolha da tabela")
        escolha_tabela = st.selectbox("Escolha a tabela que quer gerar os gráficos", ["Tabela Original 📄", "Tabela Filtrada 🔍"], index=0)

        tabela = df if escolha_tabela == "Tabela Original 📄" else df_filtrado

        st.title("Histogramas 📚")
        escolha = st.selectbox("Selecione uma variável para fazer o histograma:", filtros_histograma)

        fig, ax = plt.subplots()
        tabela[escolha].hist(ax=ax)

        ax.set_title(f"Histograma de {escolha}")
        ax.set_xlabel("Valores")
        ax.set_ylabel("Frequência")

        st.pyplot(fig)

        # Gráfico de barras:
        st.title("Gráfico de Barras 📊")

        # Calculando as médias:
        medias = {
            "Number of Test Takers": tabela["Number of Test Takers"].mean(),
            "Critical Reading Mean": tabela["Critical Reading Mean"].mean(),
            "Mathematics Mean": tabela["Mathematics Mean"].mean(),
            "Writing Mean": tabela["Writing Mean"].mean(),
        }

        # Convertendo para DataFrame:
        df_medias = pd.DataFrame(list(medias.items()), columns=["Categoria", "Média"]).set_index("Categoria")

        # Exibindo o gráfico de barras:
        st.bar_chart(df_medias)

    else:
        st.warning("Faça o upload dos dados na seção 'Upload dos dados'.", icon="⚠️")
