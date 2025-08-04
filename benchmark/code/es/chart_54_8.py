import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
categorias = [
    "Mejorar la inmunidad y aumentar la resistencia",
    "Mejorar el sueño",
    "Suplementar energía y mantenerse enérgico",
    "Mejorar la salud gastrointestinal",
    "Garantizar una ingesta nutricional equilibrada",
    "Mejorar la salud de los ojos/visión",
    "Aumentar el nivel metabólico",
    "Mejorar la memoria",
    "Regular el sistema endocrino",
    "Mejorar la salud de huesos y articulaciones"
]

# Datos simulados (los primeros 3 son verdes, el resto son grises)
porcentajes = [75.7, 57.9, 47.7, 46.9, 44.9, 43.8, 35.6, 35.0, 34.4, 33.3]

# Configuración de colores (los primeros 3 son verdes, el resto son grises)
colores = ["#a5d6a7"]*3 + ["#dcdcdc"]*(len(categorias)-3)

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(10, 6))

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

# -------------------- Agregar anotaciones de porcentaje --------------------
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

# Ocultar el marco
for espina in ax.spines.values():
    espina.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar marcas de graduación del eje y

# Agregar un título
ax.set_title(
    "Propósitos de los residentes al tomar suplementos nutricionales dietéticos (%)",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()