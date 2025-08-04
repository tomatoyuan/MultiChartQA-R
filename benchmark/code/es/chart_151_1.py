import matplotlib.pyplot as plt
import numpy as np

# Gráfico 1: Tasa de crecimiento de FMCG en línea y sus categorías en MAT2406 (utilizando un gráfico de barras)
categorias = ['Ventas minoristas en línea', 'FMCG en línea', 'Alimentos', 'Maquillaje', 'Infantil']
tasa_de_crecimiento = [4.9, 7.8, 8.1, 5.8, 10.2]
colores = ['black', '#0056d6', 'white', 'white', 'white']
colores_borde = ['black', '#0056d6', '#0056d6', '#0056d6', '#0056d6']

fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(categorias, tasa_de_crecimiento, color=colores, edgecolor=colores_borde, linewidth=2)

# Agregar etiquetas de valores
for barra, valor in zip(barras, tasa_de_crecimiento):
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2, altura + 0.3, f'{valor}%', ha='center', va='bottom', fontsize=12)

# Establecer el título y la etiqueta del eje Y
ax.set_title('Tasa de crecimiento de FMCG en línea y sus categorías en MAT2406', fontsize=16)
ax.set_ylabel('Tasa de crecimiento interanual (%)')
ax.set_ylim(0, 12)
ax.set_facecolor('#f8f9fa')

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()