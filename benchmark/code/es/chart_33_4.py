import matplotlib.pyplot as plt
import numpy as np

# Nombres de las plataformas de comercio electrónico
plataformas = ['Tmall', 'Douyin', 'JD.com']
# Datos de participación en el mercado (valores aproximados están bien)
participacion_mercado = [30, 25, 15]

x = np.arange(len(plataformas))  # Coordenadas del eje x
ancho = 0.5  # Ancho de las barras

fig, ax = plt.subplots()
# Dibujar un gráfico de barras con un color azul similar y bordes negros
rectangulos = ax.bar(x, participacion_mercado, ancho, color='#4CAF50', edgecolor='black')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(plataformas)
# Establecer la etiqueta del eje y
ax.set_ylabel('Participación en el Mercado')
# Establecer el título del gráfico
ax.set_title('Participación en el Mercado de las Plataformas de Comercio Electrónico en MAT25')

# Agregar etiquetas de datos
def agregar_etiquetas(rectangulos):
    for rectangulo in rectangulos:
        altura = rectangulo.get_height()
        ax.annotate(f'{altura}',
                    xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom')

agregar_etiquetas(rectangulos)

plt.show()