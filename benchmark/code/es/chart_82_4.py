import matplotlib.pyplot as plt
import numpy as np

# Categorías de razones
razones = [
    "El modo de tarjeta anual tiene una duración larga y es difícil de mantener",
    "Insatisfecho con la actitud y habilidades de enseñanza del entrenador",
    "El estilo de la tienda está desactualizado y carece de atractivo",
    "El modo de tarjeta anual tiene altos riesgos, se preocupa por que el comerciante se marche",
    "A menudo envían folletos o hacen ventas directas, lo que deja una mala impresión",
    "El precio es alto, insatisfecho con la relación calidad - precio",
    "Los cursos son bastante homogéneos y no pueden satisfacer las necesidades",
    "A menudo hay noticias sobre gimnasios que cierran y se marchan, lo que deja una mala impresión",
    "Ubicación inconveniente"
]
# Porcentajes correspondientes (%)
porcentajes = [47.5, 43.0, 42.4, 41.1, 39.9, 38.0, 30.4, 21.5, 12.0]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras (gráfico de barras horizontales, ajustado para ser consistente con la orientación de la imagen original)
y = np.arange(len(razones))
ancho_barra = 0.6
barras = ax.barh(y, porcentajes, height=ancho_barra, color="#A4C639")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Dibujar un borde discontinuo para los 5 primeros (los primeros 5 elementos)
for i in range(5):
    barra_especial = barras[i]
    x0, y0 = barra_especial.get_xy()
    ancho, altura = barra_especial.get_width(), barra_especial.get_height()
    rect = plt.Rectangle((x0, y0), ancho, altura, fill=False, edgecolor='green', linestyle='--')
    ax.add_patch(rect)

# Establecer las marcas y etiquetas del eje y (ajustar el orden para que la primera razón esté en la parte superior)
ax.set_yticks(y)
ax.set_yticklabels(razones)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Razones por las que los usuarios de gimnasios chinos no eligieron gimnasios tradicionales en 2022", fontsize=14, fontweight="bold")

# Embellir el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()