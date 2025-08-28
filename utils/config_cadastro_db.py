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
           


def Obter_combustivel():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT nome_combustivel FROM combustivel")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[0] for categoria in categorias]


def Obter_tabela_combustivel():
    conn = sqlite3.connect(LOCAL_DB)    
    query = "SELECT * FROM combustivel"

    combustivel = pd.read_sql(query, conn)
    conn.close()

    return combustivel.rename(columns={'nome_combustivel': 'Combustível'})


# --------------------------------------------------------------------------------------

def Adicionar_carro(data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia,
                    tipo_combustivel, observacoes):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO carros (data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia, tipo_combustivel, observacoes)"
        "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        (data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia,
         tipo_combustivel, observacoes)
    )
    conn.commit()
    conn.close()


def Remover_carro(id):
    try:
        id_int = int(id)  # Converte int
        conn = sqlite3.connect(LOCAL_DB)
        cursor = conn.cursor()

        # Verifica se o ID existe
        cursor.execute("SELECT COUNT(*) FROM carros WHERE id = ?", (id_int,))
        if cursor.fetchone()[0] == 0:
            conn.close()
            return False, "ID não encontrado no banco de dados"

        # Tenta excluir o registro
        cursor.execute("DELETE FROM carros WHERE id = ?", (id_int,))
        if cursor.rowcount == 0:
            conn.rollback()
            conn.close()
            return False, "Nenhum registro foi afetado pela exclusão"

        conn.commit()
        conn.close()
        return True, "Carro removido com sucesso"
    except Exception as e:
        return False, f"Erro ao remover carro: {str(e)}"


def Atualizar_carro():
    pass


def Obter_select_box_carros():
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


def Cadastrar_combustivel(nome, valor=0.0, posto='BR'):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO combustivel (nome, valor, posto_referencia) "
        "VALUES (?, ?, ?)",
        (nome, valor, posto)
    )

    conn.commit()
    conn.close()


def Obter_combustivel():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM combustivel")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[1:2] for categoria in categorias]

