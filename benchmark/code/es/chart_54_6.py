import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
categorias = [
    "Problemas de sueño",
    "Fácil fatiga/falta de energía",
    "Alto estrés mental",
    "Problemas de inmunidad (poca o ninguna enfermedad)",
    "Problemas de salud de la piel",
    "Problemas de visión",
    "Problemas de cabello (por ejemplo, pérdida de cabello)",
    "Dolor de hombros y cuello",
    "Bajo estado de ánimo/ansiedad",
    "Problemas de memoria",
    "Antienvejecimiento",
    "Problemas endocrinos",
    "Problemas de las tres altas",
    "Obesidad/sobrepeso",
    "Problemas cardiovasculares y cerebrovasculares",
    "Problemas óseos y articulares",
    "Depresión",
    "Diabetes"
]

# Datos simulados (los primeros 3 elementos son verdes, el resto son grises)
porcentajes = [61.1, 50.5, 48.9, 45.9, 44.2, 43.3, 42.2, 42.1, 40.8, 36.9, 28.1, 22.9, 20.7, 20.7, 15.5, 15.5, 9.3, 5.3]

# Configuración de colores (los primeros 3 elementos son verdes, el resto son grises)
colores = ["#a5d6a7"]*3 + ["#dcdcdc"]*(len(categorias)-3)

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(10, 8))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(categorias))

barras = ax.barh(
    y, 
    porcentajes, 
    color=colores, 
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar etiquetas de porcentaje --------------------
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height()/2,
        f"{ancho}",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# -------------------- Embelezar el gráfico --------------------
# Establecer etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(categorias, fontsize=11, color="#424242")

# Ocultar el eje x
ax.set_xticks([])

# Ocultar los bordes
for espina in ax.spines.values():
    espina.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar las marcas de graduación del eje y

# Agregar un título
ax.set_title(
    "Preocupaciones de salud de adultos de 18 - 65 años (%)",
    fontsize=14,
    fontweight="bold",
    pad=20,
    loc="right"  # Simular la posición del título de la imagen original
)

# Ajustar el diseño
plt.tight_layout()

plt.show()