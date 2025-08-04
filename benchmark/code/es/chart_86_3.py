import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2019", "2020", "2021"]
# Cantidad de temas de programas de variedades femeninos, los datos son consistentes con el gráfico
quantity = [4, 7, 10]

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de barras
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, quantity, width=bar_width, color="#C6395A")

# Agregar etiquetas de datos
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C6395A")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title("Tendencia de temas de programas de variedades femeninos SVC de 2019 a 2021", fontsize=14, fontweight="bold")

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()