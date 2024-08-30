import sqlite3

class Database:
    def __init__(self, db_name="banco_avancado.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            rg TEXT NOT NULL UNIQUE,
            cpf TEXT NOT NULL UNIQUE,
            data_nascimento TEXT NOT NULL,
            localidade_nascimento TEXT NOT NULL
        )
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def insert_client(self, nome, rg, cpf, data_nascimento, localidade_nascimento):
        query = '''
        INSERT INTO clientes (nome, rg, cpf, data_nascimento, localidade_nascimento)
        VALUES (?, ?, ?, ?, ?)
        '''
        self.cursor.execute(query, (nome, rg, cpf, data_nascimento, localidade_nascimento))
        self.connection.commit()

    def fetch_clients(self):
        query = "SELECT * FROM clientes"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()
