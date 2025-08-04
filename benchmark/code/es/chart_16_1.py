import matplotlib.pyplot as plt
import numpy as np

# Años
años = [2011, 2012, 2013, 2014, 2015]
# Número de mejores estudiantes provinciales admitidos por la Universidad de Tsinghua
qinghua = [35, 43, 50, 42, 43]
# Número de mejores estudiantes provinciales admitidos por la Universidad de Pekín
beida = [23, 27, 24, 48, 38]

# Establecer el ancho de las barras
ancho_barra = 0.35
# Generar posiciones en el eje x para los dos grupos de barras
x = np.arange(len(años))

# Crear una figura y ejes
fig, ax = plt.subplots()

# Dibujar las barras para la Universidad de Tsinghua
rects1 = ax.bar(x - ancho_barra/2, qinghua, ancho_barra, label='Tsinghua', color='#6699CC')
# Dibujar las barras para la Universidad de Pekín
rects2 = ax.bar(x + ancho_barra/2, beida, ancho_barra, label='Pekín', color='#CC6666')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(años)
# Establecer la etiqueta del eje y
ax.set_ylabel('Número de mejores estudiantes provinciales admitidos')
# Establecer el título
ax.set_title('Comparación del número de mejores estudiantes provinciales admitidos por las Universidades de Tsinghua y Pekín desde 2011 a 2015')
# Agregar una leyenda
ax.legend()

# Etiquetar los valores en las barras
def autolabel(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate('{}'.format(altura),
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Ajustar el diseño para evitar la superposición de etiquetas
fig.tight_layout()
# Mostrar el gráfico
plt.show()