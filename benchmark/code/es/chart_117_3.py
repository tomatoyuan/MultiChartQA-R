import matplotlib.pyplot as plt
import numpy as np

# Canales de compra
canales = [
    "Mercado profesional de mobiliario doméstico/ciudad de mobiliario doméstico", "Tiendas exclusivas de marca", "Compra en línea",
    "Recomendación o transferencia de amigos/familia", "Organizado por diseñadores u otros",
    "Feria de mobiliario doméstico", "Mercado de segunda mano/plataforma de comercio de objetos en desuso", "Centros comerciales", "Recogida en fábrica"
]
# Proporciones correspondientes (%)
proporciones = [37.70, 36.98, 35.19, 34.29, 33.57, 32.14, 28.19, 28.19, 24.24]

x = np.arange(len(canales))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas, centradas por encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center', va='center', fontsize=9)

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(canales, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Formas en que los consumidores chinos compran productos de mobiliario de decoración rígida en 2025')

plt.tight_layout()
plt.show()