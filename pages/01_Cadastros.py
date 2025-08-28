import locale
import streamlit as st
import datetime

# --------------------------------------------------------------
# Importa o arquivo de configuração, se necessário
from utils import *
from utils.config_cadastro_db import *

# --------------------------------------------------------------

# --------------------------------------------------------------
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
st.set_page_config(page_title='Formulários', initial_sidebar_state='collapsed', layout='centered')
# --------------------------------------------------------------

st.title("Sistema de Cadastros")

with st.expander('Cadastro de Marcas e Combustível', expanded=True):

    st.subheader('Cadastro de Marcas')
    with st.form(key='form_marca'):
        nome_marca = st.text_input('Nome da Marca', placeholder='Ford')
        nome_modelo = st.text_input('Nome d Modelo', placeholder='KA')

        # Botão de envio do formulário
        submit_marca = st.form_submit_button(label='Salvar Marca')

        if submit_marca:
            if nome_marca:
                msg = Salvar_marca_modelo(nome_marca, nome_modelo)
                st.success(f'{msg} Com sucesso')
                st.rerun()
            else:
                st.error('Por favor, insira o nome da marca.')

    st.divider()
    
    st.subheader('Cadastro de Combustível')
    with st.form(key='form_combustivel'):
        nome_combustivel = st.text_input('Tipo de Combustível', placeholder='Etanol')

        # Botão de envio do formulário
        submit_comb = st.form_submit_button(label='Salvar Combustível')

        if submit_comb:
            if nome_combustivel:
                msg = Salvar_combustivel(nome_combustivel)
                st.success(f'{msg} Com sucesso')
                st.rerun()
            else:
                st.error('Por favor, insira o tipo de combustível.')


#-------------------------------------------------------------------
#-------------------------------------------------------------------
## Tabelas Marcas e Combustível

with st.expander('Tabelas Marcas e Combustivel', expanded=False):
    tab01, tab02 = st.columns(2)
    with tab01:
        st.dataframe(Obter_tabela_marcas())
    
    with tab02:
        st.dataframe(Obter_tabela_combustivel())


    with st.form(key='form_remover'):

        df_marca = Obter_tabela_marcas()
        df_combustivel = Obter_tabela_combustivel()
        
        # Cria um dicionário onde a chave é a string do selectbox e o valor é o ID
        map_marca_to_id = {
            f"{row['Marca']} - {row['Modelo']}": row['id']
            for index, row in df_marca.iterrows()
        }
        # Cria a lista de strings para exibir no selectbox
        nomes_marcas = list(map_marca_to_id.keys())
        
        # 2. Mapeamento para Combustíveis
        map_combustivel_to_id = {
            row['Combustível']: row['id']
            for index, row in df_combustivel.iterrows()
        }
        nomes_combustivel = list(map_combustivel_to_id.keys())
        
        col01, col02 = st.columns(2)
        with col01:
            # Passa a lista de nomes para o selectbox
            nomes_marcas_selecionados = st.selectbox('Selecione as Marcas para remover:', nomes_marcas)
            bt_remover_marca = st.form_submit_button('Remover Marca Selecionada')
            
            if bt_remover_marca:
                # Pega o ID usando o nome selecionado no selectbox como chave do dicionário
                id_para_remover = map_marca_to_id.get(nomes_marcas_selecionados)
                if id_para_remover:
                    Remover_marca(id_para_remover)
                    st.success('Marca removida com sucesso!')
                    st.rerun() 
                else:
                    st.error("Erro: ID da marca não encontrado.")

        with col02:
            # Passa a lista de nomes para o selectbox
            nomes_combustivel_selecionados = st.selectbox('Selecione os Combustíveis para remover:', nomes_combustivel)
            bt_remover_combustivel = st.form_submit_button('Remover Combustível Selecionado')
            
            if bt_remover_combustivel:
                # Pega o ID usando o nome selecionado no selectbox como chave do dicionário
                id_para_remover = map_combustivel_to_id.get(nomes_combustivel_selecionados)
                if id_para_remover:
                    Remover_combustivel(id_para_remover)
                    st.success('Combustível removido com sucesso!')
                    st.rerun()
                else:
                    st.error("Erro: ID do combustível não encontrado.")
                
        


#-------------------------------------------------------------------
#-------------------------------------------------------------------

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



with st.expander('Tabela Cadastro Motorista', expanded=False):
    tab01, tab02 = st.columns(2)
    pass



#-------------------------------------------------------------------

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



with st.expander('Tabela Cadastro Carros', expanded=False):
    tab01, tab02 = st.columns(2)
    pass



#-------------------------------------------------------------------
