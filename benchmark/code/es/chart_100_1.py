import matplotlib.pyplot as plt
import numpy as np

# Clasificación de la retroalimentación sobre la calidad del sueño
etiquetas = ["Sin problemas, dormí muy bien", "Está bien, problemas de sueño ocasionales", "Sí, problemas de sueño ocasionales", "Sí, tengo problemas de sueño relativamente graves", "Sí, tengo problemas de sueño muy graves"]
# Simular datos de porcentaje (cercano a la imagen original)
porcentajes = [18.7, 47.0, 23.2, 8.7, 2.4]
# Esquema de color libre (puede ajustarse, usando la gama verde como ejemplo)
color_barra = "#6339C6"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras
x = np.arange(len(etiquetas))
ancho_barra = 0.5
barras = ax.bar(x, porcentajes, width=ancho_barra, color=color_barra)

# Agregar anotaciones de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width()/2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=40, ha='right', fontsize=9)
# Establecer las marcas del eje y (0 - 50%, adaptado a los datos)
ax.set_ylim(0, 50)
# Establecer el título
ax.set_title("Retroalimentación de los usuarios sobre la calidad de su propio sueño", fontsize=14, fontweight="bold")

# Emprolijar: Ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()
plt.show()