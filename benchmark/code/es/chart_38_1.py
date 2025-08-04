import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

# Datos
etiquetas = ['Menos de 18', '18 - 24', '25 - 29', 'Más de 30']
tamaños = [35, 48, 13, 4]
# Configuración de colores, lo más cercano posible al gráfico original
colores = ['#4CAF50', '#FF9800', '#9E9E9E', '#795548']  

# Crear un gráfico de pastel
fig, ax = plt.subplots()
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%',
                                  startangle=90, colors=colores)

# Establecer el tamaño de fuente y otros estilos para que la visualización sea más cercana al gráfico original
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

# El siguiente es el proceso general para agregar una imagen en el centro. Reemplace 'tu_ruta_de_imagen.png' con la ruta real de la imagen.
# Suponga que la imagen es cuadrada y ha sido procesada. Este es solo un ejemplo. Es posible que deba ajustar el tamaño, la posición, etc. en la práctica.
# imagen = plt.imread('tu_ruta_de_imagen.png')
# caja_imagen = OffsetImage(imagen, zoom=0.3)  # zoom ajusta el tamaño de la imagen
# ab = AnnotationBbox(caja_imagen, (0, 0), frameon=False)
# ax.add_artist(ab)

# Establecer el título del gráfico
ax.set_title('Edad y tipo de usuarios de lentes de contacto por primera vez', fontsize=14, y=1.05)

# Mantener el gráfico de pastel circular
ax.axis('equal')

plt.show()