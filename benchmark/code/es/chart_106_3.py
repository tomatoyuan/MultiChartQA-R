import matplotlib.pyplot as plt
import numpy as np

# Nombres de las marcas
marcas = ["Agua Mineral Nongfu Spring", "Agua Mineral Wahaha", "Agua Mineral C'estbon", "Agua Mineral Ganten", "Agua Mineral Master Kong", 
          "Agua Mineral Gingkgo Spring", "Agua Mineral con Gas Coca - Cola", "Agua Mineral Kunlun Mountains", "Agua Mineral Ice Dew", "Agua Mineral Evergrande Spring", 
          "Agua Mineral French Evian", "San Pellegrino", "Poland Spring"]
# Proporciones correspondientes (%)
proporciones = [48.53, 45.04, 36.73, 35.66, 29.49, 
               22.79, 22.25, 20.38, 20.11, 18.23, 
               14.75, 11.80, 10.72]

x = np.arange(len(marcas))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(marcas, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Marcas de agua embotellada más frecuentemente compradas por los consumidores chinos en 2025')

plt.tight_layout()
plt.show()