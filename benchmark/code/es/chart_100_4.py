import matplotlib.pyplot as plt
import numpy as np

# Los 10 principales factores que afectan el sueño
factores = [
    "No puedo resistirme a usar teléfonos móviles/tabletas antes de dormir", "Estoy acostumbrado a acostarme tarde sin motivación para cambiar",
    "El alto estrés de la vida afecta el descanso", "Acostarme tarde para estudiar o trabajar afecta el descanso",
    "Acostarme tarde de forma vengativa por la falta de libertad durante el día",
    "Mala aislamiento acústico del dormitorio y ambiente ruidoso", "Los compañeros de habitación/pareja afectan mi sueño",
    "Colchones, almohadas, etc. incómodos", "Temperatura y humedad inapropiadas en el dormitorio",
    "Enfermedades físicas afectan el sueño"
]
# Datos de porcentaje simulados (cerca del gráfico original)
porcentajes = [15.9, 13.6, 12.9, 9.5, 8.1, 7.2, 6.2, 5.6, 4.5, 3.5]
# Combinación de colores libre (ajustable, usando azul en el ejemplo)
color_barra = "#87CEEB"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(factores))
altura_barra = 0.6
barras = ax.barh(y, porcentajes, height=altura_barra, color=color_barra)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + altura_barra / 2),
                xytext=(5, 0),
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(factores)
# Establecer las marcas del eje x (0 - 17%, adecuado para los datos)
ax.set_xlim(0, 17)
# Establecer el título
ax.set_title("Los 10 principales factores que afectan el sueño", fontsize=14, fontweight="bold")

# Mejora visual: Ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()