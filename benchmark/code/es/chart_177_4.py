import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = [
    "No hay suficiente tiempo",
    "No se tiene la energía y \nresistencia físicas",
    "El hijo tiene dificultades \nen el aprendizaje",
    "La tutoría después de clase \nes demasiado complicada",
    "Problemas de gestión de conducta",
    "Problemas de salud",
    "Dificultad para elegir el \nmodo de educación familiar"
]
valores = [47, 40, 39, 38, 31, 28, 21]

# Establecer colores (gradiente de la gama de rojo)
colores = [
    "#FF4C4C", "#FF6666", "#FF8080", "#FF9999", "#FFB3B3", "#FFCCCC", "#FFE5E5"
]

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.barh(etiquetas, valores, color=colores)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height() / 2, f'{ancho}%', va='center')

# Embellir el gráfico
ax.invert_yaxis()
ax.set_xlim(0, 55)
ax.set_xlabel("Porcentaje (%)")
ax.set_title("Dificultades y preocupaciones de los padres en la educación familiar de sus hijos", fontsize=14)

plt.tight_layout()
plt.show()