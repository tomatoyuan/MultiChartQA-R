import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ['2022', '2030E']
valores = [8.2, 17.4]

# Se utiliza para mostrar la tasa de crecimiento anual compuesto en una posición adecuada por encima del gráfico de barras. Aquí, simplemente se establece por encima del centro de las dos barras.
x_pos = 0.5
y_pos = max(valores) + 1

# Crear una figura y ejes
fig, ax = plt.subplots()

# Dibujar un gráfico de barras
ax.bar(años, valores, color='skyblue')

# Agregar etiquetas de datos
for x, y in zip(años, valores):
    ax.text(x, y + 0.2, f'{y}', ha='center', va='bottom')

# Establecer el título
ax.set_title('Tamaño y perspectiva del mercado de sillas ergonómicas \nen China desde 2022 hasta 2030 (en miles de millones de dólares estadounidenses)')

# Mostrar la figura
plt.show()