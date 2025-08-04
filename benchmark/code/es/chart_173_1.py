import matplotlib.pyplot as plt
import numpy as np

# 数据
años = ['2021', '2022', '2023']
conteos_alta = [107, 336, 584]      # Número de registros de puesta en línea (eje izquierdo - gráfico de barras)
conteos_rodaje = [935, 3293, 3574]   # Número de registros de rodaje (eje derecho - gráfico de líneas)

x = np.arange(len(años))
ancho_barra = 0.5

# Crear la figura principal y ejes dobles
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()  # Crear el eje derecho

# Gráfico de barras (eje izquierdo): Número de registros de puesta en línea
barras = ax1.bar(x, conteos_alta, width=ancho_barra, color='#ff2d55', label='Número de registros de puesta en línea')

# Agregar números en la parte superior de las barras
for i, val in enumerate(conteos_alta):
    ax1.text(x[i], val - 10, str(val), ha='center', fontsize=10, color='black')

# Gráfico de líneas (eje derecho): Número de registros de rodaje
ax2.plot(x, conteos_rodaje, color='#586173', linewidth=2.5, marker='o', markersize=25, label='Número de registros de rodaje', zorder=5)

# Etiquetar los puntos de la línea
for i, val in enumerate(conteos_rodaje):
    ax2.text(x[i], val, str(val), ha='center', va='center', fontsize=10, color='white', zorder=6)

# Configuración de los ejes y etiquetas
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=11)
ax1.set_ylabel('Número de registros de puesta en línea', fontsize=12, color='#ff2d55')
ax2.set_ylabel('Número de registros de rodaje', fontsize=12, color='#586173')

ax1.set_ylim(0, 700)      # Eje izquierdo del gráfico de barras
ax2.set_ylim(0, 4000)     # Eje derecho del gráfico de líneas

# Título del gráfico


# Leyenda (combinar las leyendas de las dos capas)
lineas1, etiquetas1 = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
fig.legend(lineas1 + lineas2, etiquetas1 + etiquetas2, loc='lower right', fontsize=10)

# Cuadrícula y estilo
ax1.yaxis.grid(True, linestyle='--', alpha=0.3)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['left'].set_visible(True)
ax2.spines['right'].set_visible(True)

plt.title('2021-2023 Número de registros de micro \nnovelas cortas de la Administración de Radio, Televisión y Cine', fontsize=14, fontweight='bold', loc='left')

# Fuente de los datos
fig.text(0.01, -0.1, 'Fuente de datos: Administración Nacional de Radio, Televisión y Cine', fontsize=9, ha='left')

plt.tight_layout(rect=[0, 0.03, 1, 1])
plt.show()