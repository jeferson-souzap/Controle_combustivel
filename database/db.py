import sqlite3
from datetime import datetime

LOCAL_DB = r'D:\#Mega\Jeferson - Dev\02 - Linguagens\Python\Controle_combustivel\dados\consumo.db'


def criar_banco_dados():
    # Conectar ao banco de dados (será criado se não existir)
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    
    # Criar tabela de carros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_cadastro TEXT NOT NULL,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        nome_completo TEXT NOT NULL,
        ano INTEGER DEFAULT 2000,
        placa TEXT UNIQUE NOT NULL,
        total_tanque REAL DEFAULT 0,
        consumo_litros REAL DEFAULT 0,
        autonomia REAL DEFAULT 0,                     -- km/litro
        tipo_combustivel TEXT NOT NULL,               -- gasolina, diesel, etanol, etc        
        observacoes TEXT
    )
    ''')

# Criar tabela de carros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS combustivel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor REAL NOT NULL,
        posto_referencia TEXT
    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS abastecimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        carro_id INTEGER NOT NULL,
        data TEXT NOT NULL,
        valor REAL NOT NULL,                  -- Abastecimento (R$)
        litros REAL NOT NULL,                 -- Abastecimento (Litros)
        preco_litro REAL,                     -- Calculado: valor/litros
        quilometragem REAL NOT NULL,          -- Quilometragem no momento
        distancia REAL,                      -- Distancia (km)
        consumo REAL,                        -- Consumo (L)
        litros_tanque_apos REAL,            -- Litros no Tanque (aprox)
        duracao_dias INTEGER,               -- Duração (Dias)
        ajuste BOOLEAN DEFAULT FALSE,       -- Ajuste
        status TEXT,                       -- Status
        observacao TEXT,                    -- Observação
        FOREIGN KEY (carro_id) REFERENCES carros(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_banco_dados()
    print("Banco de dados criado com sucesso!")