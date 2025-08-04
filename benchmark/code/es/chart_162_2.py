import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# 数据
años = ["2020", "2021", "2022", "2023", "2024E"]
tamaño_total_mercado = [3557, 3986, 4306, 4990, 5680]
tamaño_mercado_b = [2774, 3109, 3359, 3980, 4630]
crecimiento_total = [None, 12.1, 8.0, 15.9, 13.8]
crecimiento_b = [None, 12.1, 8.0, 18.5, 16.3]

x = np.arange(len(años))
ancho = 0.35

fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras
barras1 = ax1.bar(x - ancho/2, tamaño_total_mercado, ancho, label='Tamaño del mercado (miles de millones de yuanes)', color='red')
barras2 = ax1.bar(x + ancho/2, tamaño_mercado_b, ancho, label='Tamaño del mercado B (miles de millones de yuanes)', color='blue')

# Agregar etiquetas a las barras
for barra in barras1:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2, altura + 50, f'{int(altura)}', ha='center', va='bottom', fontsize=9)
for barra in barras2:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2, altura + 50, f'{int(altura)}', ha='center', va='bottom', fontsize=9)

ax1.set_ylabel('Tamaño del mercado (miles de millones de yuanes)')
ax1.set_xticks(x)
ax1.set_xticklabels(años)

# Eje secundario: Variación interanual (%)
ax2 = ax1.twinx()
ax2.set_ylabel('Variación interanual (%)')
ax2.set_ylim(0, 20)  # Comenzar desde 0%
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

# Dibujar la línea solo a partir de 2021
x_crecimiento = x[1:]  # Corresponde a 2021 a 2024
crecimiento_total_limpio = [v for v in crecimiento_total if v is not None]
crecimiento_b_limpio = [v for v in crecimiento_b if v is not None]

linea1 = ax2.plot(x_crecimiento, crecimiento_total_limpio, color='orange', marker='o', label='Variación interanual (%)', linewidth=2)
linea2 = ax2.plot(x_crecimiento, crecimiento_b_limpio, color='gray', marker='o', label='Variación interanual B (%)', linewidth=2)

# Etiquetar los valores en la línea
for i, valor in enumerate(crecimiento_total_limpio):
    ax2.text(x_crecimiento[i], valor + 0.6, f'{valor}%', color='orange', ha='center', fontsize=9)
for i, valor in enumerate(crecimiento_b_limpio):
    ax2.text(x_crecimiento[i], valor + 0.6, f'{valor}%', color='gray', ha='center', fontsize=9)

# Leyenda
manejadores_etiquetas1 = ax1.get_legend_handles_labels()
manejadores_etiquetas2 = ax2.get_legend_handles_labels()
ax1.legend(manejadores_etiquetas1[0] + manejadores_etiquetas2[0], manejadores_etiquetas1[1] + manejadores_etiquetas2[1], loc='upper left')

plt.title('Tamaño del mercado de alimentos prefabricados en China y su variación interanual de 2020 a 2024')
plt.tight_layout()
plt.show()