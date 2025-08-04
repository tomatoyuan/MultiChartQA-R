import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.array([2019, 2020, 2021, 2022, 2023])
# Población de 60 años y mayores (en diez miles de personas)
elderly_population = np.array([25388, 26402, 26736, 28004, 29697])
# Proporción de la población de 60 años y mayores (%)
proportion = np.array([18.1, 18.7, 18.9, 19.8, 21.1])

# Crear una figura y un eje
fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras (eje izquierdo)
bars = ax1.bar(years, elderly_population, color='darkgreen', label='Población de 60 años y mayores (en diez miles de personas)')
ax1.set_xlabel('Año')
ax1.set_ylabel('Población de 60 años y mayores (en diez miles de personas)', color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

# Agregar etiquetas de datos encima de las barras
for bar, pop in zip(bars, elderly_population):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200, 
             f'{pop}', ha='center', va='bottom', color='darkgreen')

# Crear un eje derecho para el gráfico de línea
ax2 = ax1.twinx()
line, = ax2.plot(years, proportion, marker='o', color='black', label='Proporción de la población de 60 años y mayores (%)')
ax2.set_ylabel('Proporción de la población de 60 años y mayores (%)', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Agregar etiquetas de datos junto a los puntos de datos del gráfico de línea
for x, y in zip(years, proportion):
    ax2.annotate(f'{y}%', (x, y), textcoords='offset points',
                 xytext=(0,10), ha='center', color='black')

# Agregar una leyenda
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# Establecer las marcas del eje x en años
ax1.set_xticks(years)

# Mostrar el gráfico
plt.title('Población de 60 años y mayores y su proporción de la población total desde 2019 hasta 2023')
plt.tight_layout()  # Ajustar el diseño para evitar superposición de contenido
plt.show()