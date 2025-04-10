# Matheus Magalhães Nascimento Silva

## Projeto CRUD com Flask
Este projeto é uma aplicação CRUD (Create, Read, Update, Delete) desenvolvida com o framework Flask em Python. O objetivo é gerenciar entradas de uma base de dados contendo informações sobre escolas, como DBN, nome da escola, número de estudantes, médias de leitura crítica, matemática e escrita.

## Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:

project/<br>
├── app.py<br>
├── db.py<br>
├── templates/<br>
│   ├── index.html<br>
│   ├── criar.html<br>
│   ├── busca.html<br>
│   ├── atualizar.html<br>
│   ├── excluir.html<br>
│   ├── confirmar_exclusao.html<br>
│   └── mensagem.html<br>
├── banco_SAT.db<br>
├── SAT__College_Board__2010_School_Level_Results_20240506<br>

## Dependências
Para rodar o projeto, você precisa das seguintes dependências:

- Flask

- pandas

- sqlite3

## Funcionalidades
1. **Página Inicial**
- A página inicial (index.html) contém botões que direcionam para as funcionalidades de criação, leitura, atualização e exclusão de entradas.

2. **Criação de Entrada**
- Rota: /criacao

- Permite adicionar uma nova entrada no banco de dados preenchendo os campos do formulário.

3. **Leitura de Entradas**
- Rota: /leitura

- Exibe as primeiras cinco entradas do banco de dados em uma tabela HTML.

4. **Atualização de Entrada**
- Rota: /atualizacao

- Permite buscar uma entrada pelo DBN e, após encontrar, atualizar os dados dessa entrada. A página de atualização também possui um botão para retornar à página inicial.

5. **Exclusão de Entrada**
- Rota: /excluir

- Permite buscar uma entrada pelo DBN e, após encontrar, confirmar a exclusão da entrada exibindo uma tabela HTML com os dados da entrada. A página de confirmação de exclusão também possui um botão para retornar à página inicial.