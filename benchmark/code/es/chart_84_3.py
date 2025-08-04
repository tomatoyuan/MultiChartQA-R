import matplotlib.pyplot as plt
import numpy as np

# Categorías de satisfacción
categorias = ["Muy Satisfecho", "Satisfecho", "Promedio", "Insatisfecho"]
# Porcentajes correspondientes (%)
porcentajes = [14.5, 45.7, 32.7, 7.1]

# Crear un lienzo y sub - gráfico
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
barras = ax.bar(x, porcentajes, width=ancho_barra, color="#A4C639")

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Dibujar un borde rojo para resaltar "Muy Satisfecho" y "Satisfecho"
x1, y1 = barras[0].get_xy()
x2, y2 = barras[1].get_xy() + np.array([barras[1].get_width(), barras[1].get_height()])
rect = plt.Rectangle((x1 - 0.1, y1 - 0.1), x2 - x1 + 0.2, y2 - y1 + 0.2,
                     fill=False, edgecolor='red', linewidth=2, linestyle='--')
ax.add_patch(rect)

# Agregar texto explicativo
ax.text(0.7, 0.9, "Casi el 60% de los residentes está satisfecho con su estado de salud actual",
        transform=ax.transAxes, fontsize=12, color='red', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Establecer la etiqueta del eje y
ax.set_ylabel("Porcentaje de evaluación de satisfacción con la salud (%)")
# Establecer el título
ax.set_title("Satisfacción con la salud de los residentes de China en 2022", fontsize=14, fontweight="bold")

# Mejorar la apariencia del gráfico, ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()  
plt.show()