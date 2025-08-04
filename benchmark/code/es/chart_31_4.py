import matplotlib.pyplot as plt
import numpy as np

# Datos del canal de quejas
nombres_canales = ["Sitio web", "Teléfono", "Email, etc."]
porcentajes_canales = [68, 22, 10]

# Crear un lienzo y un subgráfico
plt.figure(figsize=(8, 6))
ax = plt.subplot(111)

# Dibujar un gráfico de barras de la proporción de los canales de quejas
barras = ax.bar(
    nombres_canales, 
    porcentajes_canales, 
    color=["#FF7F50", "#FF6347", "#FFD700"],  # Mantener el esquema de colores original
    width=0.6  # Ajustar el ancho de las barras
)

# Establecer el título del gráfico y las etiquetas de los ejes
ax.set_title("Distribución de Proporción de Canales de Quejas por Infracción", fontsize=16, fontweight="bold", pad=15)
ax.set_ylabel("Proporción (%)", fontsize=12)
ax.set_ylim(0, 100)  # Establecer el rango del eje y de 0 - 100%

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width()/2., 
        altura + 1.5,  # Ajustar la posición de la etiqueta
        f"{altura}%",
        ha="center", 
        va="bottom",
        fontsize=12
    )

# Establecer líneas de cuadrícula y fondo
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.set_axisbelow(True)  # Colocar las líneas de cuadrícula en la capa inferior

# Optimizar el diseño
plt.tight_layout()
plt.show()