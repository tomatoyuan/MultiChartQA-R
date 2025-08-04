import matplotlib.pyplot as plt
import numpy as np

# Tipos de gafas inteligentes
tipos_gafas = ["Gafas inteligentes de realidad virtual (VR)", "Gafas inteligentes de realidad aumentada (AR)", "Gafas de visualización AI", "Gafas de audio AI", "Gafas de fotografía AI", "Gafas inteligentes de realidad mixta (MR)", "Otras gafas inteligentes"]
# Porcentajes correspondientes (%), los datos se simulan aproximadamente y se pueden ajustar según la situación real
porcentajes = [79.4, 69.8, 63.9, 62.0, 55.8, 38.7, 11.9]

x = np.arange(len(tipos_gafas))  # Posiciones de las marcas en el eje x

fig, ax = plt.subplots()

# Dibujar un gráfico de barras horizontales con un color verde similar
barras = ax.barh(x, porcentajes, color='greenyellow')

# Agregar un título
ax.set_title('Tipos de gafas inteligentes conocidos por todos los encuestados')

# Establecer las etiquetas de las marcas en el eje y
ax.set_yticks(x)
ax.set_yticklabels(tipos_gafas)

# Agregar etiquetas numéricas a cada barra
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(3, 0),  # Desplazamiento horizontal de 3 puntos, centrado verticalmente
                textcoords="offset points",
                ha='left', va='center')

# Ocultar las marcas del eje x (La figura original no muestra marcas obvias en el eje x, se enfoca principalmente en la longitud de las barras y las etiquetas)
ax.xaxis.set_ticks([])

plt.show()