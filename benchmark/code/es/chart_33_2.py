import matplotlib.pyplot as plt
import numpy as np

# Datos de años
years = np.arange(2018, 2025)
# Datos simulados de CR5
cr5_data = [56, 57, 53, 52, 52, 52, 53]

# Crear una figura
plt.figure(figsize=(10, 6))

# Trazar un gráfico de línea con marcadores de datos usando un color azul más profesional
line, = plt.plot(years, cr5_data, color='#1f77b4', marker='o', markersize=8, 
                 linewidth=2.5, markeredgecolor='white', markeredgewidth=1.5)

# Agregar etiquetas de datos
for x, y in zip(years, cr5_data):
    plt.annotate(f'{y}', (x, y), textcoords='offset points',
                 xytext=(0, 10), ha='center', fontsize=10)

# Establecer ejes y marcas de graduación
plt.xticks(years, fontsize=12)
plt.ylim(48, 60)  # Ajustar el rango del eje Y para hacer el gráfico más compacto
plt.yticks(np.arange(48, 61, 2), fontsize=12)

# Agregar líneas de cuadrícula para mejorar la legibilidad
plt.grid(True, linestyle='--', alpha=0.7)

# Agregar un título y etiquetas con un tamaño de fuente más profesional
plt.title('Análisis de la concentración del mercado en el mercado de lavandería y limpieza en China desde 2018 hasta 2024', fontsize=16, pad=15)
plt.xlabel('Año', fontsize=14, labelpad=10)
plt.ylabel('Concentración del mercado (%)', fontsize=14, labelpad=10)

# Embellir la leyenda
plt.legend([line], ['Concentración del mercado CR5'], fontsize=12, loc='upper right')

# Ajustar el diseño del gráfico
plt.tight_layout()

# Mostrar el gráfico
plt.show()