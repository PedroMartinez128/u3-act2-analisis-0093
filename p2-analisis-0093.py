import pandas as pd
import numpy as np

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
Agrupado = df.groupby("Tipo_Motor")
print(Agrupado)
print("\n-+-+-+ Autonomía promedio (en km) para cada tipo de motor-+-+-")
# Autonomía promedio (en km) para cada tipo de motor
print(Agrupado['Autonomia_Km'].mean())
print("\n-+-+-+ Precio máximo (en USD) registrado para cada tipo de motor-+-+-")
# Precio máximo (en USD) registrado para cada tipo de motor
print(Agrupado['Precio_USD'].max())