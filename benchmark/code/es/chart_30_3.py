import matplotlib.pyplot as plt
import numpy as np

# Título y lista de contenidos
titulo = "Atención sobre el conocimiento y prevención del SIDA"
elementos = [
    "Vías de transmisión del SIDA",
    "Síntomas iniciales del SIDA",
    "Cuánto tiempo pueden vivir las personas con SIDA",
    "Vacuna contra el SIDA",
    "Imágenes de los síntomas iniciales del SIDA",
    "Materiales de promoción del SIDA",
    "Imágenes del SIDA",
    "Tres principales manifestaciones de la fase latente del SIDA"
]
# Establecer valores de progreso según la proporción de longitud de las barras rojas en la imagen original
progreso = np.array([0.95, 0.85, 0.85, 0.85, 0.75, 0.74, 0.70, 0.70])  

# Crear un lienzo y un eje
fig, ax = plt.subplots(figsize=(6, 4), facecolor="#F5F5F5")
# Ocultar los ejes
ax.axis("off")  

# Dibujar el título
plt.text(
    0.03, 0.95, titulo, 
    fontsize=16, fontweight="bold", fontfamily="SimSun"
)

# Dibujar cada elemento uno por uno
for i, (texto, p) in enumerate(zip(elementos, progreso), start=1):
    # Dibujar el fondo de la barra de progreso
    rect_fondo = plt.Rectangle(
        (0.03, 0.9 - 0.1 * i), 0.94, 0.07, 
        facecolor="#F8D7DA", edgecolor="white"
    )
    ax.add_patch(rect_fondo)
    # Dibujar la parte rellena de la barra de progreso (utilizando diferentes valores de progreso)
    rect_llenado = plt.Rectangle(
        (0.03, 0.9 - 0.1 * i), 0.94 * p, 0.07, 
        facecolor="#F1C2C6", edgecolor="white"
    )
    ax.add_patch(rect_llenado)
    # Dibujar el texto del porcentaje de progreso
    plt.text(
        0.03 + 0.94 * p + 0.01, 0.9 - 0.1 * i + 0.035, f"{p*100:.0f}%", 
        fontsize=10, va="center", color="#8B0000"
    )
    # Dibujar el círculo del número de serie
    circulo = plt.Circle(
        (0.02, 0.9 - 0.1 * i + 0.035), 0.03, 
        facecolor=f"C{i-1}", edgecolor="white"
    )
    ax.add_artist(circulo)
    # Dibujar el texto del número de serie
    plt.text(
        0.02, 0.9 - 0.1 * i + 0.032, f"{i}", 
        fontsize=10, color="white", ha="center", va="center"
    )
    # Dibujar el texto del elemento
    plt.text(
        0.07, 0.9 - 0.1 * i + 0.035, texto, 
        fontsize=12, va="center"
    )

plt.tight_layout(pad=2)
plt.show()