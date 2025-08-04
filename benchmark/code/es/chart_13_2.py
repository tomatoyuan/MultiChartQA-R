import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Organizar los datos
grupos_edad = ["Menos de 18", "18 - 24", "25 - 34", "35 - 49", "Más de 50"]
cobertura_muestral = [23.1, 22.16, 39.41, 12.12, 2.8]  # Datos de cobertura de la muestra
cobertura_total = [12.4, 28.44, 36.63, 20.16, 3.2]  # Datos de cobertura total

x = np.arange(len(grupos_edad))  # Posiciones de las marcas en el eje x
ancho = 0.35  # Ancho de las barras

# Crear una figura y un subgráfico, optimizar el tamaño de la figura para adaptación
fig, ax = plt.subplots(figsize=(10, 7))
# Establecer el color de fondo general, similar al azul de la figura original
fig.set_facecolor('#00a8e8')
ax.set_facecolor('#00a8e8')

# Dibujar el gráfico de barras de cobertura de la muestra, ajustar el color para que sea más suave
rects1 = ax.bar(
    x - ancho/2, 
    cobertura_muestral, 
    ancho, 
    label='Cobertura de la Muestra', 
    color='#003f5c',
    edgecolor='white',  # Añadir bordes blancos para distinguir las columnas
    linewidth=1
)
# Dibujar el gráfico de barras de cobertura total, ajustar el color para que sea más suave
rects2 = ax.bar(
    x + ancho/2, 
    cobertura_total, 
    ancho, 
    label='Cobertura Total', 
    color='#457fca',
    edgecolor='white',  # Añadir bordes blancos para distinguir las columnas
    linewidth=1
)

# Personalizar el estilo del título
ax.set_title(
    'Modo de Observación: Los Trabajadores de Oficina son los Más Afectados', 
    fontsize=20, 
    fontweight='bold', 
    color='#002f4a',  # Título más oscuro para mejor visibilidad
    pad=20  # Aumentar el espacio entre el título y el gráfico
)
ax.set_ylabel(
    'Distribución de Atributos de la Población de la Opinión Pública sobre Tormentas', 
    fontsize=14, 
    color='#333333',
    labelpad=15  # Aumentar el espacio entre la etiqueta del eje y y el gráfico
)

# Personalizar el estilo de las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(
    grupos_edad, 
    fontsize=12, 
    color='#333333',
    rotation=0  # Mantener la visualización horizontal
)

# Optimizar la escala del eje y, mostrar porcentajes más claramente
ax.set_ylim(0, 50)  # Establecer un rango razonable para el eje y
ax.yaxis.set_major_formatter('{x}%')  # Mostrar directamente el estilo de porcentaje (requiere matplotlib 3.3+)
ax.tick_params(axis='y', labelsize=12, colors='#333333')

# Optimizar el estilo de las etiquetas de datos
def autolabel(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate(
            f'{altura}%',
            xy=(rect.get_x() + rect.get_width()/2, altura),
            xytext=(0, 5),  # Ajustar la posición de la etiqueta para evitar superposiciones
            textcoords='offset points',
            ha='center', 
            va='bottom',
            fontsize=11,
            color='white',  # Etiquetas blancas son más llamativas
            fontweight='bold'
        )

autolabel(rects1)
autolabel(rects2)

# Personalizar el estilo de la leyenda, colocarla encima del gráfico
elementos_leyenda = [
    Patch(facecolor='#003f5c', edgecolor='white', label='Cobertura de la Muestra'),
    Patch(facecolor='#457fca', edgecolor='white', label='Cobertura Total')
]
ax.legend(
    handles=elementos_leyenda,
    loc='upper center',  # Posición de la leyenda
    bbox_to_anchor=(0.5, 1.15),  # Ajustar finamente la posición de la leyenda encima del gráfico
    ncol=2,  # Mostrar la leyenda en dos columnas
    fontsize=12,
    frameon=False  # Quitar el borde de la leyenda
)

# Añadir líneas de cuadrícula para mejorar la legibilidad
ax.grid(
    axis='y', 
    color='white', 
    linestyle='--', 
    alpha=0.8,
    linewidth=1
)

# Optimizar el diseño general
plt.tight_layout()
# Mostrar el gráfico
plt.show()