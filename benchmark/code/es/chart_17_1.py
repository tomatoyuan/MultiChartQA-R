import matplotlib.pyplot as plt
import numpy as np

# Datos de fechas
fechas = ['8-21', '8-23', '8-25', '8-27', '8-29', '8-31', '9-02', '9-04', '9-06']
# Datos de popularidad de búsqueda. Puedes ajustarlos según los valores reales en el gráfico. Aquí es para demostración.
popularidad_busqueda = [32000, 26000, 19000, 14000, 17500, 31000, 11500, 9000, 19500]

x = np.arange(len(fechas))  # Coordenadas del eje x

fig, ax = plt.subplots()
# Dibujar un gráfico de barras
rects = ax.bar(x, popularidad_busqueda, color=['r', 'r', 'gold', 'b', 'orange', 'r', 'lightgreen', 'b', 'r'])

# Establecer las etiquetas de las marcas en el eje x
ax.set_xticks(x)
ax.set_xticklabels(fechas)
# Establecer el rango del eje y
ax.set_ylim(0, 35000)
# Establecer el título y las etiquetas de los ejes
ax.set_title('Popularidad de Búsqueda de Fraude en Telecomunicaciones')
ax.set_ylabel('Popularidad de Búsqueda')

# Anotar los valores en las barras (Opcional. Puedes omitir esto si quieres que sea más parecido al gráfico original)
for rect in rects:
    altura = rect.get_height()
    ax.annotate('{}'.format(altura),
                xy=(rect.get_x() + rect.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()