import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
# Datos del gráfico de pastel
etiquetas_pastel = ["Tener un plan claro para el desarrollo después de la graduación", "No tener un plan claro"]
tamaños_pastel = [94.6, 5.4]
colores_pastel = ["#81c784", "#b0bec5"]  # Esquema de color verde similar a la imagen original

# Datos del gráfico de barras (Sub - categorías de planes claros)
categorias_barras = ["Estudios adicionales", "Empleo", "Examen de servicio civil", "Estudios en el extranjero"]
valores_barras = [41.0, 34.8, 15.5, 3.3]
colores_barras = ["#a5d6a7", "#81c784", "#c8e6c9", "#e8f5e9"]  # Gradiente del mismo esquema de color

# -------------------- Crear el lienzo y los sub - gráficos --------------------
fig, (ax_pastel, ax_barras) = plt.subplots(1, 2, figsize=(12, 5), 
                                     gridspec_kw={'width_ratios': [1, 2]})

# -------------------- Dibujar el gráfico de pastel --------------------
porciones, etiquetas_texto, textos_porcentaje = ax_pastel.pie(
    tamaños_pastel, 
    labels=None,  # No mostrar etiquetas temporalmente, se mostrarán a través de la leyenda
    autopct='%1.1f%%',
    startangle=90,
    colors=colores_pastel,
    textprops={'fontsize': 12},
    wedgeprops={'linewidth': 2, 'edgecolor': 'white'}
)

# Establecer el color de los textos de porcentaje
for texto in textos_porcentaje:
    texto.set_color('white')
    texto.set_fontweight('bold')

# Agregar una leyenda para mostrar las etiquetas completas
ax_pastel.legend(
    porciones, 
    etiquetas_pastel, 
    loc='center left', 
    bbox_to_anchor=(-1.1, 0.5),
    fontsize=10
)

# Ajustar la posición del gráfico de pastel
ax_pastel.set_position([0.05, 0.1, 0.3, 0.8])

# -------------------- Dibujar el gráfico de barras --------------------
ancho_barra = 0.6
x = np.arange(len(categorias_barras))

# Dibujar el gráfico de barras básico
barras = ax_barras.barh(
    x, 
    valores_barras, 
    color=colores_barras, 
    height=0.6,
    edgecolor='white',
    linewidth=1
)

# Agregar anotaciones numéricas
for barra in barras:
    ancho = barra.get_width()
    ax_barras.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height()/2,
        f'{ancho}%',
        va='center',
        fontsize=10,
        fontweight='bold',
        color='#424242'
    )

# Embellir el gráfico de barras
ax_barras.set_yticks(x)
ax_barras.set_yticklabels(categorias_barras, fontsize=12, color='#424242')
ax_barras.set_xlim(0, 50)  # Similar a la proporción de la imagen original
ax_barras.set_xticks([])   # Ocultar las marcas del eje x
ax_barras.spines['top'].set_visible(False)
ax_barras.spines['right'].set_visible(False)
ax_barras.spines['bottom'].set_visible(False)
ax_barras.spines['left'].set_visible(False)
ax_barras.tick_params(axis='y', left=False)

# Ajustar la posición del gráfico de barras
ax_barras.set_position([0.4, 0.1, 0.5, 0.8])

# -------------------- Embellimiento global --------------------
# Agregar el título principal
fig.suptitle(
    "Planes de desarrollo de los estudiantes universitarios después de la graduación", 
    fontsize=16, 
    fontweight='bold', 
    y=0.95,
    x=0.3
)

# Agregar una flecha de conexión
import matplotlib.patches as patches
flecha = patches.FancyArrow(
    0.35, 0.5, 0.05, 0, 
    width=0.02, 
    head_width=0.05, 
    head_length=0.03, 
    color='#81c784',
    transform=fig.transFigure,
    figure=fig
)
fig.patches.append(flecha)

# Ajustar el diseño
plt.subplots_adjust(wspace=0.2)

plt.show()