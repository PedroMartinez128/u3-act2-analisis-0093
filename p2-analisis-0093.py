import pandas as pd
import numpy as np

# Pedro Martinez NC. 0093
print("\n---- Analisis de datos de Vehiculo Pedro Martinez NC. 0093----")
vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Hibrido", "Diesel", "Diesel", "Electrico", "Gasolina"],
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}
df = pd.DataFrame(vehiculos)
print(df)

print("\n -+-+-Agrupar por una sola columna-+-+-+")
agrupado = df.groupby("Tipo_Motor")
print(agrupado)

print("\n-+-+-+ Autonomía promedio (en km) para cada tipo de motor-+-+-")
# Autonomía promedio (en km) para cada tipo de motor
print(agrupado['Autonomia_Km'].mean())

print("\n-+-+-+ Precio máximo (en USD) registrado para cada tipo de motor-+-+-")
# Precio máximo (en USD) registrado para cada tipo de motor
print(agrupado['Precio_USD'].max())

print("\n +-+Pedro Martinez-+-Segunda parte +-+-+0093-+-+-")
print("\n +-+-+ Agregar Resultados +-+-+")
print("mean --> promedio, sum --> suma")
print("max --> maximo, min --> minimo")
resultado_agregado = agrupado['Precio_USD'].agg(['mean', 'sum', 'max', 'min'])
print(resultado_agregado)

print("\n-+-+-+ Agrupar por múltiples columnas (Tipo_Motor y Equipo)-+-+-")
print("agrega columnas al dataframe")
print("Columna de Team (Equipo) A,B")
df['Equipo'] = ['A', 'B', 'A', 'B', 'A', 'B']

# Agrupar por Tipo_Motor y Equipo calculando el promedio del Precio_USD
agrupado_multiple = df.groupby(['Tipo_Motor', 'Equipo'])['Precio_USD'].mean()
print(agrupado_multiple)
