import matplotlib.pyplot as plt
import numpy as np

# 数据
categorias = ['Cuidado de la piel', 'Maquillaje', 'Cuidado personal', 'Perfumes']
tamaño_del_mercado = [4823.5, 1700.9, 1193.5, 254]
tasa_de_crecimiento = [0.1, 13.5, 15.8, 11.4]

x = np.arange(len(categorias))
ancho = 0.4

fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras: Tamaño del mercado
barras = ax1.bar(x, tamaño_del_mercado, ancho, color='#FFB6C1', label='Tamaño del mercado (miles de millones de yuanes)')
ax1.set_ylabel('Tamaño del mercado (miles de millones de yuanes)')
ax1.set_xticks(x)
ax1.set_xticklabels(categorias)
ax1.bar_label(barras, fmt='%.1f', label_type='edge', fontsize=10, color='crimson')
ax1.set_ylim(0, 5500)

# Gráfico de línea: Tasa de crecimiento año tras año
ax2 = ax1.twinx()
linea = ax2.plot(x, tasa_de_crecimiento, color='gray', marker='o', label='Tasa de crecimiento año tras año del tamaño del mercado', linewidth=2)
ax2.set_ylabel('Tasa de crecimiento año tras año (%)')
for i, val in enumerate(tasa_de_crecimiento):
    ax2.text(x[i], val + 0.8, f'{val:.1f}%', ha='center', fontsize=10, weight='bold')
ax2.set_ylim(0, 20)

# Establecer el título y aumentar el espaciado para evitar superposiciones
plt.title('Tamaño del mercado de cada categoría principal en 2023', fontsize=14, pad=20)

# Combinar las leyendas
handles = list(barras)[:1] + linea  # Solo tomar una barra como representante + la línea
etiquetas = ['Tamaño del mercado (miles de millones de yuanes)', 'Tasa de crecimiento año tras año del tamaño del mercado']
ax1.legend(handles, etiquetas, loc='upper right', fontsize=10)

# Agregar la fuente de los datos
plt.figtext(0.01, -0.05, 'Fuente de datos: CBNData', fontsize=10, ha='left')

plt.tight_layout()
plt.show()