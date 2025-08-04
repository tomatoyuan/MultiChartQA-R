import matplotlib.pyplot as plt
import numpy as np

# Razones para comprar productos agrícolas en línea
razones = [
    "Conveniente, ahorra tiempo y energía", "Mejor comprensión de los productos antes de la compra",
    "Amplia selección de productos", "Muchas actividades promocionales", "Bajo precio",
    "Puede comprar productos de otras regiones", "Calidad del producto garantizada",
    "Puede comprar productos fuera de temporada"
]
# Proporciones correspondientes (%)
proporciones = [41.29, 40.65, 40.00, 38.71, 38.71, 37.42, 32.90, 29.03]

x = np.arange(len(razones))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas, centradas encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(razones, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Razones por las que los consumidores chinos prefieren comprar productos agrícolas en línea en 2025')

plt.tight_layout()
plt.show()