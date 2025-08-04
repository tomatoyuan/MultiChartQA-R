import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# Lugares de consumo
lugares = ["Restaurantes de alta y media gama", "Restaurantes populares", "Hogar/Dormitorio", "Bares/Pubs", "Otros"]
# Proporción de personas de 18 - 29 años (%)
edad18_29 = [41.7, 21.1, 18.6, 10.8, 7.8]
# Proporción de personas de 30 años y mayores (%)
edad30_mas = [30.6, 34.7, 19.8, 11.2, 3.7]
# Proporciones de referencia para la anotación central (para alineación)
tazas_ref = [35.4, 28.8, 19.3, 11.0, 5.5]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales para personas de 18 - 29 años (verde)
y = np.arange(len(lugares))
ancho_barra = 0.35
barras1 = ax.barh(y + ancho_barra/2, edad18_29, height=ancho_barra, color="#A4C639", label="Proporción de personas de 18 - 29 años (%)")
# Dibujar un gráfico de barras horizontales para personas de 30 años y mayores (azul)
barras2 = ax.barh(y - ancho_barra/2, edad30_mas, height=ancho_barra, color="#87CEEB", label="Proporción de personas de 30 años y mayores (%)")

# Agregar anotaciones de datos para personas de 18 - 29 años
for i, barra in enumerate(barras1):
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(-5, 0),  # Anotación a la izquierda
                textcoords="offset points",
                ha='right', va='center',
                color='white' if i == 0 else 'black')  # La primera anotación es blanca (simulando énfasis en círculo rojo)

# Agregar anotaciones de datos para personas de 30 años y mayores
for i, barra in enumerate(barras2):
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Anotación a la derecha
                textcoords="offset points",
                ha='left', va='center',
                color='white' if i == 1 else 'black')  # La segunda anotación es blanca (simulando énfasis en círculo rojo)

# Establecer las marcas y etiquetas del eje y (ajustar la posición para centrar las categorías)
ax.set_yticks(y)
ax.set_yticklabels(lugares)
ax.set_yticklabels(lugares, ha='center', va='center')

# Establecer el título
ax.set_title("Lugares de consumo de licor", fontsize=16, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='upper right')

# Embelezar: Ocultar los bordes superior, derecho e inferior
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

# Ajustar el rango del eje x para dejar espacio para las anotaciones
ax.set_xlim(0, max(max(edad18_29), max(edad30_mas)) + 10)

plt.tight_layout()
plt.show()