import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Categorías de población
grupos = ["Nueva generación de trabajadores intelectuales", "Generación Z", "Jóvenes de ciudades pequeñas", "Adultos mayores y personas de mediana edad de ciudades pequeñas", "Clase media alta", "Madres exquisitas", "Trabajadores industriales urbanos", "Adultos mayores urbanos"]
# Categorías de datos (correspondientes a la leyenda)
categorias = ["(Tmall Global) Proporción de la población total de belleza capilar y corporal", "(Taobao Tmall) Proporción de la población total de belleza capilar y corporal"]
# Datos simulados (ajustables), rango 0 - 25 (valores de ejemplo)
datos = np.array([
    [22, 12],  # Nueva generación de trabajadores intelectuales
    [20, 16],  # Generación Z
    [18, 17],  # Jóvenes de ciudades pequeñas
    [15, 24],  # Adultos mayores y personas de mediana edad de ciudades pequeñas
    [12, 8],   # Clase media alta
    [10, 5],   # Madres exquisitas
    [8, 15],   # Trabajadores industriales urbanos
    [3, 4]     # Adultos mayores urbanos
]).T  # Transpuesta de forma (2, 8) para coincidir con la estructura de plataforma - población

# Crear un lienzo
fig, ax = plt.subplots(figsize=(12, 6))

# Dibujar un gráfico de barras agrupadas
x = np.arange(len(grupos))
ancho_barra = 0.35
for i in range(len(categorias)):
    desplazamiento = ancho_barra * i
    ax.bar(x + desplazamiento, datos[i], width=ancho_barra, 
           color="#A4C639" if i == 0 else "#87CEEB",
           label=categorias[i])

# Agregar etiquetas de datos
for i in range(len(grupos)):
    for j in range(len(categorias)):
        altura = datos[j][i]
        ax.annotate(f'{altura}%',
                    xy=(x[i] + ancho_barra * j, altura),
                    xytext=(0, 3),  # Posición de la etiqueta: 3 puntos hacia arriba
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x + ancho_barra / 2)
ax.set_xticklabels(grupos, rotation=15, ha='right')  # Rotar las etiquetas para evitar superposiciones
# Establecer las marcas del eje y (0 - 40%)
ax.set_ylim(0, 40)
ax.set_yticks([0, 20, 40])
# Establecer el título
ax.set_title("Tmall Global: Proporción de las ocho principales poblaciones de \nproductos de consumo masivo de Taobao en belleza capilar y corporal", 
             fontsize=16, fontweight="bold", y=1.05)

# Leyenda personalizada
elementos_leyenda = [Patch(facecolor="#A4C639", label=categorias[0]),
                     Patch(facecolor="#87CEEB", label=categorias[1])]
ax.legend(handles=elementos_leyenda, loc="upper right")

# Emprolijar: Ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()