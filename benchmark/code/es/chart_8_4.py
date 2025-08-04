import matplotlib.pyplot as plt
import numpy as np

# Nombres de las ciudades
ciudades = ['Beijing', 'Shenzhen', 'Wuhan', 'Shanghai', 'Guangzhou']
# Datos de proporción de búsqueda correspondientes (valores aproximados leídos del gráfico, se pueden reemplazar con datos precisos)
porcentajes = [19, 6, 5.5, 4.5, 2.5]

x = np.arange(len(ciudades))  # Se utiliza para establecer la posición del eje x

fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño del gráfico
# Dibujar un gráfico de barras, ajustar el ancho y establecer el color
barras = ax.bar(x, porcentajes, width=0.6, color='skyblue')

# Agregar etiquetas de datos a cada barra
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',  # Texto de la anotación
                xy=(barra.get_x() + barra.get_width() / 2, altura),  # Posición de la anotación
                xytext=(0, 3),  # Desplazamiento vertical
                textcoords="offset points",
                ha='center',  # Alineación horizontal
                va='bottom',  # Alineación vertical
                fontsize=10)  # Tamaño de fuente

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(ciudades, fontsize=10)

# Establecer el rango y las marcas del eje y
ax.set_ylim(0, 22)  # Aumentar ligeramente el límite superior para dejar espacio para las anotaciones
ax.set_yticks(np.arange(0, 21, 5))

# Establecer los títulos de los ejes y el título del gráfico
ax.set_ylabel('Proporción de búsqueda (%)', fontsize=12)
ax.set_title('Top 5 ciudades para búsquedas en la industria de litigios de divorcio en mayo', fontsize=14)

# Agregar líneas de cuadrícula para mejorar la legibilidad
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Mejorar la apariencia del gráfico
plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()