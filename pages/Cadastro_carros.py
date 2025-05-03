import locale
import streamlit as st
import datetime

#--------------------------------------------------------------
from utils.config import *
#--------------------------------------------------------------

#--------------------------------------------------------------
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
st.set_page_config(page_title='Cadastro', initial_sidebar_state='collapsed')
#--------------------------------------------------------------

st.markdown('### Cadastro do preço de combustivel atual ###')

col_comb01,col_comb02 = st.columns(2)

col_comb01, col_comb02 = st.columns(2)
with col_comb01:
    lista_combustivel = pd.DataFrame(Obter_combustivel())
    nome_combustivel = st.selectbox('', options=lista_combustivel, key='nome_combustivel01')   
    

with col_comb02:
    preco_etanol = st.number_input('', placeholder='7,555')
    ult_vlr_etanol = 5.19 # retornar do banco de dados
    ult_vlr_etanolf = locale.format_string("%.2f", ult_vlr_etanol, grouping=True)

if st.button("Atualizar", key='bt_add_preco'):
    # Aqui você pode adicionar a lógica para adicionar a despesa ao banco de dados
    st.success("Despesa adicionada com sucesso!")
    
lista_combustivel = pd.DataFrame(Obter_combustivel())
st.dataframe(lista_combustivel)


#--------------------------------------------------------------
st.divider()
#--------------------------------------------------------------

'''
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

'''



st.markdown('### Cadastro de carros ###')

data_atual = st.date_input('Informe a data', value='today', format='DD/MM/YYYY')

marca = st.text_input('Marca do Carro', placeholder='Ford')
modelo = st.text_input('Modelo do Carro', placeholder='KA')
nome_completo = marca + " - " + modelo
st.markdown(nome_completo)

ano = st.number_input('Ano do Carro', placeholder='2024', step=1)
placa = st.text_input('Placa do carro', placeholder='ABC 1234')

#trocar pela informação do banco de dados
tipo_combustivel = st.selectbox('', options=['Gasolina', 'Etanol', 'GNV', 'Elétrico'])


total_tanque = st.number_input('Capacidade do Tanque (Litros)', step=1)
consumo_litros = st.number_input('Quilometros por litro (Km/L)', placeholder='9,8')

if consumo_litros > 0 and total_tanque >0:
     autonomia = total_tanque * consumo_litros
else:
     autonomia = 0

st.markdown(f'Autonomia total (km) = {autonomia}')

obervacao = st.text_input('', placeholder='Campo de observação', max_chars=100)





#--------------------------------------------------------------
# BOTÕES DE CONTROLE
col_bt01, col_bt02, col_bt03 = st.columns(3)

with col_bt01:
    if st.button("Salvar Valores", key='bt_add_carr'):
        resultado, mensagem = Adicionar_carro(marca, modelo, ano, placa, obervacao)

        if resultado:
            st.success(mensagem)
        else:
            st.warning(f'Erro - {mensagem}')
            st.rerun()

with col_bt02:
    if st.button("Salvar Valores", key='bt_edit_carr'):
            resultado, mensagem = Adicionar_carro(marca, modelo, ano, placa, obervacao)

            if resultado:
                st.success(mensagem)
            else:
                st.warning(f'Erro - {mensagem}')
                st.rerun()

with col_bt03:
    if st.button("Salvar Valores", key='bt_delet_carr'):
            resultado, mensagem = Adicionar_carro(marca, modelo, ano, placa, obervacao)

            if resultado:
                st.success(mensagem)
            else:
                st.warning(f'Erro - {mensagem}')
                st.rerun()


#--------------------------------------------------------------
st.divider()
#--------------------------------------------------------------

