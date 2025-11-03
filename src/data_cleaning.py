
import pandas as pd
import numpy as np

def load_and_clean_data(file_path):
    """
    Carrega e limpa os dados do Airbnb
    
    Args:
        file_path (str): Caminho para o arquivo CSV
        
    Returns:
        pandas.DataFrame: DataFrame limpo e processado
    """
    # Carregar dados
    df = pd.read_csv(file_path, compression='gzip')
    
    # Converter preço para numérico
    df['price_clean'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    
    # Criar categorias de preço
    bins = [0, 141, 311, 558, 1080, 1800, 6130, float('inf')]
    labels = ['Muito Baixo', 'Baixo', 'Médio-Baixo', 'Médio', 'Médio-Alto', 'Alto', 'Muito Alto']
    df['price_category'] = pd.cut(df['price_clean'], bins=bins, labels=labels)
    
    # Simplificar tipos de imóvel
    df['room_type_simple'] = df['room_type'].replace({
        'Entire home/apt': 'Casa/Apto Inteiro',
        'Private room': 'Quarto Privado', 
        'Shared room': 'Quarto Compartilhado',
        'Hotel room': 'Quarto de Hotel'
    })
    
    return df

def get_missing_data_summary(df):
    """
    Retorna resumo de dados missing
    
    Args:
        df (pandas.DataFrame): DataFrame para análise
        
    Returns:
        pandas.DataFrame: Resumo de dados missing
    """
    missing_data = df.isnull().sum()
    missing_percent = (missing_data / len(df)) * 100
    
    missing_info = pd.DataFrame({
        'Coluna': df.columns,
        'Missing': missing_data,
        'Percentual (%)': missing_percent
    })
    
    return missing_info[missing_info['Missing'] > 0].sort_values('Missing', ascending=False)

def remove_price_outliers(df, max_percentile=0.95):
    """
    Remove outliers extremos de preço
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
        max_percentile (float): Percentil máximo para considerar (default: 0.95)
        
    Returns:
        pandas.DataFrame: DataFrame sem outliers extremos
    """
    price_threshold = df['price_clean'].quantile(max_percentile)
    return df[df['price_clean'] <= price_threshold].copy()
