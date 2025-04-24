import sqlite3
from datetime import datetime

LOCAL_DB = r'Controle_combustivel\dados\consumo.db'


def criar_banco_dados():
    # Conectar ao banco de dados (será criado se não existir)
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    
    # Criar tabela de carros
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER,
        placa TEXT UNIQUE NOT NULL,
        quilometragem_atual REAL DEFAULT 0,
        data_cadastro TEXT NOT NULL,
        observacoes TEXT
    )
    ''')

    #Nova tabela para informações de combustível
    cursor.execute('''
   CREATE TABLE IF NOT EXISTS tanques (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        carro_id INTEGER NOT NULL,
        capacidade_tanque REAL NOT NULL,              -- em litros
        tipo_combustivel TEXT NOT NULL,               -- gasolina, diesel, etanol, etc
        autonomia_media REAL,                         -- km/litro
        ultima_medicao TEXT,                          -- data da última medição
        combustivel_atual REAL DEFAULT 0,             -- quantidade teórica atual no tanque
        FOREIGN KEY (carro_id) REFERENCES carros(id)
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