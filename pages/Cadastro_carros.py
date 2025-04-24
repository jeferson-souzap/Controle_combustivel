import locale
import streamlit as st
import datetime

#--------------------------------------------------------------
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
st.set_page_config(page_title='Cadastro', initial_sidebar_state='collapsed')
#--------------------------------------------------------------


st.markdown('### Cadastro do preço de combustivel atual ###')
col_comb01, col_comb02 = st.columns(2)
with col_comb01:
    preco_gasolina = st.number_input('Valor da Gasolina', placeholder='7,555')
    ult_vlr_gasolina = 5.79 # retornar do banco de dados
    ult_vlr_gasolinaf = locale.format_string("%.2f", ult_vlr_gasolina, grouping=True)    
    st.metric(label='Ultimo valor', value=ult_vlr_gasolinaf)
    

with col_comb02:
    preco_etanol = st.number_input('Valor do **Etanol**', placeholder='7,555')
    ult_vlr_etanol = 5.19 # retornar do banco de dados
    ult_vlr_etanolf = locale.format_string("%.2f", ult_vlr_etanol, grouping=True)    
    st.metric(label='Ultimo valor', value=ult_vlr_etanolf)    


if st.button("Salvar Valores", key='bt_add_preco'):
    # Aqui você pode adicionar a lógica para adicionar a despesa ao banco de dados
    st.success("Despesa adicionada com sucesso!")
    

#--------------------------------------------------------------
st.divider()
#--------------------------------------------------------------

st.markdown('### Cadastro de carros ###')

col01, col02  = st.columns(2)
with col01:
    marca_carro = st.text_input('Informe a Marca do Carro', placeholder='Ford')
    modelo_carro = st.text_input('Informe o modelo do Carro', placeholder='KA 1.0')
    ano_carro = st.number_input('Ano do Carro', placeholder='2025', min_value=1900)

with col02:
    km_atual = st.number_input('Quilometragem atual ', placeholder='10999')    
    km_litro = st.number_input('Quilometros por litro (Km/L)', placeholder='9,8')
    placa = st.text_input('Placa do carro', placeholder='ABC 1234')


if st.button("Salvar Valores", key='bt_add_carr'):
    # Aqui você pode adicionar a lógica para adicionar a despesa ao banco de dados
    st.success("Despesa adicionada com sucesso!")

st.divider()
#--------------------------------------------------------------
col03, col04 = st.columns(2, border=True)
with col03:
    st.write('Autonomia do tanque')
    total_litros = 2
    autonomia_tanque = 5

with col04:
    st.markdown('Litros no tanque')

st.divider()
st.dataframe()



