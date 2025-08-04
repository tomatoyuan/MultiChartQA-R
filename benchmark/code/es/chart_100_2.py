import matplotlib.pyplot as plt
import numpy as np

# Clasificación de problemas de sueño (TOP10)
problemas = [
    "Tiempo de sueño profundo demasiado corto", "Dificultad para conciliar el sueño", "Hábito de acostarse tarde",
    "Sueño ligero/facilmente despertado", "Duración de sueño insuficiente", "Sentirse somnoliento/con poca energía durante el día",
    "Horario de sueño irregular", "Quedarse en la cama/levantarse tarde los fines de semana, etc.", "Tener muchos sueños/pesadillas"
]
# Datos de proporción simulados (cercanos a la figura original)
porcentajes = [13.8, 11.7, 10.6, 10.0, 9.7, 9.5, 7.9, 7.1, 6.3]
# Combinación de colores libre (se puede ajustar, usando una serie azul como ejemplo)
color_barra = "#CB87EB"  # Puede reemplazarse con otros colores como "#FF8C00"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(problemas))
altura_barra = 0.6
barras = ax.barh(y, porcentajes, height=altura_barra, color=color_barra)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + altura_barra/2),
                xytext=(5, 0),  # Posición de la etiqueta: desplazamiento de 5 hacia la derecha
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(problemas)
# Establecer las marcas del eje x (0 - 15%)
ax.set_xlim(0, 15)
# Establecer el título
ax.set_title("Problemas de sueño reportados por los usuarios (TOP10)", fontsize=14, fontweight="bold")

# Mejora visual: Ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()