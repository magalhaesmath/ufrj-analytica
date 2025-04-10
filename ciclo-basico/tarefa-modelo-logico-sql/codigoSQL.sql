-- Criando o banco de dados
CREATE DATABASE Aeroporto;
USE Aeroporto;

-- Criando tabela TipoAeronave
CREATE TABLE TipoAeronave (
    Num_Modelo INT PRIMARY KEY,
    Capacidade INT NOT NULL,
    Peso FLOAT NOT NULL
);

-- Criando tabela Hangar
CREATE TABLE Hangar (
    Num_ID INT PRIMARY KEY,
    Capacidade INT NOT NULL,
    Local VARCHAR(100) NOT NULL
);

-- Criando tabela Pessoa
CREATE TABLE Pessoa (
    CPF VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Data_Nascimento DATE NOT NULL,
    Telefone VARCHAR(15)
);

-- Criando tabela Piloto
CREATE TABLE Piloto (
    CPF VARCHAR(11),
    Num_Licenca VARCHAR(20),
    PRIMARY KEY (CPF, Num_Licenca),
    FOREIGN KEY (CPF) REFERENCES Pessoa(CPF)
);

-- Criando tabela Funcionário
CREATE TABLE Funcionario (
    CPF VARCHAR(11) PRIMARY KEY,
    Salario DECIMAL(10, 2) NOT NULL,
    Turno VARCHAR(20) NOT NULL,
    FOREIGN KEY (CPF) REFERENCES Pessoa(CPF)
);

-- Criando tabela Proprietário
CREATE TABLE Proprietario (
    CPF VARCHAR(11) PRIMARY KEY,
    Endereco VARCHAR(255) NOT NULL,
    FOREIGN KEY (CPF) REFERENCES Pessoa(CPF)
);

-- Criando tabela Aeronave
CREATE TABLE Aeronave (
    Num_Registro INT PRIMARY KEY,
    Num_Modelo INT NOT NULL,
    CPF_Proprietario VARCHAR(11),
    Num_ID_Hangar INT,
    FOREIGN KEY (Num_Modelo) REFERENCES TipoAeronave(Num_Modelo),
    FOREIGN KEY (CPF_Proprietario) REFERENCES Proprietario(CPF),
    FOREIGN KEY (Num_ID_Hangar) REFERENCES Hangar(Num_ID)
);

-- Criando tabela Manutencao
CREATE TABLE Manutencao (
    Data DATE,
    Num_Registro INT,
    Num_Horas INT NOT NULL,
    Tipo VARCHAR(50) NOT NULL,
    PRIMARY KEY (Data, Num_Registro),
    FOREIGN KEY (Num_Registro) REFERENCES Aeronave(Num_Registro)
);

-- Criando tabela Autorizado
CREATE TABLE Autorizado (
    CPF VARCHAR(11),
    Num_Licenca VARCHAR(20),
    Num_Modelo INT,
    PRIMARY KEY (CPF, Num_Licenca, Num_Modelo),
    FOREIGN KEY (CPF, Num_Licenca) REFERENCES Piloto(CPF, Num_Licenca),
    FOREIGN KEY (Num_Modelo) REFERENCES TipoAeronave(Num_Modelo)
);

-- Criando tabela Faz
CREATE TABLE Faz (
    Num_Registro INT,
    Data DATE,
    CPF VARCHAR(11),
    PRIMARY KEY (Num_Registro, Data, CPF),
    FOREIGN KEY (Num_Registro, Data) REFERENCES Manutencao(Num_Registro, Data),
    FOREIGN KEY (CPF) REFERENCES Funcionario(CPF)
);

-- Inserindo dados na tabela TipoAeronave
INSERT INTO TipoAeronave (Num_Modelo, Capacidade, Peso) VALUES
(101, 180, 75000),
(102, 200, 85000),
(103, 120, 60000);

-- Inserindo dados na tabela Hangar
INSERT INTO Hangar (Num_ID, Capacidade, Local) VALUES
(1, 50, 'Hangar A'),
(2, 60, 'Hangar B'),
(3, 70, 'Hangar C');

-- Inserindo dados na tabela Pessoa
INSERT INTO Pessoa (CPF, Nome, Data_Nascimento, Telefone) VALUES
('12345678901', 'Carlos Silva', '1985-02-15', '(11) 98765-4321'),
('98765432100', 'Maria Oliveira', '1990-06-20', '(21) 91234-5678'),
('11122233344', 'João Santos', '1980-11-10', '(31) 99876-5432');

-- Inserindo dados na tabela Piloto
INSERT INTO Piloto (CPF, Num_Licenca) VALUES
('12345678901', '12345'),
('98765432100', '98765');

-- Inserindo dados na tabela Funcionário
INSERT INTO Funcionario (CPF, Salario, Turno) VALUES
('11122233344', 3500.00, 'Diurno'),
('12345678901', 4000.00, 'Noturno');

-- Inserindo dados na tabela Proprietário
INSERT INTO Proprietario (CPF, Endereco) VALUES
('98765432100', 'Rua das Flores, 123, São Paulo'),
('11122233344', 'Avenida Central, 456, Belo Horizonte');

-- Inserindo dados na tabela Aeronave (alterado para Num_Registro 1, 2, 3)
INSERT INTO Aeronave (Num_Registro, Num_Modelo, CPF_Proprietario, Num_ID_Hangar) VALUES
(1, 101, '98765432100', 1),
(2, 102, '11122233344', 2),
(3, 103, '98765432100', 3);

-- Inserindo dados na tabela Manutencao
INSERT INTO Manutencao (Data, Num_Registro, Num_Horas, Tipo) VALUES
('2025-01-10', 1, 50, 'Revisão Geral'),
('2025-01-12', 2, 30, 'Troca de Peças'),
('2025-01-15', 3, 40, 'Inspeção de Motores');

-- Inserindo dados na tabela Autorizado
INSERT INTO Autorizado (CPF, Num_Licenca, Num_Modelo) VALUES
('12345678901', '12345', 101),
('98765432100', '98765', 102);

-- Inserirndo dados na tabela Faz
INSERT INTO Faz (Num_Registro, Data, CPF) VALUES
(1, '2025-01-10', '11122233344'),
(2, '2025-01-12', '12345678901'),
(3, '2025-01-15', '11122233344');

-- Inserindo dados na tabela TipoAeronave
INSERT INTO TipoAeronave (Num_Modelo, Capacidade, Peso) VALUES
(201, 250, 100000),
(202, 300, 120000);

-- Inserindo dados na tabela Hangar
INSERT INTO Hangar (Num_ID, Capacidade, Local) VALUES
(4, 80, 'Hangar D'),
(5, 90, 'Hangar E');

-- Inserindo dados na tabela Pessoa
INSERT INTO Pessoa (CPF, Nome, Data_Nascimento, Telefone) VALUES
('22233344455', 'Ana Paula', '2000-05-06', '(41) 98765-4321'),
('33344455566', 'Pedro Alves', '2000-05-06', '(31) 91234-5678');

-- Inserindo dados na tabela Piloto
INSERT INTO Piloto (CPF, Num_Licenca) VALUES
('22233344455', '55555'),
('33344455566', '66666');

-- Inserindo dados na tabela Aeronave
INSERT INTO Aeronave (Num_Registro, Num_Modelo, CPF_Proprietario, Num_ID_Hangar) VALUES
(4, 201, '98765432100', 1),
(5, 202, '11122233344', 1);

-- Consulta para retornar a aeronave com Num_Registro = 1
SELECT * 
FROM Aeronave
WHERE Num_Registro = 1;

-- Consulta para retornar as aeronaves armazenadas no Hangar com ID = 1
SELECT * 
FROM Aeronave
WHERE Num_ID_Hangar = 1;

-- Consulta para retornar os pilotos nascidos em 2000-05-06
SELECT P.*
FROM Pessoa P
INNER JOIN Piloto PL ON P.CPF = PL.CPF
WHERE P.Data_Nascimento = '2000-05-06';
