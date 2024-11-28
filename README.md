# 🍤 Desafio Coco Bambu - Engenharia de Dados

## 📜 Sobre o Projeto
Este repositório contém a solução para os desafios práticos de **Engenharia de Dados** propostos pelo restaurante **Coco Bambu**. Os desafios envolvem modelagem e estruturação de dados, ingestão em data lakes, criação de pipelines escaláveis e análise de grandes volumes de dados.

## 🚀 Tecnologias e Ferramentas
As seguintes tecnologias e ferramentas foram utilizadas para a implementação do projeto:

- **Python**: Linguagem principal para os scripts e processamento.
- **PySpark**: Para ingestão e transformação de grandes volumes de dados.
- **SQL**: Modelagem do Data Warehouse e consultas analíticas.
- **MySQL**: Banco de dados relacional para armazenar os dados estruturados.
- **JSON**: Formato de armazenamento de dados no Data Lake.
- **Docker**: Para virtualização de ambientes.
- **Visual Paradigm**: Para o diagramação do modelo de dados.


## 🗂️ Estrutura do Repositório
```plaintext
.
├── data_lake/              # Diretório do Data Lake
│   ├── store_id=1/
│   │   ├── bus_dt=2024-01-01/
│   │   │   ├── detail_lines.json
│   │   │   ├── detail_metadata.json
│   │   │   ├── fato_pedidos.json
│   │   │   ├── dim_lojas.json
│   │   │   ├── dim_datas.json
│   │   │   └── dim_itens.json
├── scripts/                # Scripts Python
│   ├── ingestion.py        # Código de ingestão com PySpark
│   ├── transformation.sql  # Queries SQL para transformação
│   └── validation.py       # Scripts para validação do esquema
├── diagrams/               # Diagramas do modelo de dados
├── README.md               # Documentação do repositório
└── requirements.txt        # Dependências do projeto
```

## 📈 Modelagem do Data Lake
O modelo de dados foi desenvolvido seguindo as melhores práticas de modelagem dimensional. Ele é composto por:

Fato: fato_pedidos com dados financeiros do pedido.  
Dimensões:  
dim_lojas para dados das lojas.  
dim_itens para itens do cardápio.  
dim_datas para datas.  
detail_lines e detail_metadata para granularidade das linhas do pedido.  
### 📐 Diagrama do Modelo  
![Diagrama](https://github.com/user-attachments/assets/a3261c64-6a36-47df-a027-68a17b824f04)

## 🔄 Fluxo de Dados
O fluxo de dados foi implementado para atender os seguintes passos:

Extração: Dados recebidos via API no formato JSON.  
Ingestão: Armazenamento dos arquivos no Data Lake, organizados por loja e data.  
Transformação: Estruturas transformadas e carregadas no banco de dados relacional.  
Validação: Scripts de validação garantem a integridade e consistência dos dados.  

## 🛠️ Como Executar o Projeto

### Pré-requisitos
Docker: Para criar os containers necessários.  
Spark: Para processamento dos dados.  
Python: Para execução dos scripts.  

### Passos
### 1. Clone este repositório:
```plaintext
git clone https://github.com/igorferrer-data/desafio-coco-bambu.git  
cd desafio-coco-bambu
```
### 2. Instale as dependências:
```plaintext
pip install -r requirements.txt
```
### 3. Execute o pipeline de ingestão:
```plaintext
python scripts/ingestion.py
```
### 4. Visualize os dados no banco de dados relacional (MySQL).

## 📬 Contato
- Nome: Igor Ferrer  
- LinkedIn: [Seu Perfil](https://www.linkedin.com/in/igor-ferrer-01b945112/)  
- E-mail: igori83@gmail.com  


