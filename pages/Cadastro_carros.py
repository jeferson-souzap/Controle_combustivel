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

#Precisa criar um link com o DB para mostrar os resultados cadastrados
#Solicitar o usuário revisar o cadastro 1 mes por mes (opcional)

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



#precisa organizar melhor os controles na tela

st.markdown('### Cadastro de carros ###')

data_cadastro = st.date_input('Data Cadastro', value='today', format='DD/MM/YYYY')

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

observacoes = st.text_input('', placeholder='Campo de observação', max_chars=100)



#--------------------------------------------------------------
# BOTÕES DE CONTROLE

if st.button("Salvar Valores", key='bt_add_carr'):
        Adicionar_carro(data_cadastro, marca, modelo, nome_completo, ano, placa, total_tanque, consumo_litros, autonomia, tipo_combustivel, observacoes)
        st.success('Salvo com sucesso!')


with st.expander('Edição de cadastro', expanded=False):
    select_carros = pd.DataFrame(Obter_select_box_carros(), columns=['id', 'nome_completo'])
    nome_carro_edit = st.selectbox('', options=select_carros['nome_completo'])    
    id_selecionado = select_carros.loc[select_carros['nome_completo'] == nome_carro_edit, 'id'].values[0]
    st.write(id_selecionado)

    #-------------------------------------------------------------------------------------
    #BOTÕES DE ATUALIZAR E REMOVER
    col_bt01, col_bt02 = st.columns(2)

    with col_bt01:
        if st.button("Atualiza Carro Selecionado", key='bt_edit_carr'):
                #Ainda falta implementar a função que atualiza o registro 
                pass


    with col_bt02:
       if st.button("Remover Carro selecionado", key='bt_delet_carr'):
        st.write(f"Tentando remover carro com ID: {id_selecionado}") 
        sucesso, mensagem = Remover_carro(id_selecionado)
        if sucesso:
            st.success(mensagem)
            st.rerun()
        else:
            st.error(mensagem)
                

#--------------------------------------------------------------
st.divider()

lista_carros = pd.DataFrame(Obter_lista_carros())
st.dataframe(lista_carros)

#--------------------------------------------------------------

