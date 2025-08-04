import matplotlib.pyplot as plt
import numpy as np

# Categorías de educación
educacion = ["Secundaria o inferior", "Título de asociado", "Licenciatura", "Maestría/MBA o superior"]
# Datos de porcentaje simulados (cerca de la figura original)
porcentajes = [15.0, 19.0, 54.3, 11.7]
# Color personalizado (ajustable)
color_barra = "#C6BF39"  # Verde básico, también se puede cambiar a otros colores como "#FF8C00"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(educacion))
altura_barra = 0.6  # Definir la variable altura_barra
barras = ax.barh(y, porcentajes, color=color_barra, height=altura_barra)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + altura_barra/2),
                xytext=(5, 0),  # Posición de la etiqueta: desplazamiento 5 hacia la derecha
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(educacion)
# Establecer las marcas del eje x (0 - 60%)
ax.set_xlim(0, 60)
# Establecer el título
ax.set_title("Nivel educativo de los aficionados al fútbol chino en 2022", fontsize=14, fontweight="bold")

# Embellir: Ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()