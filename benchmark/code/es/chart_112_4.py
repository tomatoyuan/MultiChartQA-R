import matplotlib.pyplot as plt
import numpy as np

# Canales para obtener información sobre figuras coleccionables
canales = ["Plataformas de pago", "Recomendaciones de familiares y amigos", "Plataformas de videos cortos (Douyin, Kuaishou, etc.)",
           "Plataformas de compartición de contenido (Xiaohongshu, Weibo, Douban, Zhihu, etc.)", "Plataformas de compartición de videos (Bilibili, Tencent Video, etc.)"]
# Proporciones correspondientes (%)
proporciones = [24.31, 28.94, 41.20, 50.23, 52.55]

y = np.arange(len(canales))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(canales)
ax.set_xlabel('Proporción (%)')
ax.set_title('Canales por los que los consumidores chinos de figuras coleccionables obtienen información sobre figuras en 2025')

plt.tight_layout()
plt.show()