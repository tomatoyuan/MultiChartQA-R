import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.array([2020, 2021, 2022, 2023, 2024])
# Datos del tamaño del mercado de mascotas/alimentos y suministros para mascotas (aproximados, ajustables)
market_size = np.array([40, 45, 55, 60, 70])
# Datos de la tasa de crecimiento (aproximados, ajustables)
growth_rate = np.array([10, 9, 15, 8, 14])

# Crear un lienzo y ejes
fig, ax1 = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño del gráfico

# Dibujar un gráfico de barras (Tamaño del mercado de mascotas/alimentos y suministros para mascotas)
bars = ax1.bar(years, market_size, color='blue', label='Mascotas/Alimentos y Suministros para Mascotas')
ax1.set_xlabel('Año')
ax1.set_ylabel('Tamaño del Mercado (Valor Aproximado)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Agregar etiquetas de datos encima del gráfico de barras
for bar, value in zip(bars, market_size):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
             f'{value}', ha='center', va='bottom', color='blue')

# Crear un segundo eje para dibujar un gráfico de línea (Tasa de crecimiento)
ax2 = ax1.twinx()
line, = ax2.plot(years, growth_rate, color='orange', marker='o', label='Tasa de Crecimiento')
ax2.set_ylabel('Tasa de Crecimiento (%)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')
# Establecer la escala del eje y, similar al gráfico original
ax2.set_ylim(0, 18)
ax2.set_yticks(np.arange(0, 18, 2))

# Agregar anotaciones a cada punto de datos del gráfico de línea
for x, y in zip(years, growth_rate):
    ax2.annotate(f'{y}%', (x, y), textcoords='offset points',
                 xytext=(0,10), ha='center', color='orange')

# Agregar una leyenda
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# Establecer el título del gráfico
plt.title('Tendencia del Tamaño del Mercado de Comercio Electrónico en Línea para Mascotas')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()