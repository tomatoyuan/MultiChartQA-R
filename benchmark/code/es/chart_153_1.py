# 图表1：关键词搜索笔记数据变化（柱状图 + 折线图双轴）

import matplotlib.pyplot as plt
import numpy as np

# 数据定义
categorias = ["Problemas de discusión sobre poros", "Total de temas de poros dilatados", "Cuidado de los poros"]
valores_antiguos = [43.65, 8.7, 0.16]
valores_nuevos = [79.06, 17.95, 0.39]
tasas_de_crecimiento = [81.12, 106.32, 143.75]

x = np.arange(len(categorias))
ancho = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras
barras1 = ax1.bar(x - ancho/2, valores_antiguos, ancho, label='2022/08 - 2023/07', color='#c5d9de')
barras2 = ax1.bar(x + ancho/2, valores_nuevos, ancho, label='2023/08 - 2024/07', color='#355c5c')
ax1.set_ylabel('Número de notas de búsqueda (en miles de unidades)')
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, fontsize=10)
ax1.legend(loc='upper right')

# Agregar valores en la parte superior de las barras
for barra in barras1 + barras2:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2, altura + 1, f'{altura:.2f}',
             ha='center', va='bottom', fontsize=9)

# Gráfico de líneas
ax2 = ax1.twinx()
ax2.plot(x, tasas_de_crecimiento, color='gray', marker='o', label='Tasa de crecimiento año tras año')
for i, tasa in enumerate(tasas_de_crecimiento):
    ax2.text(x[i], tasa + 3, f'{tasa:.2f}%', color='black', ha='center', fontsize=9)
ax2.set_ylabel('Tasa de crecimiento año tras año (%)')
ax2.set_ylim(0, 180)

# Título y mejora visual
plt.title("Figura 1.1 - 1 Datos de notas de búsqueda de palabras clave en Xiaohongshu (Fuente de datos: Feigua)")
plt.tight_layout()
plt.show()