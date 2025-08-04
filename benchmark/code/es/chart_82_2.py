import matplotlib.pyplot as plt
import numpy as np

# Categorías de puntos problemáticos
puntos_problematicos = [
    "Alto estrés entre trabajo y vida privada, propenso a la tensión emocional/depresión",
    "Insatisfacción subjetiva con el propio cuerpo/físico",
    "Estado de salud subóptima, padecimiento de enfermedades crónicas como la espondilitis cervical",
    "El marketing en redes sociales desencadena ansiedad corporal/o sobre el estilo de vida",
    "Tener malos hábitos de vida/adicciones como acostarse tarde y fumar",
    "Dificultad para equilibrar trabajo y vida privada, con poco tiempo libre",
    "Círculo social reducido, deseo de hacer más amigos",
    "Los ingresos disponibles son insuficientes para satisfacer las necesidades de consumo"
]
# Porcentajes correspondientes (%)
porcentajes = [55.1, 50.7, 47.0, 43.8, 41.6, 39.9, 31.9, 29.7]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras (gráfico de barras horizontales, ajustado para ser consistente con la imagen original)
y = np.arange(len(puntos_problematicos))
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

# Establecer las marcas y etiquetas del eje y (ajustar el orden para que el primer punto problemático esté en la parte superior)
ax.set_yticks(y)
ax.set_yticklabels(puntos_problematicos)
# Ocultar las marcas del eje x
ax.set_xticks([])
# Establecer el título
ax.set_title("Principales puntos problemáticos en la vida diaria y el trabajo de los usuarios de fitness chinos en 2022", fontsize=14, fontweight="bold")

# Simular diferentes estilos de borde (según la imagen original, algunas entradas tienen bordes discontinuos. Aquí es una demostración simplificada y se puede expandir según sea necesario)
# Por ejemplo, agregar un borde discontinuo a "Estado de salud subóptima, padecimiento de enfermedades crónicas como la espondilitis cervical"
indice_especial = 2
barra_especial = barras[indice_especial]
x0, y0 = barra_especial.get_xy()
ancho, alto = barra_especial.get_width(), barra_especial.get_height()
# Dibujar un borde rectangular discontinuo
rect = plt.Rectangle((x0, y0), ancho, alto, fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rect)

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for borde in ["top", "right", "bottom"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()