
import pandas as pd
from functions import (
    remove_null_values, round_and_convert_age, rename_variation_column,
    calculate_metrics, plot_age_distribution, plot_tenure_distribution,
    create_age_boxplot, create_tenure_boxplot, perform_t_test
)

# Supongamos que ya tienes cargado el DataFrame df_combined

# Eliminar filas con valores nulos
df_combined = remove_null_values(df_combined)

# Redondear y convertir la columna de edad
df_combined = round_and_convert_age(df_combined)

# Renombrar la columna 'Variation'
df_combined = rename_variation_column(df_combined)

# Calcular métricas de tendencia central
metrics = calculate_metrics(df_combined)
print("Métricas de edad y antigüedad:")
print(metrics)

# Graficar la distribución de la edad
plot_age_distribution(df_combined)

# Graficar la distribución de la antigüedad
plot_tenure_distribution(df_combined)

# Crear el boxplot para la edad
create_age_boxplot(df_combined)

# Crear el boxplot para la antigüedad
create_tenure_boxplot(df_combined)

# Realizar una prueba T (necesitas definir count_test, nobs_test, count_control y nobs_control antes)
t_stat, p_value = perform_t_test(count_test, nobs_test, count_control, nobs_control)
print(f"Estadístico t: {t_stat}")
print(f"Valor p: {p_value}")
