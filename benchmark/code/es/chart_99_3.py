import matplotlib.pyplot as plt
import numpy as np

# Clasificación de escenarios comibles
escenarios = [
    "Después de la cena/la reunión", "Mientras se ven programas de televisión/televisión de variedades/películas",
    "Té de la tarde", "Durante el trabajo/estudio",
    "Después del deporte/entrenamiento", "Viaje al aire libre", "Escenario de comida casera"
]
# Simular datos de porcentaje (cerca de la figura original)
porcentajes = [64.0, 59.6, 55.4, 51.8, 47.5, 44.0, 42.2]
# Combinación de colores libres (se puede ajustar, usando la serie naranja como ejemplo)
color_barra = "#F6FF7A"  # Se puede reemplazar con otros colores como "#87CEEB"
# Índices de los primeros cuatro elementos cubiertos por el cuadro discontinuo azul
indices_cuadro_discontinuo = [0, 1, 2, 3]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(escenarios))
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
ax.set_yticklabels(escenarios)
# Establecer las marcas del eje x (0 - 70%)
ax.set_xlim(0, 70)
# Establecer el título
ax.set_title("Escenarios de consumo de frutas", fontsize=14, fontweight="bold")

# Embelezar: ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()
plt.show()