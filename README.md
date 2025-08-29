# FuelTrack - Aplicativo de Controle de Combustível

## Resumo

Um aplicativo de gerenciamento de combustível para calcular autonomia, monitorar o consumo e planejar viagens de carro, nascido da necessidade de nunca mais quebrar a bomba de gasolina.

## Descrição

O FuelTrack é uma aplicação web desenvolvida em Python e Streamlit que resolve um problema prático e comum: o controle de combustível. Criado a partir de uma experiência pessoal de falha da bomba de gasolina, o projeto tem como objetivo principal ajudar motoristas a monitorarem o consumo de seus veículos, prever a autonomia do tanque e planejar viagens com mais segurança.


## Visão Geral

O FuelTrack é uma aplicação web desenvolvida em Python e Streamlit que resolve um problema prático e comum: o controle de combustível. Criado a partir de uma experiência pessoal de falha da bomba de gasolina, o projeto tem como objetivo principal ajudar motoristas a monitorarem o consumo de seus veículos, prever a autonomia do tanque e planejar viagens com mais segurança.

### Recursos

- Registro de Dados: Cadastre veículos com especificações detalhadas (marca, modelo, tipo de combustível, etc.) e registre cada abastecimento para manter um histórico preciso.

- Monitoramento e Análise: Visualize o consumo de combustível por veículo, acompanhando médias e tendências para identificar o uso mais eficiente.

- Cálculo de Autonomia: Preveja a autonomia restante do seu tanque, sabendo quantos quilômetros você ainda pode percorrer com o combustível atual.

- Planejador de Viagens: Faça projeções de consumo para viagens longas, ajudando a planejar paradas e estimar custos.

### Tecnologias

O FuelTrack foi desenvolvido usando as seguintes tecnologias:

- Python: A linguagem principal por trás da lógica da aplicação.
-Streamlit: O framework que transformou o código Python em uma interface web interativa.
- Pandas: Usado para manipulação, processamento e análise dos dados de consumo.
- SQLite3: O banco de dados para armazenar todas as informações localmente.
- Matplotlib/Plotly: Bibliotecas de visualização para gerar gráficos e painéis interativos.

### Instalação

```bash
git clone https://github.com/seu-usuario/fueltrack.git
cd fueltrack
```

### Crie e ative um ambiente virtual (recomendado)

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```
