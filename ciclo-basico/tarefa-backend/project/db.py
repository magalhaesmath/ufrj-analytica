import csv
import sqlite3

print("Iniciando a importação de dados...")

try:
    # Conectando ao banco de dados:
    conexao = sqlite3.connect('banco_SAT.db')
    cursor = conexao.cursor()
    print("Conexão com o banco de dados estabelecida com sucesso.")
except sqlite3.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    exit()

try:
    # Criando a tabela no banco de dados:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados_SAT (
        DBN TEXT PRIMARY KEY,
        School_Name TEXT,
        Number_of_Test_Takers INTEGER,
        Critical_Reading_Mean REAL,
        Mathematics_Mean REAL,
        Writing_Mean REAL              
    )
    ''')
    print("Tabela criada/verificada com sucesso.")
except sqlite3.Error as e:
    print(f"Erro ao criar/verificar a tabela: {e}")
    exit()

try:
    # Importando os dados do CSV para a tabela:
    with open('SAT__College_Board__2010_School_Level_Results_20240506.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        cabeçalho = next(leitor_csv)  # Pulando o cabeçalho
        for linha in leitor_csv:
            cursor.execute('''
            INSERT OR IGNORE INTO dados_SAT (DBN, School_Name, Number_of_Test_Takers, Critical_Reading_Mean, Mathematics_Mean, Writing_Mean) 
            VALUES (?, ?, ?, ?, ?, ?)
            ''', linha)
        print("Dados importados com sucesso.")
except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado.")
    exit()
except csv.Error as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    exit()
except sqlite3.Error as e:
    print(f"Erro ao inserir dados no banco de dados: {e}")
    exit()

# Salvando as mudanças e fechando a conexão
try:
    conexao.commit()
    print("Mudanças salvas com sucesso.")
except sqlite3.Error as e:
    print(f"Erro ao salvar mudanças no banco de dados: {e}")
finally:
    conexao.close()
    print("Conexão com o banco de dados fechada.")

print("Importação de dados concluída.")
