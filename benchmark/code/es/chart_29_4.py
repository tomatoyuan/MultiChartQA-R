import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Datos de calor de búsqueda por hora (unidad: diez mil)
horas = list(range(25))  # 0 - 24 horas
datos_calor = [
    1100, 1100, 1100, 1100, 1100,  # 0 - 4 horas
    1500, 2000, 2800, 3200, 2800,  # 5 - 9 horas
    2300, 2000, 1800, 2200, 2700,  # 10 - 14 horas
    3000, 3100, 2800, 2200, 1600,  # 15 - 19 horas
    1200, 1250, 1320, 1200, 1100   # 20 - 24 horas
]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(14, 7), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Utilizar interpolación de spline cúbica para generar una curva suave
x_suave = np.linspace(min(horas), max(horas), 500)
spl = make_interp_spline(horas, datos_calor, k=3)
calor_suave = spl(x_suave)

# Trazar la curva suave y agregar relleno de color degradado
line, = ax.plot(x_suave, calor_suave, linestyle='-', color='#1a73e8', linewidth=3)
ax.fill_between(x_suave, calor_suave, 0, alpha=0.1, color='#1a73e8')

# Agregar líneas horizontales de referencia y optimizar el estilo de la línea
ax.axhline(y=1100, color='#9aa0a6', linestyle='--', alpha=0.7, linewidth=1.5)
ax.axhline(y=3300, color='#9aa0a6', linestyle='--', alpha=0.7, linewidth=1.5)

# Agregar título y etiquetas, optimizar la fuente y la posición
ax.set_title('Gráfico de tendencia de 24 horas del calor de búsqueda de la Copa del Mundo', fontsize=18, pad=20, fontweight='bold', color='#202124')
ax.set_xlabel('Tiempo (horas)', fontsize=14, labelpad=10, color='#3c4043')
ax.set_ylabel('Calor de búsqueda (diez mil)', fontsize=14, labelpad=10, color='#3c4043')

# Establecer las marcas del eje x y optimizar el formato de visualización
ax.set_xticks(horas[::4])
ax.set_xticklabels([f'{h}h' for h in horas[::4]], fontsize=12)
ax.set_xlim(0, 24)
ax.set_ylim(0, 4000)

# Establecer las marcas del eje y y optimizar el formato de visualización
ax.set_yticks(np.arange(0, 4500, 500))
ax.set_yticklabels([f'{y}' for y in np.arange(0, 4500, 500)], fontsize=12)

# Agregar líneas de cuadrícula y optimizar el estilo
ax.grid(True, linestyle='--', alpha=0.4, color='#9aa0a6')

# Agregar puntos de datos originales y optimizar el estilo
ax.scatter(horas, datos_calor, color='#1a73e8', s=50, zorder=5, edgecolor='white', linewidth=1)

# Agregar etiquetas de datos para puntos de tiempo clave y optimizar el estilo y la posición
for x, y in zip(horas[::4], datos_calor[::4]):
    ax.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 12), ha='center', fontsize=11, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='#dadce0', alpha=0.8))

# Resaltar picos y valles y optimizar el estilo
indice_pico = np.argmax(datos_calor)
indice_valle = np.argmin(datos_calor)
ax.scatter([horas[indice_pico], horas[indice_valle]],
           [datos_calor[indice_pico], datos_calor[indice_valle]],
           color='#ea4335', s=100, zorder=5, edgecolor='white', linewidth=1.5)

# Agregar anotaciones para picos y valles y optimizar el estilo
ax.annotate(f'Pico: {datos_calor[indice_pico]} diez mil', (horas[indice_pico], datos_calor[indice_pico]),
            textcoords='offset points', xytext=(30, 20), ha='left', fontsize=12,
            arrowprops=dict(arrowstyle='->', color='#ea4335', linewidth=1.5))

ax.annotate(f'Valle: {datos_calor[indice_valle]} diez mil', (horas[indice_valle], datos_calor[indice_valle]),
            textcoords='offset points', xytext=(-30, -30), ha='right', fontsize=12,
            arrowprops=dict(arrowstyle='->', color='#ea4335', linewidth=1.5))

# Agregar sugerencias de zona horaria y optimizar el estilo
ax.axvspan(5, 9, alpha=0.05, color='#4285f4', label='Pico Matutino')
ax.axvspan(15, 17, alpha=0.05, color='#4285f4')
ax.text(7, 3800, 'Pico Matutino', ha='center', fontsize=12, color='#202124',
        bbox=dict(boxstyle='round,pad=0.2', fc='#4285f4', alpha=0.1))
ax.text(16, 3800, 'Pico Vespertino', ha='center', fontsize=12, color='#202124',
        bbox=dict(boxstyle='round,pad=0.2', fc='#4285f4', alpha=0.1))

# Optimizar el estilo de los ejes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#dadce0')
ax.spines['bottom'].set_color('#dadce0')
ax.tick_params(axis='both', which='major', labelsize=12, color='#9aa0a6')

# Agregar una leyenda y optimizar el estilo
ax.legend([line], ['Tendencia del calor de búsqueda'], loc='upper right', frameon=True,
          framealpha=0.9, edgecolor='#dadce0', fontsize=12)

# Agregar una marca de agua y optimizar el estilo
fig.text(0.85, 0.15, 'Visualización de Datos', fontsize=30, color='#e0e0e0',
         ha='center', va='center', rotation=30, alpha=0.3)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()