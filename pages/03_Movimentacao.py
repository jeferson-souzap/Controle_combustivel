import locale
import streamlit as st
import datetime

# Define a localidade para português do Brasil para formatação de datas, etc.
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Configurações da página Streamlit
st.set_page_config(
    page_title='Movimentação de Veículos',
    layout='centered',  # Centraliza o conteúdo da página
    initial_sidebar_state='collapsed'  # Sidebar inicialmente colapsada
)

# Título principal da página
st.title("Registro de Movimentação de Veículos")
st.markdown("---")  # Divisor visual

# Checkbox para indicar se houve abastecimento. ESTE CHECKBOX ESTÁ FORA DO FORMULÁRIO
# para que ele possa controlar a visibilidade dos campos de abastecimento dinamicamente.
abasteceu_checkbox = st.checkbox('O veículo abasteceu nesta movimentação?', value=False,
                                 help='Marque esta opção se houve abastecimento durante a movimentação.')

# Seção 3: Detalhes do Abastecimento (condicional e fora do form principal)
st.subheader('Informações de Abastecimento')

# A seção de abastecimento só aparece se o checkbox estiver marcado
if abasteceu_checkbox:
    # Coluna para o Posto de Combustível (agora aparece dinamicamente)
    col_posto, _ = st.columns([1, 2])
    with col_posto:
        st.selectbox('Posto de Combustível', options=['Posto BR', 'Posto Ipiranga', 'Posto Shell'],
                     help='Selecione o posto onde foi realizado o abastecimento.',
                     key='posto_combustivel')

    col9, col10, col11 = st.columns(3)  # 3 colunas para detalhes do abastecimento
    with col9:
        st.number_input('Litros Abastecidos', min_value=0.0, step=0.01, format="%.2f",
                        help='Quantidade de litros de combustível abastecidos.')
    with col10:
        st.number_input('Valor Abastecido (R$)', min_value=0.0, step=0.01, format="%.2f",
                        help='Valor total pago pelo abastecimento.')
    with col11:
        st.number_input('Qtd. no Tanque (Litros)', min_value=0.0, step=0.01, format="%.2f",
                        help='Quantidade estimada de combustível no tanque após o abastecimento.')

    col12, col13 = st.columns(2)
    with col12:
        st.number_input('Autonomia Estimada (km)', value=0.0, disabled=True, format="%.2f",
                        help='Autonomia estimada restante do veículo. Pode ser calculada.')
    with col13:
        st.date_input('Data Prevista Abastecimento', value=datetime.date.today() + datetime.timedelta(days=7),
                      help='Data estimada para o próximo abastecimento.')
else:
    # Mensagem opcional quando a seção de abastecimento está oculta
    st.info("Marque a caixa acima se houver abastecimento para preencher os detalhes.")

st.markdown("---")  # Divisor visual

# Inicia o formulário principal. Este formulário conterá os dados que serão submetidos de uma vez.
with st.form(key='form_movimentacao_principal'):
    # Seção 1: Detalhes Essenciais da Movimentação
    st.subheader('Detalhes da Movimentação')
    col1, col2, col3 = st.columns(3)  # Cria 3 colunas para organizar os campos

    with col1:
        st.date_input('Data do Movimento', value=datetime.date.today(), help='Selecione a data da movimentação.')
    with col2:
        st.selectbox('Carro (Placa)', options=['Carro A (ABC-1234)', 'Carro B (XYZ-5678)', 'Carro C (DEF-9012)'],
                     help='Selecione o veículo envolvido nesta movimentação.')
    with col3:
        st.selectbox('Motorista', options=['João Silva', 'Maria Santos', 'Pedro Oliveira'],
                     help='Selecione o motorista responsável pela movimentação.')

    col_rota, _ = st.columns([1, 2])
    with col_rota:
        st.selectbox('Rota', options=['Rota Diária', 'Entrega Externa', 'Viagem Longa'],
                     help='Selecione a rota percorrida.')

    st.markdown("---")  # Divisor visual

    # Seção 2: Registro de Quilometragem
    st.subheader('Registro de Quilometragem')
    col6, col7, col8 = st.columns(3)

    with col6:
        st.number_input('Km Inicial', min_value=0.0, step=0.1, format="%.1f",
                        help='Quilometragem registrada no início da movimentação.')
    with col7:
        st.number_input('Km Final', min_value=0.0, step=0.1, format="%.1f",
                        help='Quilometragem registrada no final da movimentação.')
    with col8:
        st.number_input('Distância Percorrida (km)', value=0.0, disabled=True, format="%.2f",
                        help='Distância total percorrida. Será calculada automaticamente.')

    st.markdown("---")  # Divisor visual

    # Seção 4: Observações (dentro do formulário principal)
    st.subheader('Observações Adicionais')
    st.text_area('Observação', height=100,
                 help='Qualquer observação relevante sobre esta movimentação (ex: problemas no veículo, rota alternativa).')

    st.markdown("---")  # Divisor visual

    # Botão de submissão do formulário principal
    col_submit, _ = st.columns([1, 4])
    with col_submit:
        submit_button = st.form_submit_button("Salvar Movimentação")

    # Lógica de processamento após a submissão do formulário
    if submit_button:
        # Aqui você coletaria os dados tanto do formulário principal
        # quanto da seção de abastecimento (se ela estiver visível).
        # Por exemplo, para acessar o valor do checkbox: abasteceu_selecionado = st.session_state['abasteceu_checkbox']
        st.success("🎉 Movimentação registrada com sucesso! Os dados foram enviados para o sistema.")
