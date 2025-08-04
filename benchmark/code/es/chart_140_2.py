import matplotlib.pyplot as plt
import numpy as np

# Datos
factores = ["Rango máximo de crucero", "Tiempo de carga requerido", "Seguridad del vehículo", 
            "Precio de los vehículos de energía nueva", "Rendimiento de ahorro de energía y reducción de emisiones", 
            "Subsidios estatales", "Apariencia de los vehículos de energía nueva", 
            "Estrategias de promoción de las empresas automotrices", "Seguir la moda"]
porcentajes = [51.3, 46.2, 46.0, 45.1, 38.2, 35.7, 34.8, 22.9, 17.4]

x = np.arange(len(factores))

fig, ax = plt.subplots(figsize=(12, 7))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange')

# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Porcentaje (%)')
ax.set_xlabel('Factores de compra')
ax.set_xticks(x)
ax.set_xticklabels(factores, rotation=15, ha='right')
ax.set_title('Análisis de los factores de compra de usuarios de vehículos de energía nueva en China en 2023')

plt.tight_layout()
plt.show()