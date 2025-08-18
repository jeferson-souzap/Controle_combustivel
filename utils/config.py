import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
import streamlit as st
import sqlite3
from database.db import LOCAL_DB



#--------------------------------------------------------------------------------------
# CADASTRO DE CARROS

def Adicionar_carro(data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia, tipo_combustivel, observacoes):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO carros (data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia, tipo_combustivel, observacoes)"
        "VALUES(?,?,?,?,?,?,?,?,?,?,?)",
        (data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia, tipo_combustivel, observacoes)
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


#--------------------------------------------------------------------------------------


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

