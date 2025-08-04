import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2018", "2019", "2020"]
# Área de almacenes generales (en cientos de millones de metros cuadrados), los datos pueden ser aproximadamente iguales
general_warehouse = [10.60, 10.80, 11.45]
# Área de almacenes de alta calidad (en cientos de millones de metros cuadrados), los datos pueden ser aproximadamente iguales
high_standard_warehouse = [3.00, 3.15, 3.45]

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(6, 5))

# Dibujar un gráfico de barras agrupadas
x = np.arange(len(years))
bar_width = 0.35
# Almacén general (verde)
general_bars = ax.bar(x - bar_width/2, general_warehouse, width=bar_width, color="#C63982", label="Almacén General (Cientos de Millones de Metros Cuadrados)")
# Almacén de alta calidad (azul)
high_standard_bars = ax.bar(x + bar_width/2, high_standard_warehouse, width=bar_width, color="#64B5F6", label="Almacén de Alta Calidad (Cientos de Millones de Metros Cuadrados)")

# Agregar etiquetas de datos para los almacenes generales
for bar in general_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos para los almacenes de alta calidad
for bar in high_standard_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Área (Cientos de Millones de Metros Cuadrados)")
# Establecer el título
ax.set_title("Área de Almacenes Generales y de Alta Calidad en China de 2018 a 2020", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='lower center')

# Embellir el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()