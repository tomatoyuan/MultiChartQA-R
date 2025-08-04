import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2016", "2017", "2018", "2019", "2020", "2021", "2022e"]
# Datos de porcentaje de ventas simulados (cerca del gráfico original)
porcentajes = [5.4, 7.5, 12.7, 14.7, 20.6, 23.4, 27.3]
# Color libre para la coincidencia (se puede ajustar, se usa verde + azul en el ejemplo)
color_barra = "#87CEEB"  # Se puede reemplazar con otros colores como "#FF8C00"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras
x = np.arange(len(años))
ancho_barra = 0.6
barras = ax.bar(x, porcentajes, width=ancho_barra, color=color_barra)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + ancho_barra/2, altura),
                xytext=(0, 3),  # Posición de la etiqueta: desplazamiento 3 hacia arriba
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(años)
# Establecer las marcas del eje y (0 - 30%)
ax.set_ylim(0, 30)
# Establecer el título
ax.set_title("Proporción de ventas y pronóstico de bicicletas de dos ruedas con batería de litio en China desde 2016 hasta 2022", fontsize=14, fontweight="bold")

# Mejorar: ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()
plt.show()