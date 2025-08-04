import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
provincias = ["Hubei", "Zhejiang"]
# Cada Juegos Olímpicos (Nota: Los Juegos Olímpicos de la 24ª edición aparecen dos veces en los datos originales. Aquí, los procesamos según el orden de los títulos de columna.)
juegos = ["23ª", "24ª", "24ª", "26ª", "27ª", "28ª", "29ª", "30ª"]
# Medallas de oro de Hubei
hubei_medallas_oro = [1, 1, 3, 4, 6, 4, 5, 2]
# Medallas de oro de Zhejiang
zhejiang_medallas_oro = [2, 1, 1, 1, 1, 4, 2, 4]

x = np.arange(len(juegos))  # Posiciones de las marcas en el eje x
ancho = 0.35  # Ancho de las barras

fig, ax = plt.subplots()
# Graficar datos de Hubei
rects1 = ax.bar(x - ancho/2, hubei_medallas_oro, ancho, label='Hubei')
# Graficar datos de Zhejiang
rects2 = ax.bar(x + ancho/2, zhejiang_medallas_oro, ancho, label='Zhejiang')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(juegos)
# Título del eje y
ax.set_ylabel('Número de medallas de oro')
# Título del gráfico
ax.set_title('Comparación de medallas de oro en cada Juegos Olímpicos entre Hubei y Zhejiang')
ax.legend()  # Mostrar la leyenda

# Añadir etiquetas numéricas a cada barra
def autolabel(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate('{}'.format(altura),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Distancia vertical de la etiqueta desde la barra
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()  # Optimizar el diseño
plt.show()  # Mostrar el gráfico