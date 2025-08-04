import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Años
years = np.arange(2012, 2017)
# Datos simulados, siguiendo aproximadamente la tendencia del gráfico original, ingresos por derechos de autor, patrocinios comerciales, intercambio de recursos
copyright_income = [0.5, 0.6, 0.6, 1, 10]
sponsorship_income = [1, 2, 4.5, 8, 5]
resource_swap = [1, 1.2, 1.5, 1.6, 1.7]

# Crear un gráfico
fig, ax = plt.subplots(figsize=(10, 6))  # Aumentar el tamaño del gráfico

# Establecer la cuadrícula de fondo y el color
ax.set_facecolor('#f8f9fa')
ax.grid(True, linestyle='--', alpha=0.7)

# Dibujar tres líneas con colores y marcadores más bonitos
line1, = ax.plot(years, copyright_income, color='#3498db', label='Ingresos por Derechos de Autor', linewidth=3, marker='o', markersize=8)
line2, = ax.plot(years, sponsorship_income, color='#e74c3c', label='Patrocinio Comercial', linewidth=3, marker='s', markersize=8)
line3, = ax.plot(years, resource_swap, color='#2ecc71', label='Intercambio de Recursos', linewidth=3, marker='^', markersize=8)

# Establecer el título y el subtítulo
ax.set_title('Análisis de la Tendencia de Ingresos de 2012 a 2016', fontsize=18, fontweight='bold', pad=20)

# Establecer las etiquetas y las marcas de los ejes
ax.set_xlabel('Año', fontsize=12)
ax.set_ylabel('Ingresos (Miles de Millones de Yuanes)', fontsize=12)
ax.set_xticks(years)
ax.set_xticklabels([f'{year}' for year in years], fontsize=10)
ax.set_yticks(np.arange(0, 11, 2.5))

# Agregar etiquetas numéricas a cada punto de datos
for x, y in zip(years, copyright_income):
    ax.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=9)
for x, y in zip(years, sponsorship_income):
    ax.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=9)
for x, y in zip(years, resource_swap):
    ax.annotate(f'{y}', (x, y), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=9)

# Resaltar el crecimiento de los ingresos por derechos de autor
ax.fill_between(years, copyright_income, 0, color='#3498db', alpha=0.1)

# Ajustar la posición y el estilo de la leyenda
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
          fancybox=True, shadow=True, ncol=3, fontsize=11)

plt.tight_layout()  # Ajustar el diseño
plt.show()