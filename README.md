Análise do Mercado Airbnb - Rio de Janeiro
Sobre o Projeto

Análise exploratória completa do mercado de aluguel por temporada no Rio de Janeiro através da plataforma Airbnb. Este projeto investiga os fatores que influenciam os preços de diárias e fornece insights baseados em dados para anfitriões e viajantes.

Este trabalho faz parte do portfólio de projetos em Ciência de Dados, com foco em análise de negócios e tomada de decisão orientada por dados.
Objetivos

    Identificar os principais fatores que impactam o preço das diárias

    Analisar a distribuição geográfica dos imóveis e preços

    Descobrir padrões de precificação por tipo de imóvel e localização

    Fornecer recomendações baseadas em dados para precificação estratégica

    Identificar oportunidades de mercado para novos anfitriões

Tecnologias Utilizadas

    Python 3.9+

    Pandas - Manipulação e análise de dados

    NumPy - Computação numérica

    Matplotlib/Seaborn - Visualizações e gráficos

    Jupyter Notebook - Análise interativa e documentação

    Google Colab - Ambiente de desenvolvimento

Estrutura do Projeto
text

analise-airbnb-rio/
├── data/
│   ├── raw/           # Dataset original do Inside Airbnb
│   └── processed/     # Dados tratados e limpos
├── notebooks/
│   └── 01_eda_airbnb_rio.ipynb  # Análise exploratória completa
├── src/               # Scripts Python para processamento
├── reports/           # Relatórios e documentação
├── images/            # Gráficos e visualizações
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação principal

Metodologia
Coleta de Dados

    Fonte: Inside Airbnb (dados públicos de junho 2025)

    Dataset: listings.csv.gz com 42.572 imóveis e 79 colunas

    Período: Dados mais recentes disponíveis

Processamento e Limpeza

    Conversão de formatos de preço (string para numérico)

    Tratamento de valores missing e outliers

    Criação de variáveis derivadas

    Filtragem e validação de dados

Análise Realizada

    Análise Descritiva: Estatísticas básicas e distribuições

    Análise Geográfica: Preços por bairro e localização

    Análise de Segmentação: Tipos de imóvel e comodidades

    Análise de Performance: Avaliações e superhosts

    Identificação de Outliers: Valores atípicos no mercado

Resultados e Insights
Características do Mercado

    Total de imóveis: 42.572 anúncios ativos

    Preço médio: R$ 688,01

    Preço mediano: R$ 311,00

    Faixa de preço predominante: R$ 200 - R$ 558 (25º-75º percentil)

Distribuição por Tipo de Imóvel

    Casas/Apartamentos inteiros: 33.990 imóveis (79,8%) - Preço médio: R$ 762

    Quartos privados: 8.152 imóveis (19,1%) - Preço médio: R$ 392

    Quartos compartilhados: 407 imóveis (1,0%) - Preço médio: R$ 194

    Quartos de hotel: 23 imóveis (0,1%) - Preço médio: R$ 610

Top Bairros por Valor

    Joá: Média R$ 6.186 | Mediana R$ 5.000 (155 imóveis)

    São Conrado: Média R$ 2.548 | Mediana R$ 754 (364 imóveis)

    Itanhangá: Média R$ 2.457 | Mediana R$ 352 (179 imóveis)

    Lagoa: Média R$ 1.350 | Mediana R$ 630 (264 imóveis)

    Gávea: Média R$ 1.044 | Mediana R$ 450 (220 imóveis)

Fatores de Influência no Preço

    Capacidade: Média de 3,9 pessoas por imóvel

    Quartos: 58% dos imóveis possuem 1 quarto

    Comodidades essenciais:

        Wi-Fi: 95,9% dos imóveis

        Ar condicionado: 75,1% dos imóveis

        Estacionamento: 59,2% dos imóveis

        Piscina: 24,0% dos imóveis

Desempenho e Qualidade

    Nota média: 4,81/5,0

    Superhosts: 32,7% dos anfitriões

    Reviews/mês: Média de 1,20 avaliações

Insights Estratégicos
Para Anfitriões

    Precificação: Focar na mediana de R$ 311 como referência, não na média distorcida por outliers

    Comodidades: Wi-Fi e ar condicionado são considerados essenciais pelo mercado

    Localização: Bairros menos saturados oferecem melhor custo-benefício

    Certificação: Buscar status de Superhost aumenta visibilidade e credibilidade

Para o Mercado

    Bifurcação: Grande discrepância entre preço médio e mediano indica mercado segmentado

    Concentração: Copacabana representa 31% de toda a oferta

    Luxo concentrado: Bairros como Joá têm preços 20x superiores à mediana

    Padronização: Tipologia dominante de apartamentos/casas inteiras (80%)

Como Executar o Projeto
Pré-requisitos
bash

Python 3.9+
Jupyter Notebook ou Google Colab

Instalação

    Clone o repositório:

bash

git clone https://github.com/seu-usuario/analise-airbnb-rio.git
cd analise-airbnb-rio

    Instale as dependências:

bash

pip install -r requirements.txt

    Execute a análise:

bash

jupyter notebook notebooks/01_eda_airbnb_rio.ipynb

Execução no Google Colab

    Faça upload do arquivo listings.csv.gz para o Colab

    Execute o notebook célula por célula

    Os dados serão processados automaticamente

Próximas Etapas

    Análise de Sazonalidade: Variação de preços por período do ano

    Dashboard Interativo: Visualizações dinâmicas com Power BI/Tableau

    Modelo Preditivo: Previsão de preços baseada em características dos imóveis

    Análise de Concorrência: Benchmarking por bairro e tipo de imóvel

Limitações

    Dados limitados ao snapshot específico do Inside Airbnb

    Variáveis qualitativas como descrições não foram analisadas em profundidade

    Análise temporal limitada aos dados disponíveis

Contato

Matheus Diniz Silva
Email: matheus.dinizbrito@gmail.com
LinkedIn: https://www.linkedin.com/in/matheusdinizsilva/
Licença

Este projeto é para fins educacionais e de portfólio. Os dados são provenientes do Inside Airbnb e estão disponíveis publicamente.

Nota: Este projeto demonstra habilidades em análise exploratória de dados, limpeza e processamento de datasets complexos, e geração de insights acionáveis para negócios.
