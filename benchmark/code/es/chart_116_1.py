import matplotlib.pyplot as plt
import numpy as np

# Canales de compra
canales = [
    "Compra en grupo en la comunidad o compra en grupo en grupos de WeChat", "Supermercado", "Mercado de agricultores", "Compra directa de agricultores o en los campos",
    "Mercado mayorista agrícola", "Comercio electrónico en directo o compra en plataformas de videos cortos", "Tiendas especializadas (como supermercados de alimentos frescos, fruterías, tiendas especializadas en productos agrícolas, etc.)",
    "Plataformas de servicios de vida local (como Meituan, Ele.me, MissFresh, etc.)", "Plataformas de comercio electrónico (como Pinduoduo, Tmall, JD.com, Suning.com, etc.)"
]
# Proporciones correspondientes (%)
proporciones = [21.97, 22.78, 23.42, 23.75, 26.33, 27.30, 35.70, 36.35, 41.03]

y = np.arange(len(canales))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(12, 8))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas a la derecha de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(canales)
ax.set_xlabel('Proporción (%)')
ax.set_title('Canales de compra de productos agrícolas por los consumidores chinos en 2025')

plt.tight_layout()
plt.show()