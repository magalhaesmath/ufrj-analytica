# Arquivo com as operações do CRUD e a aplicação Web.

from flask import Flask, request, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

def conexao_db():
    conexao = sqlite3.connect('banco_SAT.db')
    conexao.row_factory = sqlite3.Row
    return conexao

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criacao', methods=['GET', 'POST'])
def criacao():
    if request.method == 'POST':
        dbn = request.form['DBN']
        school_name = request.form['School_Name']
        number_of_test_takers = request.form['Number_of_Test_Takers']
        critical_reading_mean = request.form['Critical_Reading_Mean']
        mathematics_mean = request.form['Mathematics_Mean']
        writing_mean = request.form['Writing_Mean']

        try:
            conn = conexao_db() # Estabelece a conexão com o bd.
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO dados_SAT (DBN, School_Name, Number_of_Test_Takers, Critical_Reading_Mean, Mathematics_Mean, Writing_Mean)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (dbn, school_name, number_of_test_takers, critical_reading_mean, mathematics_mean, writing_mean))
            conn.commit()
            conn.close()
            return render_template('mensagem.html', mensagem="Entrada adicionada com sucesso!")
        except sqlite3.Error as e:
            return render_template('mensagem.html', mensagem=f"Ocorreu um erro: {e}")
    return render_template('criar.html')   

@app.route('/leitura', methods=['GET'])
def leitura():
    conexao = conexao_db()  # Estabelece conexão com meu banco de dados.
    df = pd.read_sql_query('SELECT * FROM dados_SAT', conexao)  # Converte o resultado da consulta em um dataframe Pandas.
    conexao.close()  # Fecha a conexão.
    tabela_html = df.head().to_html()  # Converte e retorna o dataframe em uma tabela HTML.
    return render_template('leitura.html', tabela_html=tabela_html)

@app.route('/atualizacao', methods=['GET', 'POST'])
def atualizacao():
    if request.method == 'POST' and 'buscar' in request.form:
        dbn = request.form['DBN']
        print(f"DBN recebido para busca: {dbn}")  # Adicionando print para verificar o DBN recebido
        conexao = conexao_db()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM dados_SAT WHERE DBN = ?', (dbn,))
        escola = cursor.fetchone()
        conexao.close()

        if escola:
            print(f"Escola encontrada: {escola}")  # Adicionando print para verificar os dados da escola encontrados
            return render_template('atualizar.html', escola=escola)
        else:
            print("Escola não encontrada.")  # Adicionando print para verificar quando a escola não é encontrada
            return render_template('mensagem.html', mensagem="Escola não encontrada na base de dados.")
    
    if request.method == 'POST' and 'atualizar' in request.form:
        dbn = request.form['DBN']
        nome_escola = request.form['School_Name']
        numero_de_estudantes = request.form['Number_of_Test_Takers']
        media_leitura_critica = request.form['Critical_Reading_Mean']
        media_matematica = request.form['Mathematics_Mean']
        media_escrita = request.form['Writing_Mean']

        try:
            conexao = conexao_db()
            cursor = conexao.cursor()
            cursor.execute('''
                UPDATE dados_SAT
                SET School_Name = ?, Number_of_Test_Takers = ?, Critical_Reading_Mean = ?, Mathematics_Mean = ?, Writing_Mean = ?
                WHERE DBN = ?
            ''', (nome_escola, numero_de_estudantes, media_leitura_critica, media_matematica, media_escrita, dbn))
            conexao.commit()  # Salva as mudanças.
            conexao.close()  # Fecha a conexão com o banco de dados.
            print("Atualização realizada com sucesso.")  # Adicionando print para confirmar a atualização
            return render_template('mensagem.html', mensagem="Entrada atualizada com sucesso!")  # Mensagem de sucesso na atualização dos dados.
        except sqlite3.Error as e:
            print(f"Erro ao atualizar os dados: {e}")  # Adicionando print para verificar erros durante a atualização
            return render_template('mensagem.html', mensagem=f"Ocorreu um erro: {e}")  # Mensagem de erro durante a inserção dos dados atualizados.

    return render_template('busca.html')


@app.route('/excluir', methods=['GET', 'POST'])
def excluir():
    if request.method == 'POST' and 'buscar' in request.form:
        dbn = request.form['DBN']
        print(f"DBN recebido para busca: {dbn}")  # Adicionando print para verificar o DBN recebido
        conexao = conexao_db()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM dados_SAT WHERE DBN = ?', (dbn,))
        escola = cursor.fetchone()
        conexao.close()

        if escola:
            print(f"Escola encontrada: {escola}")  # Adicionando print para verificar os dados da escola encontrados
            df = pd.DataFrame([escola], columns=escola.keys())
            tabela_html = df.to_html(index=False)
            return render_template('confirmar_exclusao.html', tabela_html=tabela_html, dbn=dbn)
        else:
            print("Escola não encontrada.")  # Adicionando print para verificar quando a escola não é encontrada
            return render_template('mensagem.html', mensagem='Escola não encontrada na base de dados.')

    if request.method == 'POST' and 'confirmo' in request.form:
        dbn = request.form['DBN']
        print(f"DBN recebido para exclusão: {dbn}")  # Adicionando print para verificar o DBN recebido para exclusão

        try:
            conexao = conexao_db()
            cursor = conexao.cursor()
            cursor.execute('DELETE FROM dados_SAT WHERE DBN = ?', (dbn,))
            conexao.commit()
            conexao.close()
            print("Escola excluída com sucesso.")  # Adicionando print para confirmar a exclusão
            return render_template('mensagem.html', mensagem="Escola excluída com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao excluir a escola: {e}")  # Adicionando print para verificar erros durante a exclusão
            return render_template('mensagem.html', mensagem=f'Ocorreu um erro: {e}')

    return render_template('excluir.html')

if __name__ == "__main__":
    app.run(debug=True)