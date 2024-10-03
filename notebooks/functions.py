
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

def remove_null_values(df):
    """Elimina filas con valores nulos en cualquier columna."""
    return df.dropna()

def round_and_convert_age(df):
    """Redondea y convierte la columna de edad a enteros."""
    df['clnt_age'] = df['clnt_age'].round(0).astype(int)
    return df

def rename_variation_column(df):
    """Renombra la columna 'Variation' a 'variation'."""
    return df.rename(columns={'Variation': 'variation'})

def calculate_metrics(df):
    """Calcula métricas de tendencia central para la edad y antigüedad."""
    metrics = df.agg({
        'clnt_age': ['mean', 'median', 'min', 'max'],
        'clnt_tenure_yr': ['mean', 'median', 'min', 'max']
    })
    return metrics

def plot_age_distribution(df):
    """Grafica la distribución de la edad de los clientes."""
    plt.figure(figsize=(10, 6))
    df['clnt_age'].hist(bins=20, color='skyblue')
    plt.title('Distribución de la Edad de los Clientes')
    plt.xlabel('Edad')
    plt.ylabel('Número de Clientes')
    plt.show()

def plot_tenure_distribution(df):
    """Grafica la distribución de la antigüedad de los clientes."""
    plt.figure(figsize=(10, 6))
    df['clnt_tenure_yr'].hist(bins=35, color='lightgreen')
    plt.title('Distribución de la Antigüedad de los Clientes (en años)')
    plt.xlabel('Años de Antigüedad')
    plt.ylabel('Número de Clientes')
    plt.show()

def create_age_boxplot(df):
    """Crea un boxplot para la distribución de la edad de los clientes."""
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['clnt_age'].dropna(), vert=False, patch_artist=True)
    plt.title('Diagrama de Caja y Bigotes: Edad de los Clientes')
    plt.xlabel('Edad')
    plt.show()

def create_tenure_boxplot(df):
    """Crea un boxplot para la distribución de la antigüedad de los clientes."""
    plt.figure(figsize=(10, 6))
    plt.boxplot(df['clnt_tenure_yr'].dropna(), vert=False, patch_artist=True)
    plt.title('Diagrama de Caja y Bigotes: Antigüedad de los Clientes')
    plt.xlabel('Años de Antigüedad')
    plt.show()