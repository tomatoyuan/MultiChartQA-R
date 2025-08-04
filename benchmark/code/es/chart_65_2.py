import matplotlib.pyplot as plt
import numpy as np

# Nombres de las plataformas
plataformas = ["TikTok", "YouTube", "Instagram", "Facebook", "Twitter", "Otros"]
# Datos correspondientes
datos = [30.0, 22.0, 22.0, 14.0, 4.0, 13.0]

x = np.arange(len(plataformas))  # Se utiliza para establecer la posición del eje x
ancho_barra = 0.5  # Ancho del gráfico de barras

fig, ax = plt.subplots()
# Dibujar el gráfico de barras, establecer el color, ancho, etc. El color es lo más cercano al azul posible
barras = ax.bar(x, datos, width=ancho_barra, color="#64B5F6", edgecolor="white")  

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Distancia vertical de la etiqueta desde el gráfico de barras
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(plataformas)
# Establecer la etiqueta del eje y (El gráfico original no muestra la etiqueta del eje y. Puedes decidir si agregarla según tus necesidades)
# ax.set_ylabel("Porcentaje (%)")
# Establecer el título del gráfico
ax.set_title("Plataformas preferidas por creadores internacionales para la publicación de contenido")

# Embelezar el gráfico, ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.show()