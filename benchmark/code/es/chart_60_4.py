import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
motivaciones = [
    "Las gafas se desgastan, envejecen o se dañan, lo que afecta su uso",
    "Las gafas son incómodas de usar (visión incómoda / incomodidad en el armazón)",
    "Cambio en los requisitos funcionales de las gafas, obtener gafas funcionales",
    "Cambio en la visión / grado ocular",
    "Relajación local del armazón, uso inestable",
    "El consejo de un médico profesional para reemplazar / cambiar las gafas periódicamente",
    "Quiero cambiar de imagen / probar un nuevo estilo",
    "Las gafas originales se han usado durante mucho tiempo y han perdido su frescura",
    "Combinar nuevos estilos con los atuendos diarios",
    "Seguir la tendencia actual o imitar a celebridades / influencers (Seguir la tendencia actual o obtener el mismo estilo que celebridades / influencers)",
    "Satisfacer las necesidades de diferentes escenarios, colocar gafas en diferentes escenarios para un uso conveniente"
]
porcentajes = [39.2, 35.9, 35.5, 30.6, 30.6, 28.3, 24.0, 23.7, 19.5, 18.3, 14.8]  # Porcentaje (%)

# Configuración de color (similar al gradiente verde en la imagen original)
color_barra = "#a5d6a7"

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(motivaciones))

barras = ax.barh(
    y, 
    porcentajes, 
    color=color_barra, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar etiquetas de datos --------------------
for i, barra in enumerate(barras):
    ancho = barra.get_width()
    ax.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height()/2,
        f"{ancho}%",
        va="center",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Embelezar el gráfico --------------------
# Establecer etiquetas del eje y (descripciones de las motivaciones)
ax.set_yticks(y)
ax.set_yticklabels(motivaciones, fontsize=10, color="#424242")

# Ocultar el eje x
ax.set_xticks([])

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar un título
ax.set_title(
    "Motivaciones para cambiar de gafas",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()