import matplotlib.pyplot as plt
import numpy as np

# Categorías de preferencias de alojamiento
categorias = ["Higiene y Seguridad", "Experiencia Única", "Programas para Familias", "Apto para Mascotas", "Lugares para Fotos", "Todo Incluido", "Otros"]
# Datos correspondientes (proporción), los datos pueden ser aproximadamente iguales
datos = [91.2, 49.8, 36.6, 28.7, 27.0, 12.0, 10.5]
# Configuración de color, similar al esquema de color verde de la imagen original
color = "#C6395C"

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
barras = ax.bar(x, datos, width=ancho_barra, color=color, edgecolor="white")

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=25)
# Ocultar las marcas del eje y
ax.set_yticks([])
# Establecer el título
ax.set_title("Preferencias de Alojamiento de los Micro - vacacionistas", fontsize=14, fontweight="bold")

# Hacer el gráfico más bonito, ocultar los bordes superior, derecho e inferior
for espina in ["top", "right", "bottom"]:
    ax.spines[espina].set_visible(False)

plt.show()