import sqlite3
from datetime import datetime

LOCAL_DB = r'D:\#Mega\Jeferson - Dev\02 - Linguagens\Python\Controle_combustivel\dados\consumo.db'


def criar_banco_dados():
    # Conectar ao banco de dados (será criado se não existir)
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()


    # Tabela Marcas
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS marca_modelo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT,
                modelo TEXT UNIQUE
            )
            ''')

    # Tabela combustivel
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS combustivel (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_combustivel TEXT UNIQUE
            )
            ''')

    # Tabela carro
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS veiculo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fk_marca_modelo_id INTEGER,
                fk_combustivel_id INTEGER,                
                consumo_km_litro REAL,
                tanque REAL,
                ano INTEGER,
                placa TEXT UNIQUE,
                status BOOLEAN,
                FOREIGN KEY (fk_marca_modelo_id) REFERENCES marca_modelo(id),
                FOREIGN KEY (fk_combustivel_id) REFERENCES combustivel(id)
            )
            ''')

    # Tabela motorista
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS motorista (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT UNIQUE,
                telefone TEXT,
                email TEXT,
                data_nascimento DATE,
                habilitacao_categoria TEXT,
                dt_validade_cnh DATE,
                status BOOLEAN
            )
            ''')

    # Tabela rota
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS rota (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_rota TEXT,
                origem TEXT,
                destino TEXT,
                distancia_km REAL,
                descricao TEXT
            )
            ''')

    # Tabela posto
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS posto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_posto TEXT,
                endereco TEXT,
                cidade TEXT,
                estado TEXT
            )
            ''')

    # Tabela movimentacao
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS movimentacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dt_movimento DATE,
                fk_carro_id INTEGER,
                fk_motorista_id INTEGER,
                fk_rotas_id INTEGER,
                fk_posto_id INTEGER,
                km_inicial REAL,
                km_final REAL,
                distancia_km REAL,
                abasteceu BOOLEAN,
                abast_litros REAL,
                abast_valor REAL,
                qtd_tanque REAL,
                autonomia_estimada REAL,
                dt_prev_abast DATE,
                observacao TEXT,
                FOREIGN KEY (fk_carro_id) REFERENCES carro(id),
                FOREIGN KEY (fk_motorista_id) REFERENCES motorista(id),
                FOREIGN KEY (fk_rotas_id) REFERENCES rota(id),
                FOREIGN KEY (fk_posto_id) REFERENCES posto(id)
            )
            ''')

    # Tabela historico_preco
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS historico_preco (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fk_posto_id INTEGER,
                fk_combustivel_id INTEGER,
                data_coleta DATE,
                preco_litro REAL,
                FOREIGN KEY (fk_posto_id) REFERENCES posto(id),
                FOREIGN KEY (fk_combustivel_id) REFERENCES combustivel(id)
            )
            ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    criar_banco_dados()
    print("Banco de dados criado com sucesso!")