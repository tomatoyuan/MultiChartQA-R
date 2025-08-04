import matplotlib.pyplot as plt
import numpy as np

# Categorías de puntos problemáticos
puntos_problematicos = [
    "Equipamiento tradicional y no inteligente", "Equipamiento de función única", "Alta dependencia de mano de obra",
    "Ruido fuerte durante el uso del equipo", "Gran espacio ocupado por el equipo", "Alta tasa de daño del equipo",
    "Gran cantidad de humos durante el uso del equipo", "Corta vida útil y alta tasa de descarte del equipo",
    "Alto costo del equipo y difícil recuperación de la inversión", "Baja eficiencia de operación/servicio del equipo",
    "Operación compleja e inconveniente del equipo"
]
# Datos de proporción simulados (se pueden ajustar, los tres primeros son similares a la figura original)
porcentajes = [48.9, 48.1, 48.1, 37.6, 36.8, 33.8, 28.6, 27.8, 25.6, 24.8, 16.5]
# Índices de los tres primeros elementos cubiertos por el cuadro discontinuo azul
indices_cuadro_discontinuo = [0, 1, 2]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 7))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(puntos_problematicos))
altura_barra = 0.6
barras = ax.barh(y, porcentajes, height=altura_barra, color="#A4C639")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + altura_barra/2),
                xytext=(5, 0),  # Posición de la etiqueta: desplazamiento de 5 hacia la derecha
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Dibujar un cuadro discontinuo azul
min_y = min([barras[i].get_y() for i in indices_cuadro_discontinuo])
max_y = max([barras[i].get_y() + altura_barra for i in indices_cuadro_discontinuo])
max_ancho = max([barras[i].get_width() for i in indices_cuadro_discontinuo])

# Dibujar el cuadro discontinuo (arriba, derecha, abajo, izquierda)
ax.plot([0, max_ancho], [max_y, max_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([max_ancho, max_ancho], [min_y, max_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([0, max_ancho], [min_y, min_y], linestyle='--', color='lightblue', linewidth=1)
ax.plot([0, 0], [min_y, max_y], linestyle='--', color='lightblue', linewidth=1)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(puntos_problematicos)
# Establecer las marcas del eje x (0 - 50%)
ax.set_xlim(0, 55)
# Establecer el título
ax.set_title("Puntos problemáticos en el uso de electrodomésticos de cocina", fontsize=14, fontweight="bold")

# Ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()
plt.show()