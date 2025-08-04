import matplotlib.pyplot as plt
import numpy as np

# Datos (ordenados en orden descendente)
universidades = [
    "Universidad de Harvard", "Instituto Tecnológico de Massachusetts", "Universidad de Stanford",
    "Universidad Johns Hopkins", "Universidad de California, Berkeley",
    "Universidad de Washington, Seattle", "Universidad de Toronto",
    "Universidad de Oxford", "Universidad de California, Los Ángeles", "Universidad College London"
]

# Proporción de búsquedas (ordenada en orden descendente)
proporcion_busqueda = [1.0, 0.9, 0.85, 0.7, 0.65, 0.6, 0.5, 0.45, 0.4, 0.3]

# Esquema de colores (contraste mejorado)
colores = [
    "#FF5252", "#FF9800", "#FFEB3B",
    "#42A5F5", "#42A5F5", "#42A5F5",
    "#5C6BC0", "#5C6BC0", "#5C6BC0", "#5C6BC0"
]

# Crear un lienzo (aumentar la claridad)
plt.rcParams['figure.dpi'] = 300
fig, ax = plt.subplots(figsize=(10, 7), facecolor="#E8F5E9")

# Invertir el orden de los datos
universidades = universidades[::-1]
proporcion_busqueda = proporcion_busqueda[::-1]
colores = colores[::-1]  # Invertir los colores si es necesario mantener la correspondencia de colores

# Dibujar un gráfico de barras horizontales (agregar efecto de sombra)
barras = ax.barh(universidades, proporcion_busqueda, color=colores, height=0.7,
                 edgecolor='black', linewidth=0.5, alpha=0.9)

# Agregar un título (mejorar el diseño)
fondo_titulo = plt.Rectangle((0, 1.02), 1, 0.1, color="#D32F2F", transform=ax.transAxes,
                             clip_on=False, zorder=3)
ax.add_patch(fondo_titulo)
ax.text(0.5, 1.06, "Principales Universidades Extranjeras Más Concurridas",
        fontsize=18, fontweight="bold", color="white",
        transform=ax.transAxes, va="center", ha="center")

# Agregar la etiqueta "Índice de Búsqueda" (mejorar la posición)
ax.text(-0.15, 0.98, "Índice de Búsqueda",
        fontsize=14, fontweight="bold", color="#D32F2F",
        transform=ax.transAxes, va="center", rotation=0)

# Embelezar las etiquetas del eje y (agregar relleno y bordes)
for i, txt in enumerate(ax.get_yticklabels()):
    txt.set_bbox(dict(facecolor='white', alpha=0.7, edgecolor='gray', boxstyle='round,pad=0.3'))

# Ocultar los bordes y las marcas
ax.spines[:].set_visible(False)
ax.set_xticks([])
ax.tick_params(axis='y', labelsize=12, pad=15)

# Agregar líneas de cuadrícula (dirección horizontal)
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Agregar una línea decorativa en la parte inferior
linea_pie = plt.Line2D([0, 1], [-0.03, -0.03], color='#D32F2F',
                       transform=ax.transAxes, linewidth=3, clip_on=False)
ax.add_artist(linea_pie)

plt.tight_layout()
plt.show()