import matplotlib.pyplot as plt
import numpy as np

# Gráfico 3: Desempeño del tamaño del mercado de la industria del comercio electrónico farmacéutico de 2018 a 2023

años = ['2018', '2019', '2020', '2021', '2022', '2023']
ventas = [700, 950, 1500, 1850, 2500, 2900]  # Unidad: miles de millones de yuanes
tasa_de_crecimiento = [55, 45, 35, 30, 29, 15]  # Unidad: %

fig, ax1 = plt.subplots(figsize=(10, 6))

# Eje principal - Gráfico de barras (tamaño de las ventas)
barras = ax1.bar(años, ventas, color='#fdbf6f', label='Tamaño de las ventas (miles de millones de yuanes)', width=0.6)
ax1.set_ylabel('Tamaño de las ventas (miles de millones de yuanes)', fontsize=12)
ax1.set_ylim(0, 3500)

# Agregar etiquetas de valores a las barras
for barra in barras:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2, altura + 80, f'{int(altura)}', ha='center', va='bottom', fontsize=10)

# Eje secundario - Gráfico de línea (tasa de crecimiento año tras año)
ax2 = ax1.twinx()
ax2.plot(años, tasa_de_crecimiento, color='brown', marker='o', linewidth=2.5, label='Tasa de crecimiento año tras año')
ax2.set_ylabel('Tasa de crecimiento año tras año (%)', fontsize=12)
ax2.set_ylim(0, 65)

# Agregar etiquetas de datos al gráfico de línea
for x, y in zip(años, tasa_de_crecimiento):
    ax2.text(x, y + 2, f'{y:.1f}%', ha='center', fontsize=10)

# Título y leyenda
plt.title('Desempeño del tamaño del mercado de la industria\n del comercio electrónico farmacéutico de 2018 a 2023', fontsize=14, weight='bold')
handles_labels = [ax.get_legend_handles_labels() for ax in [ax1, ax2]]
handles, labels = [sum(lol, []) for lol in zip(*handles_labels)]
ax1.legend(handles, labels, loc='upper left')

plt.tight_layout()
plt.show()