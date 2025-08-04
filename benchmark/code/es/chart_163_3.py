import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import cm

# 数据
años = list(range(2012, 2023))
porcentaje_pib = [55, 54, 56, 56, 44, 42, 42, 40, 40, 40, 41]

# Degradado de colores (de rojo claro a rojo oscuro)
colores = cm.Reds(np.linspace(0.3, 0.8, len(porcentaje_pib)))

# Dibujo del gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(años, porcentaje_pib, color=colores, edgecolor='black')

# Añadir etiquetas de valores
for barra, valor in zip(barras, porcentaje_pib):
    ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.8,
            f'{valor}%', ha='center', va='bottom', fontsize=11)

# Título y etiquetas
ax.set_title("Tamaño de la economía rural y proporción del PIB nacional (2012–2022)", fontsize=15)
ax.set_ylabel("Proporción (%)", fontsize=12)
ax.set_xticks(años)
ax.set_ylim(0, 60)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()