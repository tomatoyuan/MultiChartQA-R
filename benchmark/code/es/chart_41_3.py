import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ['Estantes', 'Contenidos']
# Datos de marcas nacionales
datos_nacionales = [22, 27]
# Datos de marcas internacionales
datos_internacionales = [8, 3]

x = np.arange(len(categorias))  # Posiciones en el eje x
ancho = 0.35  # Ancho de las barras

fig, ax = plt.subplots()
# Dibujar las barras de las marcas nacionales
rects1 = ax.bar(x - ancho/2, datos_nacionales, ancho, label='Marcas Nacionales', color='#4B72C2')
# Dibujar las barras de las marcas internacionales
rects2 = ax.bar(x + ancho/2, datos_internacionales, ancho, label='Marcas Internacionales', color='#F08C2E')

# Añadir etiquetas de datos a las barras
def agregar_etiquetas(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate(f'{altura}',
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom')

agregar_etiquetas(rects1)
agregar_etiquetas(rects2)

# Establecer las etiquetas de las marcas de graduación en el eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Establecer la etiqueta del eje y (no se muestra claramente en el gráfico original, se puede agregar según sea necesario)
# ax.set_ylabel('Cantidad')
# Establecer el título del gráfico
ax.set_title('Proporción de Marcas Nacionales e Internacionales entre las 30 Mejores Marcas de MAT2024')
# Añadir una leyenda
ax.legend()

plt.tight_layout()  # Ajustar el diseño para asegurar que las etiquetas se muestren completamente
plt.show()