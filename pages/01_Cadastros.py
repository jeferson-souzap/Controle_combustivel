import locale
import streamlit as st
import datetime

# --------------------------------------------------------------
# Importa o arquivo de configuração, se necessário
# from utils.config import *
# --------------------------------------------------------------

# --------------------------------------------------------------
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
st.set_page_config(page_title='Formulários', initial_sidebar_state='collapsed', layout='centered')
# --------------------------------------------------------------

st.title("Sistema de Cadastros")
st.markdown("---")

## Formulário de Cadastro de Marcas e Combustível
with st.expander('Cadastro de Marcas e Combustível', expanded=True):
    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Cadastro de Marcas')
        with st.form(key='form_marca'):
            nome_marca = st.text_input('Nome da Marca', placeholder='Ford')

            # Botão de envio do formulário
            submit_marca = st.form_submit_button(label='Salvar Marca')

            if submit_marca:
                if nome_marca:
                    st.success(f'Marca "{nome_marca}" salva com sucesso!')
                else:
                    st.error('Por favor, insira o nome da marca.')

    with col2:
        st.subheader('Cadastro de Combustível')
        with st.form(key='form_combustivel'):
            nome_combustivel = st.text_input('Tipo de Combustível', placeholder='Etanol')

            # Botão de envio do formulário
            submit_comb = st.form_submit_button(label='Salvar Combustível')

            if submit_comb:
                if nome_combustivel:
                    st.success(f'Combustível "{nome_combustivel}" salvo com sucesso!')
                else:
                    st.error('Por favor, insira o tipo de combustível.')

# Divisor visual para separar as seções
st.markdown("---")

## Formulário de Cadastro de Motorista
with st.expander('Cadastro de Motorista', expanded=True):
    with st.form(key='form_motorista'):
        col_motorista_left, col_motorista_right = st.columns(2)

        with col_motorista_left:
            st.text_input('Nome', key='nome_motorista')
            st.text_input('CPF', placeholder='000.000.000-00')
            st.text_input('Telefone', placeholder='(99) 99999-9999')
            st.text_input('Email', placeholder='nome@email.com')

        with col_motorista_right:
            st.date_input('Data de Nascimento')
            st.selectbox('Status', ('Ativo', 'Inativo'))
            st.text_input('Categoria da CNH', max_chars=1, placeholder='Ex: B')
            st.date_input('Validade CNH')

        # Centralizando os botões na parte inferior do formulário
        st.markdown("---")
        col_botoes_motorista_left, col_botoes_motorista_right, _ = st.columns([1, 1, 4])

        with col_botoes_motorista_left:
            salvar_motorista = st.form_submit_button("Salvar")

        with col_botoes_motorista_right:
            # Para o botão "Atualizar", você pode adicionar uma lógica separada se necessário,
            # ou remover e tratar todas as ações dentro do `submit_button`.
            # Por simplicidade, vamos usar um único botão de submit.
            pass

        if salvar_motorista:
            st.success('Motorista salvo com sucesso!')

with st.expander('Cadastro de Carros', expanded=True):
    with st.form(key='form_carros'):
        st.subheader("Informações do Veículo")
        col1, col2 = st.columns(2)

        with col1:
            st.text_input('Marca', placeholder='Ex: Ford')
            st.text_input('Modelo', placeholder='Ex: Ka')
            # Combustível agora é uma lista de opções
            combustivel_options = ['Gasolina', 'Etanol', 'Diesel', 'Flex', 'Elétrico']
            st.selectbox('Tipo de Combustível', options=combustivel_options)

        with col2:
            st.number_input('Ano de Fabricação', min_value=1900, max_value=datetime.date.today().year, value=datetime.date.today().year)
            st.text_input('Placa', placeholder='AAA-0A00 ou AAA0A00', help='Formato: 3 letras e 4 números ou 3 letras, 1 número, 1 letra, 2 números.')
            # Status agora é uma lista de opções
            status_options = ['Ativo', 'Em Manutenção', 'Vendido', 'Inativo']
            st.selectbox('Status', options=status_options)

        st.markdown("---")
        st.subheader("Detalhes Técnicos")
        col3, col4 = st.columns(2)
        with col3:
            st.number_input('Consumo (Km/L)', min_value=0.01, format="%.2f", help='Consumo médio em quilômetros por litro')
        with col4:
            st.number_input('Capacidade do Tanque (Litros)', min_value=1)

        # Divisor visual
        st.markdown("---")

        # Botão de submissão do formulário
        col_botoes, _ = st.columns([1, 4])
        with col_botoes:
            submit_carro = st.form_submit_button("Salvar Cadastro")

        if submit_carro:
            # Aqui você adicionaria a lógica para processar os dados
            # e verificar se os campos foram preenchidos
            st.success("Cadastro do carro realizado com sucesso!")


