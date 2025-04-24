import streamlit as st
import sqlite3

from database.db import LOCAL_DB



def adicionar_carro(nome, tipo):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categoria (nome, tipo) VALUES (?, ?)", (nome, tipo))
    conn.commit()
    conn.close()


#modificar para carros
def remover_categoria(nome):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE nome = ?", (nome))
    conn.commit()
    conn.close()


#modificar para listar os carros
def obter_categorias_tipo():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, tipo FROM categoria")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[0:2] for categoria in categorias]  # Retorna uma lista de nomes
