import matplotlib.pyplot as plt
import numpy as np

# 数据
años = ['2020', '2021', '2022', '2023']
venta_minorista_total = [390000, 440000, 440000, 470000]  # Volumen total de ventas minoristas de consumo social (en millones de yuanes)
venta_minorista_online = [110000, 120000, 120000, 130000]  # Volumen de ventas minoristas de bienes físicos en línea (en millones de yuanes)
crecimiento_total = [-0.04, 0.12, 0.00, 0.07]  # Tasa de crecimiento año tras año
crecimiento_online = [0.14, 0.11, 0.11, 0.08]

x = np.arange(len(años))
ancho = 0.35

# Crear la figura
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

# Gráfico de barras
bar1 = ax1.bar(x - ancho/2, venta_minorista_total, ancho,
               label='Volumen total de ventas minoristas de consumo social\n (en millones de yuanes)', color='#e55322')
bar2 = ax1.bar(x + ancho/2, venta_minorista_online, ancho, label='Volumen de ventas minoristas de bienes físicos en línea \n(en millones de yuanes)', color='lightgray')

# Anotar los datos del gráfico de barras
for i, rect in enumerate(bar1):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, altura + 1000, f'{altura}', ha='center', va='bottom', fontsize=9)

for i, rect in enumerate(bar2):
    altura = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width()/2, altura + 1000, f'{altura}', ha='center', va='bottom', fontsize=9)

# Gráfico de línea
line1 = ax2.plot(x, crecimiento_total, label='Tasa de crecimiento año tras año del volumen \ntotal de ventas minoristas de consumo social', color='black', marker='o', linewidth=2)
line2 = ax2.plot(x, crecimiento_online, label='Tasa de crecimiento año tras año del volumen \nde ventas minoristas de bienes físicos en línea', color='#7f3f1d', marker='o', linewidth=2)

# Anotar las tasas de crecimiento
for i, v in enumerate(crecimiento_total):
    ax2.text(x[i] + 0.1, v, f'{int(v * 100)}%', ha='center', va='bottom', fontsize=10)

for i, v in enumerate(crecimiento_online):
    ax2.text(x[i] - 0.1, v - 0.01, f'{int(v * 100)}%', ha='center', va='bottom', fontsize=10)

# Ejes y leyendas
ax1.set_ylabel('Volumen (en millones de yuanes)', fontsize=12)
ax2.set_ylabel('Tasa de crecimiento año tras año', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=11)
plt.title('Volumen actual del total de ventas minoristas de consumo social y del volumen de \nventas minoristas de bienes físicos en línea (en millones de yuanes)', fontsize=14, pad=20)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=2, frameon=False, fontsize=10)

# Cuadrícula y fondo
ax1.yaxis.grid(True, linestyle='--', alpha=0.4)
ax2.set_ylim(-0.05, 0.20)
ax1.set_facecolor('white')

# Fuente de los datos (usar fig.text para colocarla fuera en la parte inferior)
fig.text(0.01, 0.01, 'Fuente de datos: Instituto Nacional de Estadísticas. Dibujado por el Centro de Contenidos de Youmiyun', ha='left', va='bottom', fontsize=9)

plt.tight_layout(rect=[0, 0.03, 1, 1])  # Dejar espacio para el texto inferior
plt.show()