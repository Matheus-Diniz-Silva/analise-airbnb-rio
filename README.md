# Análise do Mercado Airbnb - Rio de Janeiro

## Sobre o Projeto

Análise exploratória completa do mercado de aluguel por temporada no Rio de Janeiro através da plataforma Airbnb. Este projeto investiga os fatores que influenciam os preços e fornece insights para anfitriões e viajantes.

## Objetivos

- Identificar os principais fatores que impactam o preço das diárias
- Analisar a distribuição geográfica dos imóveis e preços
- Descobrir padrões sazonais e de disponibilidade
- Fornecer recomendações baseadas em dados para precificação

## Tecnologias Utilizadas

- Python 3.9+
- Pandas - Manipulação de dados
- Matplotlib/Seaborn - Visualizações
- Jupyter Notebook - Análise interativa
- Plotly - Gráficos interativos

## Estrutura do Projeto

- **data/raw/** - Dados originais (listings.csv.gz)
- **data/processed/** - Dados processados (airbnb_rio_processed_super_light.csv)
- **notebooks/** - Jupyter notebooks (01_eda_airbnb_rio.ipynb)
- **src/** - Códigos Python modulares
- **reports/** - Relatórios e documentação
- **images/** - Gráficos e visualizações
- **requirements.txt** - Dependências do projeto
- **README.md** - Documentação principal

## Dataset

**Base de Dados:** Inside Airbnb - Rio de Janeiro  
**Período:** Dados mais recentes disponíveis  
**Amostra:** 42.572 imóveis analisados

### Dataset Processado
O arquivo `airbnb_rio_processed_super_light.csv` contém uma amostra representativa com as colunas mais relevantes:

- **Informações básicas:** id, neighbourhood_cleansed, room_type_simple
- **Capacidade:** accommodates, bedrooms
- **Preço:** price_clean, price_category
- **Localização:** latitude, longitude
- **Avaliações:** review_scores_rating, number_of_reviews
- **Host:** host_is_superhost

## Principais Análises

- Distribuição de preços e identificação de outliers
- Análise geográfica por bairros e regiões
- Impacto das comodidades no preço
- Segmentação por tipo de imóvel
- Relação entre avaliações e preços

## Resultados e Insights

### Visão Geral do Mercado
- Total de imóveis analisados: 42,572
- Preço médio: R$ 688.01
- Preço mediano: R$ 311.00
- Faixa de preço predominante: R$ 200 - R$ 558

### Distribuição por Tipo de Imóvel
- Entire home/apt: 33,990 imóveis (79.8%) - Preço médio: R$ 762
- Private room: 8,152 imóveis (19.1%) - Preço médio: R$ 392
- Shared room: 407 imóveis (1.0%) - Preço médio: R$ 194

### Top 5 Bairros Mais Caros
1. Joá: 155 imóveis - Média: R$ 6.186 - Mediana: R$ 5.000
2. São Conrado: 364 imóveis - Média: R$ 2.548 - Mediana: R$ 754
3. Itanhangá: 179 imóveis - Média: R$ 2.457 - Mediana: R$ 352
4. Lagoa: 264 imóveis - Média: R$ 1.350 - Mediana: R$ 630
5. Gávea: 220 imóveis - Média: R$ 1.044 - Mediana: R$ 450

### Fatores que Impactam o Preço
- Capacidade média: 3.9 pessoas
- Quartos mais comuns: 1 quarto (24,895 imóveis)
- Comodidades mais populares:
  - Wi-Fi: 40,829 imóveis (95.9%)
  - Ar condicionado: 31,954 imóveis (75.1%)
  - Estacionamento: 25,212 imóveis (59.2%)
  - Piscina: 10,209 imóveis (24.0%)

## Visualizações Principais

### Distribuição de Preços
![Distribuição de Preços](images/price_distribution.png)

### Tipos de Imóvel
![Tipos de Imóvel](images/room_type_distribution.png)

### Análise Geográfica
![Mapa de Preços](images/price_geographic.png)

### Bairros Mais Caros
![Bairros Mais Caros](images/top_expensive_neighborhoods.png)

## Código Fonte (src/)

Scripts Python modulares para reproduzir a análise:

### data_cleaning.py
- `load_and_clean_data()` - Carrega e limpa os dados
- `get_missing_data_summary()` - Análise de dados missing
- `remove_price_outliers()` - Remove outliers de preço

### visualization.py  
- `plot_price_distribution()` - Gráfico de distribuição de preços
- `plot_room_type_analysis()` - Análise por tipo de imóvel
- `plot_geographic_prices()` - Mapa geográfico

### analysis.py
- `get_price_statistics()` - Estatísticas de preços
- `get_neighborhood_analysis()` - Análise por bairro
- `generate_executive_summary()` - Resumo executivo

**Exemplo de uso:**
```python
from src.data_cleaning import load_and_clean_data
from src.analysis import get_price_statistics

df = load_and_clean_data('data/raw/listings.csv.gz')
stats = get_price_statistics(df)
print(stats)

## Relatórios e Documentação

**Relatório Executivo:** [relatorio_airbnb_rio.txt](reports/relatorio_airbnb_rio.txt)
- Resumo executivo
- Descobertas principais  
- Top bairros por preço
- Recomendações estratégicas
- Próximos passos

## Como Executar

```bash
# Clone o repositório
git clone https://github.com/Matheus-Diniz-Silva/analise-airbnb-rio.git

# Instale as dependências
pip install -r requirements.txt

# Execute o Jupyter Notebook
jupyter notebook notebooks/01_eda_airbnb_rio.ipynb
