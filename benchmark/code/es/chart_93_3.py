import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Categorías de población
grupos = ["Población femenina", "Población con educación posgraduada", "Población menor de 30 años", "Población en ciudades de primer y segundo nivel", "Población de altos ingresos", "Población de alto consumo"]
# Categorías de datos (correspondientes a la leyenda)
categorias = ["(Tmall Global) Proporción de la población total de belleza capilar", "(Tmall + Taobao) Proporción de la población total de belleza capilar"]
# Corregir la estructura de datos: transponer para coincidir con las categorías de población (6 categorías)
datos = np.array([
    [85, 55, 60, 65, 50, 40],  # Tmall Global: Proporción de cada población
    [70, 35, 50, 55, 38, 20]   # Tmall + Taobao: Proporción de cada población
]).T  # Después de transponer, la forma es (6, 2), coincidiendo con el número de categorías de población

# Texto de anotación
texto_anotacion = "Tmall Global tiene más personas con alta educación y alto consumo."
# Parámetros de la flecha
propiedades_flecha = dict(arrowstyle="->", color="green", connectionstyle="arc3,rad=0.2")

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 7))

# Dibujar un gráfico de barras horizontales agrupadas
y = np.arange(len(grupos))
altura_barra = 0.35
for i in range(len(categorias)):
    desplazamiento = altura_barra * i
    ax.barh(y + desplazamiento, datos[:, i], height=altura_barra, 
            color="#A4C639" if i==0 else "#EBD487",
            label=categorias[i])

# Agregar anotaciones de datos
for i in range(len(grupos)):
    for j in range(len(categorias)):
        ancho = datos[i, j]
        ax.annotate(f'{ancho}%',
                    xy=(ancho, y[i] + altura_barra*j),
                    xytext=(5, 0),  # Posición de la anotación: desplazamiento de 5 hacia la derecha
                    textcoords="offset points",
                    ha='left', va='center',
                    color='black')

# Establecer las marcas y etiquetas del eje y (centrar la visualización agrupada)
ax.set_yticks(y + altura_barra/2)
ax.set_yticklabels(grupos)
# Establecer las marcas del eje x (0 - 100%)
ax.set_xlim(0, 100)
ax.set_xticks([0, 50, 100])
# Establecer el título
ax.set_title("Retrato de la población de belleza capilar: Tmall Global vs Tmall + Taobao", 
             fontsize=16, fontweight="bold", y=1.03)

# Leyenda personalizada
elementos_leyenda = [Patch(facecolor="#A4C639", label=categorias[0]),
                   Patch(facecolor="#EBD487", label=categorias[1])]
ax.legend(handles=elementos_leyenda, loc="right")

# Embellir: ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()