import matplotlib.pyplot as plt
import numpy as np

# Datos del eje de tiempo
fechas = ['Ene 2015', 'Mar 2015', 'May 2015', 'Jul 2015', 'Sep 2015', 
         'Nov 2015', 'Ene 2016', 'Mar 2016', 'May 2016', 'Jul 2016', 'Sep 2016']

# Datos del índice de búsqueda con ligeras fluctuaciones (ajustados manualmente)
indice_busqueda = [
    2950,  # Original 3000
    2980,  # Original 3000
    3020,  # Original 3000
    6000,
    9000,
    2950,  # Original 3000
    2960,  # Original 3000
    2970,  # Original 3000
    3010,  # Original 3000
    9000,
    15000
]

# Convertir el eje de tiempo a un índice para graficar
x = np.arange(len(fechas))  

# Crear un objeto de gráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Trazar el gráfico de línea, establecer el ancho de línea y el estilo del marcador
line, = ax.plot(x, indice_busqueda, color='orange', marker='o', markersize=6, 
                linewidth=2, label='Tendencia del índice de búsqueda de "enfermedad por aire acondicionado"')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(fechas, rotation=45, ha='right')

# Establecer el rango y la etiqueta del eje y
ax.set_ylim(0, 1.1 * max(indice_busqueda))
ax.set_ylabel('Índice de búsqueda')

# Agregar un título y un subtítulo
ax.set_title('Índice de búsqueda relacionado con "enfermedad por aire acondicionado"', fontsize=16, pad=15)

# Anotar los valores en el gráfico de línea
for i, (xi, yi) in enumerate(zip(x, indice_busqueda)):
    ax.annotate(f'{int(round(yi))}',  # Mostrar como un entero
                (xi, yi),
                textcoords='offset points',
                xytext=(0, 10),  # Desplazamiento de la posición del texto
                ha='center',
                fontsize=9)

# Agregar una leyenda y líneas de cuadrícula
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Ocultar los ejes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()