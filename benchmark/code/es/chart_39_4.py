import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Cafetería en Librería', 'Cafetería en Jardín', 'Cafetería en Camping', 'Cafetería en Museo', 'Cafetería en Teatro', 'Cafetería en Gimnasio', 'Cafetería en Mercado', 'Cafetería en Templo']
valores = [62, 58, 50, 47, 43, 37, 18, 17]

# Crear un objeto de trazado
fig, ax = plt.subplots()

# Dibujar un gráfico de barras horizontales
barras = ax.barh(etiquetas, valores, color='#8FBC8F')  # El color se puede ajustar según las necesidades reales

# Etiquetar el valor en cada barra
for barra, valor in zip(barras, valores):
    ax.text(barra.get_width() + 1, barra.get_y() + barra.get_height()/2,
            f'{valor}', ha='left', va='center', fontsize=10)

# Establecer el título y el estilo
ax.set_title('Preferencias de los consumidores por la integración de cafeterías con diferentes formas de negocio')
ax.spines['right'].set_visible(False)  # Ocultar el borde derecho
ax.spines['top'].set_visible(False)    # Ocultar el borde superior

# Ajustar el diseño para que las etiquetas se vean mejor
plt.tight_layout()

# Mostrar el gráfico
plt.show()