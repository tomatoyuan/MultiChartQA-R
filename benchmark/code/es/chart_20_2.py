import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
constelaciones = [
    "Tauro", "Acuario", "Capricornio", "Leo", "Piscis", "Aries", "Sagitario", "Cáncer",
    "Libra", "Géminis", "Virgo", "Escorpio"
]
porcentajes = [4, 4, 7, 10, 5, 9, 6, 6, 6, 10, 18, 15]
# Establecer manualmente las coordenadas de cada constelación para facilitar el diseño (se pueden ajustar según el diseño)
coords = [
    (0.2, 0.8), (0.1, 0.6), (0.3, 0.4), (0.2, 0.2), (0.4, 0.1), (0.6, 0.2),
    (0.7, 0.3), (0.8, 0.5), (0.7, 0.7), (0.5, 0.8), (0.6, 0.6), (0.4, 0.7)
]
# Colores de las burbujas correspondientes (esquema de colores de ejemplo, se pueden ajustar)
colores = [
    "#D4AF37", "#ADD8E6", "#C0C0C0", "#87CEFA", "#F0E68C", "#90EE90",
    "#FFD700", "#FF6347", "#FFC0CB", "#BA55D3", "#FF69B4", "#1E90FF"
]
# Texto de anotación especial para Virgo
texto_virgo = "Aunque Virgo es noble y distante,\n lo más hábil que hace es esconder la ansiedad."

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
# Ocultar los ejes
ax.set_xticks([])
ax.set_yticks([])

# Dibujar burbujas + anotaciones
for constelacion, p, (x, y), color in zip(constelaciones, porcentajes, coords, colores):
    # Dibujar burbujas (simuladas por un diagrama de dispersión)
    ax.scatter(
        x, y, 
        s=p * 120,  # El tamaño de la burbuja está relacionado con el porcentaje de ansiedad
        c=color, 
        alpha=0.8,
        edgecolors='white', 
        linewidths=1
    )
    # Dibujar el texto del porcentaje
    color_texto = 'white' if p != 18 else 'black'  # Invertir el color del texto para Virgo
    ax.text(
        x, y, 
        f"{p}%", 
        ha='center', 
        va='center', 
        fontsize=10, 
        color=color_texto, 
        fontweight='bold'
    )
    # Dibujar el nombre de la constelación
    ax.text(
        x, y - 0.05, 
        constelacion, 
        ha='center', 
        va='top', 
        fontsize=9, 
        color='white'
    )

# Texto de descripción especial para Virgo
virgo_x, virgo_y = coords[constelaciones.index("Virgo")]
ax.text(
    virgo_x, virgo_y - 0.18, 
    texto_virgo, 
    ha='center', 
    va='bottom', 
    fontsize=10, 
    color='white', 
    linespacing=1.2,
    # Fix: Cambiar el formato de color CSS al formato de tupla RGBA
    bbox=dict(facecolor=(1, 1, 1, 0.1), edgecolor='white', pad=5)
)

# Agregar un título
ax.text(
    0.5, 0.95, 
    "Ranking de las constelaciones más ansiosas", 
    ha='center', 
    va='center', 
    fontsize=20, 
    color='white', 
    fontweight='bold'
)

plt.tight_layout()
plt.show()