import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        rg TEXT,
        cpf TEXT,
        data_nascimento TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        saldo REAL DEFAULT 0.0,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    ''')
    
    conn.commit()
    conn.close()

def adicionar_cliente(nome, rg, cpf, data_nascimento):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO clientes (nome, rg, cpf, data_nascimento)
    VALUES (?, ?, ?, ?)
    ''', (nome, rg, cpf, data_nascimento))

    conn.commit()
    conn.close()

def obter_cliente_por_cpf(cpf):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT id FROM clientes WHERE cpf = ?
    ''', (cpf,))
    
    cliente_id = cursor.fetchone()
    conn.close()
    
    return cliente_id[0] if cliente_id else None

def obter_saldo(cliente_id):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT saldo FROM contas WHERE cliente_id = ?
    ''', (cliente_id,))
    
    saldo = cursor.fetchone()[0]
    conn.close()
    
    return saldo

def atualizar_saldo(cliente_id, novo_saldo):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE contas SET saldo = ? WHERE cliente_id = ?
    ''', (novo_saldo, cliente_id))

    conn.commit()
    conn.close()
