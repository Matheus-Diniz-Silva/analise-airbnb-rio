
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def setup_plot_style():
    """Configura o estilo padrão dos gráficos"""
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 8)

def plot_price_distribution(df, max_price=None):
    """
    Plota distribuição de preços
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
        max_price (float): Preço máximo para visualização
    """
    setup_plot_style()
    
    data_to_plot = df.copy()
    if max_price:
        data_to_plot = data_to_plot[data_to_plot['price_clean'] <= max_price]
    
    plt.figure(figsize=(10, 6))
    plt.hist(data_to_plot['price_clean'], bins=50, edgecolor='black', alpha=0.7)
    plt.title('Distribuição de Preços - Airbnb Rio')
    plt.xlabel('Preço (R$)')
    plt.ylabel('Frequência')
    plt.grid(True, alpha=0.3)
    plt.show()

def plot_room_type_analysis(df):
    """
    Análise visual por tipo de imóvel
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
    """
    setup_plot_style()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Quantidade por tipo
    room_type_counts = df['room_type'].value_counts()
    room_type_counts.plot(kind='bar', ax=ax1, color='skyblue')
    ax1.set_title('Quantidade por Tipo de Imóvel')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
    
    # Preço médio por tipo
    price_by_room = df.groupby('room_type')['price_clean'].mean().sort_values(ascending=False)
    price_by_room.plot(kind='bar', ax=ax2, color='lightgreen')
    ax2.set_title('Preço Médio por Tipo de Imóvel')
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
    
    plt.tight_layout()
    plt.show()

def plot_geographic_prices(df):
    """
    Mapa geográfico de preços
    
    Args:
        df (pandas.DataFrame): DataFrame com dados
    """
    setup_plot_style()
    
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df['longitude'], df['latitude'], 
                         c=df['price_clean'], 
                         cmap='viridis', 
                         alpha=0.6, 
                         s=10)
    plt.colorbar(scatter, label='Preço (R$)')
    plt.title('Distribuição Geográfica dos Preços - Rio de Janeiro')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.show()
