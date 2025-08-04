import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Construir datos
data = {
    'Mes': ['202401', '202402', '202403', '202404', '202405', '202406', 
            '202407', '202408', '202409', '202410', '202411', '202412', '202501'],
    'Ventas (Miles de millones)': [8, 7, 10, 9, 11, 10, 9, 9, 10, 13, 12, 9, 10],
    'Precio Promedio de Transacción': [10, 11, 7, 8, 8, 8, 4, 6, 9, 10, 10, 8, 10]
}
df = pd.DataFrame(data)

# Convertir el mes al formato de fecha para una mejor visualización
df['Fecha'] = df['Mes'].apply(lambda x: datetime.strptime(x, '%Y%m'))

# Crear un gráfico de doble eje
fig, ax1 = plt.subplots(figsize=(14, 7))  # Aumentar el tamaño del gráfico
ax2 = ax1.twinx()

# Establecer el fondo del gráfico y la cuadrícula
fig.patch.set_facecolor('#f8f9fa')  # Fondo de color gris claro
ax1.set_facecolor('#ffffff')  # Área de trazado en blanco
ax1.grid(True, linestyle='--', alpha=0.7)  # Agregar líneas de cuadrícula

# Dibujar el gráfico de barras de ventas - usar color degradado y efecto de sombra
ancho_barra = 0.6
barras = ax1.bar(df['Fecha'], df['Ventas (Miles de millones)'], width=ancho_barra, 
                 color='#3274A1', edgecolor='#285F8F', alpha=0.9, 
                 label='Ventas (Miles de millones)', zorder=3)  # zorder controla el orden de las capas

# Agregar etiquetas numéricas al gráfico de barras
for barra in barras:
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., altura + 0.15,
             f'{altura}', ha='center', va='bottom', fontsize=9)

# Dibujar el gráfico de línea del precio promedio de transacción - usar una curva suave y puntos marcadores
linea, = ax2.plot(df['Fecha'], df['Precio Promedio de Transacción'], color='#E1812C', 
                  label='Precio Promedio de Transacción', linewidth=2.5, marker='o', markersize=7,
                  markeredgecolor='white', markeredgewidth=1, zorder=4)

# Agregar etiquetas numéricas al gráfico de línea
for x, y in zip(df['Fecha'], df['Precio Promedio de Transacción']):
    ax2.annotate(f'{y}', (x, y), textcoords='offset points',
                 xytext=(0, 8), ha='center', fontsize=9)

# Establecer las etiquetas de los ejes y el título
ax1.set_xlabel('Mes', fontsize=12)
ax1.set_ylabel('Ventas (Miles de millones)', color='#3274A1', fontsize=12)
ax2.set_ylabel('Precio Promedio de Transacción', color='#E1812C', fontsize=12)

# Establecer el título y el subtítulo
plt.suptitle('Ventas Mensuales de Industrias Relacionadas con Alimentos Saludables en 2024', fontsize=16, fontweight='bold', y=0.96)
plt.title('*Algunas plataformas principales de comercio electrónico en estantes y de comercio electrónico de contenido', fontsize=11, color='#666666', y=1.02)

# Formatear la visualización de la fecha en el eje x
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
plt.xticks(rotation=45, ha='right', fontsize=10)

# Establecer el rango del eje y
ax1.set_ylim(0, max(df['Ventas (Miles de millones)']) * 1.1)  # Dejar un 10% de espacio
ax2.set_ylim(0, max(df['Precio Promedio de Transacción']) * 1.1)

# Agregar una leyenda - usar una mejor posición y estilo
lineas_1, etiquetas_1 = ax1.get_legend_handles_labels()
lineas_2, etiquetas_2 = ax2.get_legend_handles_labels()
ax1.legend(lineas_1 + lineas_2, etiquetas_1 + etiquetas_2, 
           loc='upper center', bbox_to_anchor=(0.5, -0.08),
           ncol=2, frameon=True, fancybox=True, shadow=True,
           fontsize=10)

# Agregar una anotación - resaltar el mes con las ventas más altas
indice_max_ventas = df['Ventas (Miles de millones)'].idxmax()
ax1.annotate('Pico de Ventas', xy=(df['Fecha'][indice_max_ventas], df['Ventas (Miles de millones)'][indice_max_ventas]),
             xytext=(20, 30), textcoords='offset points',
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=10)

# Ajustar el diseño
plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Dejar espacio para el texto inferior y superior

# Mostrar el gráfico
plt.show()