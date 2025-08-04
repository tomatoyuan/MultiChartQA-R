import matplotlib.pyplot as plt
import numpy as np

# Rangos de edad
edades = ["Generación 00", "Generación 95", "Generación 90", "Generación 85", "Generación 80", "Generación 75", "Generación 70", "Antes de los 70"]
# Proporción de la población que regala en general (gráfico de barras)
porcentaje_regalo_total = [11, 17, 25, 18, 15, 8, 7, 4]
# TGI de regalos de salud (gráfico de línea)
tgi_regalo_salud = [105, 90, 101, 106, 103, 99, 97, 93]

x = np.arange(len(edades))
ancho = 0.6

fig, ax1 = plt.subplots(figsize=(10, 6))

# Gráfico de barras (eje izquierdo)
barras = ax1.bar(x, porcentaje_regalo_total, width=ancho, color='lightcoral', label='Población que regala en general')
ax1.set_ylabel('Proporción de la población que regala en general', fontsize=12)
ax1.set_ylim(0, 30)
ax1.set_xticks(x)
ax1.set_xticklabels(edades, fontsize=10)
for barra in barras:
    altura = barra.get_height()
    ax1.annotate(f'{altura}%', xy=(barra.get_x() + barra.get_width() / 2, altura),
                 xytext=(0, 3), textcoords="offset points", ha='center', fontsize=10)

# Gráfico de línea (eje derecho)
ax2 = ax1.twinx()
linea, = ax2.plot(x, tgi_regalo_salud, color='firebrick', marker='o', label='TGI de regalos de salud')
ax2.set_ylabel('TGI de regalos de salud', fontsize=12)
ax2.set_ylim(80, 110)
for i, v in enumerate(tgi_regalo_salud):
    ax2.text(x[i], v + 1, str(v), color='firebrick', ha='center', fontsize=10)

# Combinar leyendas (forma de arreglarlo)
manejadores1, etiquetas1 = ax1.get_legend_handles_labels()
manejadores2, etiquetas2 = ax2.get_legend_handles_labels()
fig.legend(manejadores1 + manejadores2, etiquetas1 + etiquetas2, loc='upper right', fontsize=10)

# Título y diseño
fig.suptitle('Distribución generacional de la población \nque regala en el Año Nuevo', fontsize=14, fontweight='bold', ha='right')
fig.tight_layout()
plt.show()