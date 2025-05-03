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


def Remover_carro(nome):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE nome = ?", (nome))
    conn.commit()
    conn.close()

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

