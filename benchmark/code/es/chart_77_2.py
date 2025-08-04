import matplotlib.pyplot as plt
import numpy as np

# Categorías de cambio de rendimiento
categorias = ["Crecimiento por encima del 20%", "Crecimiento dentro del 20%", "Declive dentro del 20%", "Declive por encima del 20%"]
# Datos de instituciones de aprendizaje en línea (%)
en_linea = [51, 31, 16, 2]
# Datos de proveedores de capacitación (%)
proveedor = [16, 31, 43, 11]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras agrupadas
x = np.arange(len(categorias))
ancho_barra = 0.35
barras_en_linea = ax.bar(x - ancho_barra/2, en_linea, width=ancho_barra, color="#C68439", label="Instituciones de Aprendizaje en Línea")
barras_proveedor = ax.bar(x + ancho_barra/2, proveedor, width=ancho_barra, color="#64B5F6", label="Proveedores de Capacitación")

# Agregar etiquetas de datos para instituciones de aprendizaje en línea
for barra in barras_en_linea:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos para proveedores de capacitación
for barra in barras_proveedor:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Establecer la etiqueta del eje y
ax.set_ylabel("Proporción (%)")
# Establecer el título
ax.set_title("Rendimiento de Instituciones de Aprendizaje en Línea y Proveedores de Capacitación en 2021", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embellir el gráfico, ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()