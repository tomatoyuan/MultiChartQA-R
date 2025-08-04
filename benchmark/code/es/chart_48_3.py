import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ['Muy acomodado', 'Relativamente acomodado', 'Apenas suficiente', 'Relativamente difícil', 'Muy difícil']
# Datos rurales
rural = [2.3, 14.9, 61.3, 17.9, 3.6]
# Datos urbanos
urbano = [4.5, 22.0, 61.2, 10.5, 1.8]
# Datos totales
total = [3.5, 18.7, 61.2, 13.9, 2.7]

x = np.arange(len(categorias))  # Posición en el eje x
ancho = 0.25  # Ancho de cada barra

fig, ax = plt.subplots()
# Dibujar barras para rural, urbano y total
rects1 = ax.barh(x - ancho, rural, ancho, label='Rural', color='green')
rects2 = ax.barh(x, urbano, ancho, label='Urbano', color='darkgreen')
rects3 = ax.barh(x + ancho, total, ancho, label='Total', color='gray')

# Agregar etiquetas, título, etc.
ax.set_yticks(x)
ax.set_yticklabels(categorias)
ax.set_xlabel('Porcentaje%')
ax.set_title('Estado económico auto - evaluado de las personas mayores en áreas urbanas y rurales de China en 2021')
ax.legend()

# Mostrar valores en las barras
def label_bars(rects):
    for rect in rects:
        longitud = rect.get_width()
        ax.text(longitud + 0.5, rect.get_y() + rect.get_height() / 2, f'{longitud}%', va='center')

label_bars(rects1)
label_bars(rects2)
label_bars(rects3)

plt.show()