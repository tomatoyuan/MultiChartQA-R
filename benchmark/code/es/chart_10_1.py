import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Los datos se colocan directamente en la lista (formato de fecha: 'YYYY-MM-DD', los valores son valores completos)
fechas = ['2025-05-01', '2025-05-02', '2025-05-03', '2025-05-04', '2025-05-05', '2025-05-06', '2025-05-07', '2025-05-08', '2025-05-09', '2025-05-10', '2025-05-11', '2025-05-12', '2025-05-13', '2025-05-14', '2025-05-15', '2025-05-16', '2025-05-17', '2025-05-18', '2025-05-19', '2025-05-20', '2025-05-21', '2025-05-22', '2025-05-23', '2025-05-24', '2025-05-25', '2025-05-26', '2025-05-27', '2025-05-28', '2025-05-29', '2025-05-30', '2025-05-31']
atencion_busqueda = [6200000, 6500000, 7000000, 9700000, 9500000, 8500000, 7200000, 9500000, 9500000, 9500000, 9500000, 9300000, 8800000, 7800000, 9000000, 10200000, 9800000, 9500000, 9200000, 8500000, 7800000, 7800000, 9000000, 9500000, 9500000, 9300000, 8800000, 7800000, 8500000, 9000000, 9500000]

# Convertir cadenas de fecha a objetos datetime
fechas = [datetime.strptime(fecha, '%Y-%m-%d') for fecha in fechas]

# Crear un lienzo y un sub - gráfico, aumentar el tamaño del gráfico
fig, ax = plt.subplots(figsize=(15, 7))

# Establecer el estilo de fondo
ax.set_facecolor('#f8f9fa')
fig.patch.set_facecolor('#ffffff')

# Dibujar un gráfico de líneas, agregar transparencia y puntos de marcador
linea, = ax.plot(fechas, atencion_busqueda, color='#1f77b4', linewidth=2.5, alpha=0.8, marker='o', markersize=5, markevery=3)

# Agregar un área rellena
ax.fill_between(fechas, atencion_busqueda, 0, color='#1f77b4', alpha=0.1)

# Establecer el eje x en formato de fecha, mostrar una marca cada 3 días
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))

# Establecer el título del gráfico y las etiquetas de los ejes, aumentar el tamaño y el estilo de la fuente
ax.set_title('Tendencia de Atención de Búsqueda en el Sector de Capacitación Profesional en Mayo', fontsize=20, pad=20, fontweight='bold')
ax.set_ylabel('Atención de Búsqueda', fontsize=16, labelpad=15)
ax.set_xlabel('Fecha', fontsize=16, labelpad=15)

# Establecer el rango y el formato de las marcas del eje y, agregar separadores de miles
ax.set_ylim(0, 12000000)
ax.yaxis.set_major_formatter(lambda x, pos: f'{int(x):,}')

# Agregar líneas de cuadrícula y establecer el estilo
ax.grid(True, linestyle='--', alpha=0.5, color='#cccccc')

# Personalizar el tamaño de la fuente de las etiquetas de las marcas
ax.tick_params(axis='both', which='major', labelsize=12)

# Hacer que las fechas del eje x ajusten automáticamente el espaciado para evitar superposiciones
fig.autofmt_xdate(rotation=45, ha='right')

# Agregar anotaciones para los valores máximo y mínimo
max_val = max(atencion_busqueda)
min_val = min(atencion_busqueda)
max_idx = atencion_busqueda.index(max_val)
min_idx = atencion_busqueda.index(min_val)

ax.annotate(f'Pico: {max_val:,}',
            xy=(fechas[max_idx], max_val),
            xytext=(fechas[max_idx], max_val + 500000),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12,
            ha='center')

ax.annotate(f'Válle: {min_val:,}',
            xy=(fechas[min_idx], min_val),
            xytext=(fechas[min_idx], min_val - 1000000),
            arrowprops=dict(facecolor='green', shrink=0.05, width=1.5, headwidth=8),
            fontsize=12,
            ha='center')

# Agregar una leyenda
ax.legend([linea], ['Atención de Búsqueda'], loc='upper left', fontsize=12)

# Agregar una marca de agua
fig.text(0.85, 0.15, 'Fuente de Datos: Informe de la Industria', fontsize=10, color='gray', alpha=0.7, ha='right')

# Optimizar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()