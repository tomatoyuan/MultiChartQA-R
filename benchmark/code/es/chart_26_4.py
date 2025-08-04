import matplotlib.pyplot as plt
import numpy as np

# Datos
grupos_edad = ["Menos de 19 años", "Entre 19 y 24 años", "Entre 25 y 34 años", "Entre 35 y 49 años", "50 años o más"]
porcentajes_hombres = [13, 37, 41, 8, 1]
porcentajes_mujeres = [20, 47, 27, 5, 1]

x = np.arange(len(grupos_edad))  # Posiciones en el eje x
ancho = 0.35  # Ancho de las barras

# Crear una figura y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar las barras agrupadas para hombres y mujeres
rects_hombres = ax.bar(x - ancho/2, porcentajes_hombres, ancho, label="Grupo de hombres", color="#4CAF50")
rects_mujeres = ax.bar(x + ancho/2, porcentajes_mujeres, ancho, label="Grupo de mujeres", color="#F44336")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(grupos_edad)
# Establecer la etiqueta del eje y
ax.set_ylabel("Porcentaje de atención (%)")
# Establecer el título
ax.set_title('Distribución de género - edad de la atención a "Regalos de San Valentín"')
# Añadir una leyenda
ax.legend()

# Anotar los valores en las barras
def autolabel(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate('{}%'.format(altura),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Distancia vertical de la etiqueta del valor desde la barra
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects_hombres)
autolabel(rects_mujeres)

# Ajustar el diseño y mostrar el gráfico
plt.tight_layout()
plt.show()