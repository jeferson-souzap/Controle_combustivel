# FuelTrack - Aplicativo de Controle de Combustível

### Resumo

O aplicativo nasceu com a necessidade de poder controlar o consumo de combustivel baseado nas configurações do carro.
Vale lembrar que é um calculo aproximado, que pode ajudar muito na programação de viagens longas.

## Descrição

FuelTrack é uma aplicação web desenvolvida em Python com Streamlit que permite aos usuários gerenciar e monitorar o consumo de combustível de seus veículos.
O aplicativo oferece recursos como cadastro de veículos, acompanhamento de abastecimentos, previsões de autonomia e planejamento de viagens.
Funcionalidades

**Cadastro de Veículos:**
Registre seus carros com especificações detalhadas (marca, modelo, ano, tipo de combustível, capacidade do tanque, consumo médio)

**Registro de Abastecimentos:** Acompanhe cada abastecimento realizado

**Monitoramento de Consumo:** Visualize estatísticas de consumo por veículo

**Previsão de Autonomia:** Calcule quanto tempo e quilômetros seu combustível atual vai durar

**Planejador de Viagens:** Faça projeções de consumo para viagens planejadas

## Tecnologias Utilizadas

Python: Linguagem de programação principal
Streamlit: Framework para desenvolvimento da interface web
Pandas: Manipulação e análise de dados
Matplotlib/Plotly: Visualização de dados e gráficos

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fueltrack.git
cd fueltrack

### Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
Como Executar
bashstreamlit run app.py
```

### Estrutura do Projeto

```bash
fueltrack/
├── app.py                  # Ponto de entrada principal
├── pages/                  # Páginas do aplicativo
│   ├── cadastro_veiculos.py
│   ├── abastecimentos.py
│   ├── estatisticas.py
│   └── planejador_viagens.py
├── utils/                  # Funções utilitárias
│   ├── calculo_consumo.py
│   └── data_manager.py
├── data/                   # Armazenamento de dados
│   ├── veiculos.csv
│   └── abastecimentos.csv
├── assets/                 # Recursos estáticos
└── requirements.txt        # Dependências do projeto
```