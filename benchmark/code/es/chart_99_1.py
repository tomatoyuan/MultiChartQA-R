import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2015", "2016", "2017", "2018", "2019", "2020"]
# Datos de consumo simulados (kg, siguiendo la tendencia del gráfico original)
consumos = [40.5, 43.9, 45.6, 47.4, 51.4, 51.3]
# Colores a elección (pueden ajustarse, se usa naranja en el ejemplo)
color_linea = "#FF8C00"  # Puede reemplazarse con otros colores como "#32CD32"

# Crear un lienzo
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de línea
x = np.arange(len(años))
linea, = ax.plot(x, consumos, marker='o', color=color_linea, label="Peso (kg)")

# Añadir etiquetas de datos
for i, val in enumerate(consumos):
    ax.annotate(f'{val}',
                xy=(x[i], val),
                xytext=(5, 5),  # Posición de la etiqueta: desplazamiento de 5 puntos hacia la derecha y abajo
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(años)
# Establecer las marcas del eje y (35 - 55 kg, adecuado para los datos)
ax.set_ylim(35, 55)
# Establecer el título
ax.set_title("Consumo per cápita de frutas frescas de los residentes nacionales desde 2015 hasta 2020", fontsize=14, fontweight="bold")
# Añadir una leyenda
ax.legend()

# Mejora visual: Ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()
plt.show()