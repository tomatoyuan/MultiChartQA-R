import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
cantidades = [177, 201, 238, 290, 341, 377, 457, 474, 438]

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras, utilizando un patrón similar a una gorra de graduación (simplificado como un gráfico de barras naranja, se puede reemplazar con un patrón personalizado)
barras = ax.bar(x, cantidades, color='orange')

# Agregar anotaciones numéricas encima de las barras
for i, cantidad in enumerate(cantidades):
    ax.text(i, cantidad + 10, f'{cantidad}', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Cantidad (en diez miles de personas)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)

ax.set_title('Escala de candidatos al examen de admisión a posgrado en China de 2016 a 2024')

plt.tight_layout()
plt.show()