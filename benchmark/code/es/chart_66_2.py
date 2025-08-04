import matplotlib.pyplot as plt
import numpy as np

# Establece la fuente para mostrar correctamente el español
plt.rcParams["font.sans-serif"] = ["Arial"]
plt.rcParams["axes.unicode_minus"] = False

# Define grupos de edad y categorías en español
grupos_edad = ["Nacidos después de 1995", "Nacidos en los años 90", "Nacidos en los años 85", "Nacidos antes de 1985"]
categorias = ["Necesita suplementación diaria regular", "Suplementar solo cuando las mascotas presenten síntomas relevantes o estén en períodos especiales"]
datos = [[46, 52, 56, 54], [33, 35, 28, 30]]
colores = [["#C0C0C0", "#A4C639", "#8DB328", "#7EA11E"], 
           ["#A4C639", "#8DB328", "#C0C0C0", "#D3D3D3"]]

# Genera las coordenadas x para las barras
x = np.arange(len(grupos_edad))  
ancho = 0.35  

# Crea una figura y un eje
fig, ax = plt.subplots(figsize=(8, 5))

# Dibuja las barras para cada categoría
for i in range(len(categorias)):
    rectangulos = ax.bar(x + i * ancho, datos[i], ancho, color=colores[i], edgecolor="white", label=categorias[i])
    # Añade etiquetas de datos a las barras
    for rectangulo, etiqueta in zip(rectangulos, datos[i]):
        altura = rectangulo.get_height()
        ax.annotate(f'{etiqueta}%',
                    xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

# Establece las posiciones y etiquetas de las marcas en el eje x
ax.set_xticks(x + ancho / 2)
ax.set_xticklabels(grupos_edad)
# Establece el límite del eje y
ax.set_ylim(0, 60)
# Establece el título del gráfico
ax.set_title("Aceptación de productos de salud para mascotas entre diferentes grupos de edad", fontsize=14, fontweight="bold")

# Ajusta la posición de la leyenda, por ejemplo, colócala en el lado izquierdo fuera del gráfico
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))  

# Muestra el gráfico
plt.show()