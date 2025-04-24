import streamlit as st
import sqlite3
from datetime import datetime
import pandas as pd
import streamlit as st
import sqlite3
from database.db import LOCAL_DB

'''
marca, modelo, ano, placa, quilometragem_atual, data_cadastro, observacoes
'''
'''
def Adicionar_carro(marca, modelo, ano, placa, km_atual, data_cadastro, observacoes):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categoria (marca, modelo, ano, placa, quilometragem_atual, data_cadastro, observacoes) VALUES (?,?,?,?,?,?,?)", (marca, modelo, ano, placa, km_atual, data_cadastro, observacoes))
    conn.commit()
    conn.close()'''

def Adicionar_carro(marca, modelo, ano, placa, km_atual=0, observacoes=None):
    """
    Adiciona um novo carro ao banco de dados com tratamento de erros
    
    Parâmetros:
    - marca: str (obrigatório)
    - modelo: str (obrigatório)
    - ano: int (obrigatório)
    - placa: str (obrigatório, formato válido)
    - km_atual: float (opcional, default=0)
    - observacoes: str (opcional)
    
    Retorna:
    - (success, message) onde success é booleano e message contém detalhes
    """
    
    # Validações iniciais
    if not all([marca, modelo, ano, placa]):
        return False,
    
    ''' 
    try:
        ano = int(ano)
        if ano < 1900 or ano > datetime.now().year + 1:
            return False, "Ano inválido"
    except ValueError:
        return False, "Ano deve ser um número inteiro"
    '''
    
    try:
        km_atual = float(km_atual)
        if km_atual < 0:
            return False, "Quilometragem não pode ser negativa"
    except ValueError:
        return False, "Quilometragem deve ser um número"
    
    # Formata a placa (remove espaços e traços)
    placa = placa.upper().replace(" ", "").replace("-", "")
    if len(placa) != 7 or not placa[:3].isalpha() or not placa[3:].isalnum():
        return False, "Formato de placa inválido (use AAA9999 ou AAA9A99)"
    
    conn = None
    try:
        conn = sqlite3.connect(LOCAL_DB)
        cursor = conn.cursor()
        
        # Verifica se a placa já existe
        cursor.execute("SELECT 1 FROM carros WHERE placa = ?", (placa,))
        if cursor.fetchone():
            return False, "Placa já cadastrada no sistema"
        
        # Insere o novo carro
        data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute(
            "INSERT INTO carros (marca, modelo, ano, placa, km_atual, data_cadastro, observacoes) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (marca.strip(), modelo.strip(), ano, placa, km_atual, data_cadastro, observacoes.strip() if observacoes else None)
        )
        
        conn.commit()
        return True, "Carro cadastrado com sucesso!"
        
    except sqlite3.Error as e:
        return False, f"Erro no banco de dados: {str(e)}"
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"
    finally:
        if conn:
            conn.close()

#modificar para carros
def remover_categoria(nome):
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE nome = ?", (nome))
    conn.commit()
    conn.close()

'''
#modificar para listar os carros
def Obter_carros():
    conn = sqlite3.connect(LOCAL_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM carros")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[1:5] for categoria in categorias]

'''

def Obter_tabela_carros():
    """
    Obtém todos os carros cadastrados e retorna um DataFrame com colunas renomeadas
    """
    conn = sqlite3.connect(LOCAL_DB)
    try:
        # Obtém os dados e os nomes das colunas
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM carros")
        dados = cursor.fetchall()
        
        # Obtém os nomes das colunas
        cursor.execute("PRAGMA table_info(carros)")
        colunas = [info[1] for info in cursor.fetchall()]
        
        # Cria o DataFrame
        df = pd.DataFrame(dados, columns=colunas)
        
        # Renomeia as colunas para exibição amigável
        df = df.rename(columns={
            'id': 'ID',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'ano': 'Ano',
            'placa': 'Placa',
            'km_atual': 'Quilometragem',
            'data_cadastro': 'Data de Cadastro',
            'observacoes': 'Observações'
        })
        
        # Seleciona apenas as colunas relevantes para exibição
        colunas_exibir = ['Marca', 'Modelo', 'Ano', 'Placa', 'Quilometragem']
        return df[colunas_exibir]
        
    finally:
        conn.close()



def Obter_carros_para_selecao():
    """Retorna uma lista de tuplas (id, descrição) dos carros cadastrados"""
    conn = sqlite3.connect(LOCAL_DB)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, marca, modelo, placa FROM carros")
        carros = cursor.fetchall()
        
        # Formata: (id, "Marca Modelo - PLACA")
        return [(carro[0], f"{carro[1]} {carro[2]} - {carro[3]}") for carro in carros]
    finally:
        conn.close()


def Adicionar_tanque(carro_id, capacidade_tanque, tipo_combustivel, autonomia_media=None):
    """
    Adiciona informações de tanque para um carro específico
    
    Parâmetros:
    - carro_id: ID do carro na tabela carros (INTEGER)
    - capacidade_tanque: Capacidade total em litros (REAL)
    - tipo_combustivel: Tipo de combustível (TEXT) - ex: "Gasolina", "Etanol", "Diesel"
    - autonomia_media: Autonomia média em km/l (REAL, opcional)
    
    Retorna:
    - (success, message) onde success é booleano e message contém detalhes
    """
    
    # Validações básicas
    if not all([carro_id, capacidade_tanque, tipo_combustivel]):
        return False, "Todos os campos obrigatórios devem ser preenchidos"
    
    try:
        carro_id = int(carro_id)
        capacidade_tanque = float(capacidade_tanque)
        if capacidade_tanque <= 0:
            return False, "Capacidade do tanque deve ser positiva"
    except ValueError:
        return False, "ID do carro e capacidade devem ser números válidos"
    
    conn = None
    try:
        conn = sqlite3.connect(LOCAL_DB)
        cursor = conn.cursor()
        
        # Verifica se o carro existe
        cursor.execute("SELECT 1 FROM carros WHERE id = ?", (carro_id,))
        if not cursor.fetchone():
            return False, "Carro não encontrado"
        
        # Verifica se o carro já tem tanque cadastrado
        cursor.execute("SELECT 1 FROM tanques WHERE carro_id = ?", (carro_id,))
        if cursor.fetchone():
            return False, "Este carro já possui tanque cadastrado"
        
        # Insere o novo tanque
        cursor.execute(
            "INSERT INTO tanques (carro_id, capacidade_tanque, tipo_combustivel, autonomia_media) "
            "VALUES (?, ?, ?, ?)",
            (carro_id, capacidade_tanque, tipo_combustivel.strip().title(), autonomia_media)
        )
        
        conn.commit()
        return True, "Informações do tanque cadastradas com sucesso!"
        
    except sqlite3.Error as e:
        return False, f"Erro no banco de dados: {str(e)}"
    except Exception as e:
        return False, f"Erro inesperado: {str(e)}"
    finally:
        if conn:
            conn.close()
        

def Obter_info_tabela_carros():
    """
    Obtém todos os carros cadastrados e retorna um DataFrame com colunas renomeadas
    """
    conn = sqlite3.connect(LOCAL_DB)
    try:
        # Obtém os dados e os nomes das colunas
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tanques")
        dados = cursor.fetchall()
        
        # Obtém os nomes das colunas
        cursor.execute("PRAGMA table_info(tanques)")
        colunas = [info[1] for info in cursor.fetchall()]
        
        # Cria o DataFrame
        df = pd.DataFrame(dados, columns=colunas)
        
        # Renomeia as colunas para exibição amigável
        df = df.rename(columns={
            'id': 'ID',
            'capacidade_tanque': 'Capacidade',
            'tipo_combustivel': 'Tipo Combustivel',            
            'autonomia_media': 'Autonomia'
            
        })
        
        # Seleciona apenas as colunas relevantes para exibição
        colunas_exibir = ['Capacidade', 'Tipo Combustivel', 'Autonomia']
        return df[colunas_exibir]
        
    finally:
        conn.close()
