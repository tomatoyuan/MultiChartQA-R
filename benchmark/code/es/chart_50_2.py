import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Simular datos (consistentes con la tendencia del gráfico original)
años = np.arange(2013, 2025)
datos_pib = [4.4, 4.8, 5.1, 5.5, 6.1, 6.7, 7.1, 7.3, 8.3, 8.7, 9.2, 9.6]
datos_ingresos = [1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.1, 3.2, 3.5, 3.7, 3.9, 4.1]

# Calcular la TIR Compuesta Anual (simular una tasa de crecimiento cercana al gráfico original)
def cagr(inicio, fin, años):
    return ((fin / inicio) ** (1/años) - 1) * 100

tir_pib = cagr(datos_pib[0], datos_pib[-1], len(años)-1)
tir_ingresos = cagr(datos_ingresos[0], datos_ingresos[-1], len(años)-1)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de líneas
linea_pib, = ax.plot(años, datos_pib, color='#A8D268', marker='o', label='PIB per cápita en China (10,000 yuan)', linewidth=3)
linea_ingresos, = ax.plot(años, datos_ingresos, color='#59B9E1', marker='o', label='Ingreso disponible per cápita de los residentes nacionales (10,000 yuan)', linewidth=3)

# Agregar etiquetas de datos a las líneas
for x, y in zip(años, datos_pib):
    ax.annotate(f'{y}', 
                (x, y),
                textcoords="offset points",
                xytext=(0,10),  # Desplazamiento vertical
                ha='center',
                color='#86C232')

for x, y in zip(años, datos_ingresos):
    ax.annotate(f'{y}', 
                (x, y),
                textcoords="offset points",
                xytext=(0,-15),  # Desplazamiento vertical (valor negativo significa hacia abajo)
                ha='center',
                color='#2F9EBD')

# Agregar tarjetas indicadoras de TIR Compuesta Anual (etiquetas verdes/azules en la esquina superior izquierda) - ajustar tamaño y posición
ax.text(0.02, 0.92, 'TIR Compuesta Anual', fontsize=10, transform=ax.transAxes, color='white', ha='left', va='center', 
        bbox=dict(facecolor='#86C232', pad=3, edgecolor='none', boxstyle='round,pad=0.2'))
ax.text(0.08, 0.92, f'+{tir_pib:.1f}%', fontsize=10, color='#86C232', transform=ax.transAxes, ha='left', va='center')

ax.text(0.02, 0.85, 'TIR Compuesta Anual', fontsize=10, transform=ax.transAxes, color='white', ha='left', va='center', 
        bbox=dict(facecolor='#2F9EBD', pad=3, edgecolor='none', boxstyle='round,pad=0.2'))
ax.text(0.08, 0.85, f'+{tir_ingresos:.1f}%', fontsize=10, color='#2F9EBD', transform=ax.transAxes, ha='left', va='center')

# Configuración del gráfico
ax.set_title('PIB per cápita en China e ingreso disponible per cápita de los residentes nacionales de 2013 a 2024', fontsize=14, pad=30)
ax.set_xticks(años)
ax.set_ylim(0, 11)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.68), frameon=False)

plt.tight_layout()
plt.show()