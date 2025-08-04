import matplotlib.pyplot as plt
import numpy as np

# Definición de datos (correspondiente a la estructura de la imagen original, los valores se pueden ajustar)
categorias = ["Mañana", "Horario diurno", "Noche (incluyendo madrugada)", "Tiempo fragmentado no fijo"]
valores = [3.0, 24.8, 53.2, 19.0]  # Datos simulados, se pueden reemplazar con valores reales
etiqueta_especial = {
    "Noche (incluyendo madrugada)": "TGI de estudiantes de posgrado = 121\nTGI de la región centro - China = 130"
}

# Configuración de colores (cercano al esquema de color verde de la imagen original)
color_barra = "#81c784"
color_borde = "#dcedc1"  # Color de la caja discontinua

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(categorias))
barras = ax.barh(y, valores, color=color_barra, height=0.6, edgecolor="white", linewidth=1)

# Agregar anotaciones numéricas
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 1,  # Desplazamiento de 1 unidad hacia la derecha
        barra.get_y() + barra.get_height()/2,
        f"{ancho}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# Dibujar una caja discontinua para la dimensión especial (Noche)
indice_objetivo = categorias.index("Noche (incluyendo madrugada)")
barra_objetivo = barras[indice_objetivo]
x0, y0 = barra_objetivo.get_xy()
w, h = barra_objetivo.get_width(), barra_objetivo.get_height()
# Dibujar un rectángulo discontinuo
rect = plt.Rectangle(
    (x0 - 0.2, y0 - 0.1),  # Expandir el margen hacia afuera un poco
    w + 0.4, h + 0.2,
    fill=False,
    linestyle="--",
    color=color_borde,
    linewidth=2
)
ax.add_patch(rect)

# Agregar anotaciones de texto para la dimensión especial (TGI de estudiantes de posgrado, etc.)
if "Noche (incluyendo madrugada)" in etiqueta_especial:
    ax.text(
        x0 + w + 7,  # Desplazamiento hacia la derecha
        y0 + h/2,
        etiqueta_especial["Noche (incluyendo madrugada)"],
        va="center",
        fontsize=9,
        color="#424242",
        linespacing=1.2
    )

# Embellir el gráfico
ax.set_yticks(y)
ax.set_yticklabels(categorias, fontsize=12, color="#424242")
ax.set_xticks([])  # Ocultar las marcas de graduación del eje x
# Ocultar el borde
for espina in ax.spines.values():
    espina.set_visible(False)
ax.tick_params(axis="y", left=False)  # Ocultar las líneas de graduación del eje y

# Agregar un título
ax.set_title(
    "Momento en el que los estudiantes universitarios más a menudo escriben trabajos",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño (centrar el contenido)
plt.subplots_adjust(left=0.2, right=0.7, top=0.85, bottom=0.1)

plt.show()