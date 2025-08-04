import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.colors as mcolors
import numpy as np

# Extraer contenido del gráfico
casos = [
    {
        "fecha": datetime(2024, 8, 21),
        "desc": "La estudiante de primer año de universidad de 18 años, Xu Yuyu,\nfalleció por parada cardíaca después de ser estafada de 9,900 yuanes",
        "severidad": "Extremadamente Alta",  # Nuevo campo de severidad
        "color": "#e41a1c"  # Nueva asignación de color
    },
    {
        "fecha": datetime(2024, 8, 23),
        "desc": "El estudiante de segundo año de la Universidad de Tecnología de Shandong,\nmurió repentinamente después de perder 1,996 yuanes en un fraude telefónico",
        "severidad": "Alta",
        "color": "#ff7f00"
    },
    {
        "fecha": datetime(2024, 8, 29),
        "desc": "Un profesor de la Universidad Tsinghua fue víctima de un fraude telefónico\ncon un monto involucrado de 17.6 millones de yuanes",
        "severidad": "Media",
        "color": "#4daf4a"
    },
    {
        "fecha": datetime(2024, 8, 31),
        "desc": "La joven de 19 años, Cai Yanyan, de Jieyang, Guangdong,\nse ahogó después de ser estafada de más de 10,000 yuanes en tarifas de matrícula y gastos de manutención a través de un mensaje de texto",
        "severidad": "Alta",
        "color": "#ff7f00"
    },
    {
        "fecha": datetime(2024, 9, 6),
        "desc": "El estudiante de segundo año de la Universidad de Negocios y Tecnología de Jilin,\nse suicidó después de ser estafado de 5,000 yuanes en tarifas de matrícula",
        "severidad": "Alta",
        "color": "#ff7f00"
    }
]

# Dividir los datos para facilitar la representación gráfica
fechas = [caso["fecha"] for caso in casos]
descripciones = [caso["desc"] for caso in casos]
colores = [caso["color"] for caso in casos]
severidades = [caso["severidad"] for caso in casos]

# Crear el lienzo
fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('#f8f9fa')  # Establecer el color de fondo del lienzo
ax.set_facecolor('#ffffff')  # Establecer el color de fondo del área de trazado

# Dibujar el gráfico de barras horizontales, establecer colores según la severidad
y_ticks = range(len(descripciones))
barras = ax.barh(y_ticks, [1]*len(descripciones), 
               left=mdates.date2num(fechas), 
               height=0.6, 
               color=colores,
               alpha=0.8,
               edgecolor='black',
               linewidth=0.5)

# Añadir etiquetas de datos
for i, (fecha, barra) in enumerate(zip(fechas, barras)):
    ax.text(mdates.date2num(fecha) + 0.1, i, 
            fecha.strftime('%m-%d'), 
            va='center', 
            fontsize=10,
            fontweight='bold')

# Establecer el eje x en formato de fecha
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=2))  # Mostrar una marca de graduación cada 2 días
ax.set_xlabel("Fecha", fontsize=12, fontweight='bold')
ax.set_xlim(mdates.date2num(min(fechas)) - 1, mdates.date2num(max(fechas)) + 2)  # Ajustar el rango del eje x

# Establecer el eje y con las descripciones de los casos
ax.set_yticks(y_ticks)
ax.set_yticklabels(descripciones, fontsize=10)

# Añadir título
ax.set_title("Línea de tiempo de casos típicos de fraude telefónico", fontsize=18, fontweight="bold", pad=20)
ax.title.set_color('#333333')

# Añadir cuadrícula
ax.grid(axis="x", linestyle="--", alpha=0.6, color='#cccccc')

# Añadir leyenda de severidad
elementos_leyenda = [plt.Line2D([0], [0], marker='o', color='w', label='Extremadamente Alta',
                          markerfacecolor='#e41a1c', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Alta',
                          markerfacecolor='#ff7f00', markersize=10),
                   plt.Line2D([0], [0], marker='o', color='w', label='Media',
                          markerfacecolor='#4daf4a', markersize=10)]

ax.legend(handles=elementos_leyenda, title='Severidad del caso', loc='lower right')

# Añadir nota inferior
plt.figtext(0.5, 0.01, 'Fuente de datos: Compilado a partir de informes públicos', ha='center', fontsize=9, color='#666666')

# Optimizar el diseño
plt.tight_layout()
plt.subplots_adjust(bottom=0.08)  # Ajustar el margen inferior
plt.show()