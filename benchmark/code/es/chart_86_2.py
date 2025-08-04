import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2019", "2020", "2021"]
# Proporción de programas de variedades femeninos (%)
percentage = [9.8, 10.5, 14.7]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de líneas
line, = ax.plot(years, percentage, marker='o', color="#C6395A", label="Proporción de programas de variedades femeninos (%)", linewidth=2)

# Agregar etiquetas de datos
for x, y in zip(years, percentage):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 15),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title("SVC - Tendencia de la proporción de programas de variedades femeninos de 2019 a 2021", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='upper left')

# Embellir el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()