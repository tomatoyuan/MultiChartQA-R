import matplotlib.pyplot as plt
import numpy as np

# Elementos de mejora funcional
caracteristicas = ["Mejorar la comodidad", "Mejorar la salud", "Funcionalidad para deportistas profesionales"]
# Datos de porcentaje correspondientes
porcentajes = [71, 57, 55]
# Se utiliza para mostrar información TOP en el gráfico, se configura según el índice aquí
tops = ["TOP1", "TOP2", "TOP3"]

# Establece la fuente para garantizar la visualización normal del español
plt.rcParams['axes.unicode_minus'] = False  # Resuelve el problema de que el signo menos se muestre como un cuadrado

y_pos = np.arange(len(caracteristicas))  # Posición en el eje y

# Crea un gráfico de barras horizontales
fig, ax = plt.subplots()
barras = ax.barh(y_pos, porcentajes, align='center', color=['#1f77b4', '#ff7f0e', '#2ca02c'])  # Establece colores, tratar de ser similar al estilo del ejemplo

# Agrega los valores de porcentaje al final de cada barra
for barra, porcentaje in zip(barras, porcentajes):
    longitud = barra.get_width()
    ax.text(longitud + 1,  # Coordenada x de la posición de visualización del número, se puede ajustar
            barra.get_y() + barra.get_height() / 2,  # Coordenada y de la posición de visualización del número, centrada
            f'{porcentaje}%',
            va='center')

# Agrega información TOP a la derecha de cada barra
for i, (barra, top) in enumerate(zip(barras, tops)):
    longitud = barra.get_width()
    ax.text(longitud + 6,  # Se puede ajustar según la situación real
            barra.get_y() + barra.get_height() / 2,
            top,
            va='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(caracteristicas)
ax.invert_yaxis()  # Muestra el primer elemento funcional en la parte superior
ax.set_xlabel('Porcentaje (%)')
ax.set_title('Mejoras funcionales que los consumidores esperan que tenga la ropa interior')

plt.show()