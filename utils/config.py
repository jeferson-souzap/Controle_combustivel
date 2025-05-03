import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
import streamlit as st
import sqlite3
from database.db import LOCAL_DB



#--------------------------------------------------------------------------------------
# CADASTRO DE CARROS

def Adicionar_carro(marca_carro, modelo_carro, ano_carro, placa, km_atual, obervacao):
    pass



#modificar para carros
def remover_categoria(nome):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE nome = ?", (nome))
    conn.commit()
    conn.close()




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

