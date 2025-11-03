
import pandas as pd
import numpy as np

def get_price_statistics(df):
    """
    Retorna estatísticas detalhadas de preços
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
        
    Returns:
        dict: Dicionário com estatísticas
    """
    return {
        'preco_medio': df['price_clean'].mean(),
        'preco_mediano': df['price_clean'].median(),
        'preco_minimo': df['price_clean'].min(),
        'preco_maximo': df['price_clean'].max(),
        'desvio_padrao': df['price_clean'].std(),
        'q1': df['price_clean'].quantile(0.25),
        'q3': df['price_clean'].quantile(0.75)
    }

def get_neighborhood_analysis(df, min_listings=50):
    """
    Análise detalhada por bairro
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
        min_listings (int): Mínimo de imóveis por bairro
        
    Returns:
        pandas.DataFrame: Análise por bairro
    """
    neighborhood_stats = df.groupby('neighbourhood_cleansed').agg({
        'price_clean': ['count', 'mean', 'median', 'std'],
        'review_scores_rating': 'mean',
        'number_of_reviews': 'mean'
    }).round(2)
    
    # Filtrar bairros com mínimo de imóveis
    neighborhood_stats = neighborhood_stats[neighborhood_stats[('price_clean', 'count')] >= min_listings]
    neighborhood_stats = neighborhood_stats.sort_values(('price_clean', 'mean'), ascending=False)
    
    return neighborhood_stats

def get_amenities_analysis(df):
    """
    Análise de comodidades mais comuns
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
        
    Returns:
        pandas.DataFrame: Análise de comodidades
    """
    amenities_interest = ['wifi', 'AC', 'parking', 'Pool', 'kitchen', 'heating']
    
    amenities_analysis = {}
    for amenity in amenities_interest:
        count = df['amenities'].str.contains(amenity, case=False, na=False).sum()
        percent = (count / len(df)) * 100
        amenities_analysis[amenity] = {
            'count': count,
            'percent': round(percent, 1)
        }
    
    return pd.DataFrame(amenities_analysis).T

def generate_executive_summary(df):
    """
    Gera resumo executivo da análise
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
        
    Returns:
        str: Resumo executivo formatado
    """
    stats = get_price_statistics(df)
    neighborhood_stats = get_neighborhood_analysis(df)
    
    summary = f"""
    RESUMO EXECUTIVO - AIRBNB RIO
    =============================
    Total de imóveis: {len(df):,}
    Preço médio: R$ {stats['preco_medio']:.2f}
    Preço mediano: R$ {stats['preco_mediano']:.2f}
    Bairro mais caro: {neighborhood_stats.index[0]} (R$ {neighborhood_stats[('price_clean', 'mean')].iloc[0]:.2f})
    Tipo predominante: {df['room_type'].value_counts().index[0]} ({df['room_type'].value_counts().iloc[0]:,} imóveis)
    """
    
    return summary
