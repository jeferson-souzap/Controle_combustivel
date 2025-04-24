import locale
import streamlit as st
import datetime

#--------------------------------------------------------------
from utils.config import Adicionar_carro, Obter_tabela_carros, Obter_carros_para_selecao, Adicionar_tanque, Obter_info_tabela_carros
#--------------------------------------------------------------

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

data_atual = st.date_input('Informe a data', value='today', format='DD/MM/YYYY')

col01, col02  = st.columns(2)
with col01:
    marca_carro = st.text_input('Informe a Marca do Carro', placeholder='Ford')
    modelo_carro = st.text_input('Informe o modelo do Carro', placeholder='KA 1.0')
    ano_carro = st.number_input('Ano do Carro', placeholder='2025', min_value=1900)

with col02:
    km_atual = st.number_input('Quilometragem atual ', placeholder='10999')    
    km_litro = st.number_input('Quilometros por litro (Km/L)', placeholder='9,8')
    placa = st.text_input('Placa do carro', placeholder='ABC 1234')

obervacao = st.text_input('', placeholder='Campo de observação', max_chars=100)

#--------------------------------------------------------------
# BOTÃO DE ADICIONAR CARRO
if st.button("Salvar Valores", key='bt_add_carr'):
    resultado, mensagem = Adicionar_carro(marca_carro, modelo_carro, ano_carro, placa, km_atual, obervacao)

    if resultado:
        st.success(mensagem)
    else:
        st.warning(f'Erro - {mensagem}')
        st.rerun()
      

#--------------------------------------------------------------
st.divider()
#--------------------------------------------------------------


with st.expander('Configuração Abançada', expanded=True):

    carros_db = Obter_carros_para_selecao()
    if not carros_db:
        st.warning('Nenhum carro cadastrado encontrado')

    carro_selecionado = st.selectbox(
        'Selecione o Carro', 
        options=carros_db,
        format_func=lambda x: x[1]
        )

    carro_id = carro_selecionado[0]

    capacidade = st.number_input('Capacidade do Tanque em (L)', min_value=1.0, step=0.1)
    tipo_combustivel = st.selectbox(
        'Escolha um Combustivel', 
        options=['Gasolina', 'Etanol', 'Diesel', 'Flex', 'GNV', 'Elétrico']
        )
    autonomia_media = st.number_input('Autonomia média (Km/l):', min_value=0.1, step=0.1)    
    
    

    if st.button("Cadastrar informação"):
        resultado02, mensagem02 = Adicionar_tanque(
            carro_id=carro_id,
            capacidade_tanque=capacidade,
            tipo_combustivel=tipo_combustivel,
            autonomia_media=autonomia_media
        )
    
        if resultado02:
            st.success(mensagem02)            
        else:
            st.error(f'Erro - {mensagem02}')
            st.rerun()



    col03, col04 = st.columns(2, border=True)
    with col03:
        st.write('Autonomia do tanque')
        total_litros = 2
        autonomia_tanque = 5

    with col04:
        st.markdown('Litros no tanque')






st.divider()

col_frame01, col_frame02 = st.columns(2)

with col_frame01:
    st.markdown('Tabela de Carros')
    st.dataframe(
        Obter_tabela_carros(),
        use_container_width=True,  
        hide_index=True,           # Oculta o índice
        column_config={            
            "Quilometragem": st.column_config.NumberColumn(format="%.0f km")
        }
    )


with col_frame02:
    st.markdown('Tabela com informações dos Carros')
    st.dataframe(
        Obter_info_tabela_carros(),
        use_container_width=True,  
        hide_index=True,           # Oculta o índice        
        column_config={            
            "Autonomia": st.column_config.NumberColumn(format="%.0f km")
        }
    )