import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
import streamlit as st
import sqlite3
from database.db import LOCAL_DB


# --------------------------------------------------------------------------------------
# CADASTRO DE MARCAS

def Salvar_marca_modelo(marca, modelo):
    try:
        with sqlite3.connect(LOCAL_DB) as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO marca_modelo (marca, modelo) VALUES(?,?)", (marca, modelo))

            return f"Marca '{marca}' salva com sucesso!"

    except sqlite3.IntegrityError as e:
        # Este erro específico ocorre se você tentar inserir uma marca que já existe,
        # devido à restrição UNIQUE na tabela.
        return f"Erro: A marca '{marca}' já existe no banco de dados."
    except sqlite3.Error as e:
        # Captura qualquer outro erro do SQLite.
        return f"Erro ao salvar a marca: {e}"

def Remover_marca(id_marca):
    try:
        with sqlite3.connect(LOCAL_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM marca_modelo WHERE id = ?", (id_marca,))
            conn.commit()
            return f"Marca removida com sucesso!"
    except sqlite3.Error as e:
        return f"Erro ao remover marca: {e}"

def Obter_tabela_marcas():
    conn = sqlite3.connect(LOCAL_DB)
    #cursor = conn.cursor()
    string_sql = "SELECT * FROM marca_modelo"
    marcas = pd.read_sql(string_sql, conn)

    novos_nomes = {
        'marca': 'Marca',
        'modelo': 'Modelo'
    }
    conn.close()
    return marcas.rename(columns=novos_nomes)

def Obter_lista_marcas():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT marca, modelo FROM marca_modelo")
    categorias = cursor.fetchall()
    conn.close()
    return [f"{categoria[0]} - {categoria[1]}" for categoria in categorias]

# --------------------------------------------------------------------------------------
# CADASTRO DE COMBUSTIVEL

def Salvar_combustivel(nome_combustivel):
    try:
        with sqlite3.connect(LOCAL_DB) as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO combustivel (nome_combustivel) VALUES(?)", (nome_combustivel,))

            return f"Marca '{nome_combustivel}' salva com sucesso!"

    except sqlite3.IntegrityError as e:
        return f"Erro: A marca '{nome_combustivel}' já existe no banco de dados."

    except sqlite3.Error as e:
        return f"Erro ao salvar a marca: {e}"
    
def Remover_combustivel(id_combustivel):
    try:
        with sqlite3.connect(LOCAL_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM combustivel WHERE id = ?", (id_combustivel,))
            conn.commit()
            return f"Combustível removido com sucesso!"
    except sqlite3.Error as e:
        return f"Erro ao remover combustível: {e}"
     
def Obter_tabela_combustivel():
    conn = sqlite3.connect(LOCAL_DB)    
    query = "SELECT * FROM combustivel"

    combustivel = pd.read_sql(query, conn)
    conn.close()

    return combustivel.rename(columns={'nome_combustivel': 'Combustível'})

def Obter_lista_combustivel():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT nome_combustivel FROM combustivel")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[0] for categoria in categorias]

# --------------------------------------------------------------------------------------
# CADASTRO DE VEICULOS


def Salvar_veiculo():

    pass

def Atualizar_veiculo():
    pass

def Remover_veiculo():
    pass


def obter_tabela_veiculos():
    pass


def Obter_lista_veciulos():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros")
    carros = cursor.fetchall()
    conn.close()
    return [(carro[0], carro[4]) for carro in carros]


def Obter_lista_carros():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[4:9] for categoria in categorias]


# --------------------------------------------------------------------------------------
# CADASTRO DE MOTORISTAS

def Salvar_motorista(nome, cpf, telefone, email, data_nascimento, habilitacao_categoria, dt_validade_cnh, status):
    try:
        with sqlite3.connect(LOCAL_DB) as conn:
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO motorista 
                (nome, cpf, telefone, email, data_nascimento, habilitacao_categoria, dt_validade_cnh, status) 
                VALUES(?,?,?,?,?,?,?,?)""", 
                (nome, cpf, telefone, email, data_nascimento, habilitacao_categoria, dt_validade_cnh, status)
            )

            return f"Motorista '{nome}' salvo com sucesso!"

    except sqlite3.IntegrityError as e:
        return f"Erro: O CPF '{cpf}' já existe no banco de dados."

    except sqlite3.Error as e:
        return f"Erro ao salvar o motorista: {e}"
    
def Remover_motorista(id_motorista):
    try:
        with sqlite3.connect(LOCAL_DB) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM motorista WHERE id = ?", (id_motorista,))
            conn.commit()
            return f"Motorista removido com sucesso!"
    except sqlite3.Error as e:
        return f"Erro ao remover motorista: {e}"

def Obter_tabela_motorista():
    conn = sqlite3.connect(LOCAL_DB)    
    query = "SELECT * FROM motorista"

    motorista = pd.read_sql(query, conn)
    conn.close()

    novos_nomes = {
        'id': 'id',
        'nome': 'Nome',
        'cpf': 'CPF',
        'telefone': 'Telefone',
        'email': 'Email',
        'data_nascimento': 'Data de Nascimento',
        'habilitacao_categoria': 'Categoria CNH',
        'dt_validade_cnh': 'Validade CNH',
        'status': 'Status'
    }

    return motorista.rename(columns=novos_nomes)