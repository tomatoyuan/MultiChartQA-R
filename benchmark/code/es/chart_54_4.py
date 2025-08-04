import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
categorias = [
    "Problemas de visión",
    "Problemas de crecimiento y desarrollo",
    "Problemas de inmunidad",
    "Fortalecer los huesos/Promover el desarrollo óseo",
    "Concentración",
    "Alto estrés mental",
    "Problemas de memoria",
    "Promover la digestión gastrointestinal",
    "Estado de ánimo bajo",
    "Problemas de sueño (por ejemplo, insomnio, sueño ligero)",
    "Problemas de salud de la piel (por ejemplo, acné)",
    "Fácil fatiga/Falta de energía",
    "Obesidad/Sobrepeso",
    "Problemas de cabello (por ejemplo, pérdida de cabello)",
    "Depresión",
    "Problemas de tres altas (alta lipidemia/presión/sugar)",
    "Diabetes"
]

# Datos simulados (los primeros 4 elementos son verdes, el resto son grises)
porcentajes = [61.1, 55.6, 52.5, 49.1, 41.3, 36.2, 34.6, 34.2, 26.6, 24.5, 24.3, 21.2, 19.7, 12.3, 10.9, 6.7, 4.5]

# Configuración de colores (los primeros 4 elementos son verdes, el resto son grises)
colores = ["#a5d6a7"]*4 + ["#dcdcdc"]*(len(categorias)-4)

# -------------------- Crear un lienzo --------------------
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
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar las marcas de graduación del eje y

# Agregar un título
ax.set_title(
    "Preocupaciones de salud de adolescentes de 7 a 17 años (%)",
    fontsize=14,
    fontweight="bold",
    pad=20,
    loc="right"  # Simular la posición del título de la imagen original
)

# Ajustar el diseño
plt.tight_layout()

plt.show()