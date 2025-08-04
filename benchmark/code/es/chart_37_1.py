import matplotlib.pyplot as plt
import numpy as np

# Nombres de los canales
canales = ["Sala de transmisión en vivo", "Vídeo corto", "Gráfico"]
# Datos de proporción de los canales correspondientes
porcentajes = [89, 34, 16]

x = np.arange(len(canales))  # Posiciones del eje x
ancho = 0.5  # Ancho de las barras

fig, ax = plt.subplots()
# Dibujar un gráfico de barras con un color marrón similar a la imagen original
barras = ax.bar(x, porcentajes, ancho, color='#C09A7B')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(canales)
# Establecer el rango del eje y
ax.set_ylim(0, 100)

# Mostrar el valor del porcentaje en cada barra
for barra in barras:
    altura = barra.get_height()
    ax.annotate('{}%'.format(altura),
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Distancia vertical del valor desde la barra
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer el título del gráfico
ax.set_title('Principales canales para que los consumidores compren ropa de otoño e invierno en el comercio electrónico de Douyin')

plt.show()