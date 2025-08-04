import matplotlib.pyplot as plt
import numpy as np

# Datos del primer gráfico circular
etiquetas_1 = ['Concretó un trato entre abril y mayo', 'Otros']
tamaños_1 = [86, 14]  # Los datos son aproximadamente consistentes y la suma es 100
colores_1 = ['#4fa3e1', '#c7b8e0']  # Los colores son similares a la imagen original

# Datos del segundo gráfico circular
etiquetas_2 = ['Visitó entre abril y mayo', 'Otros']
tamaños_2 = [94, 6]  # Los datos son aproximadamente consistentes y la suma es 100
colores_2 = ['#4fa3e1', '#f1c4e0']  # Los colores son similares a la imagen original

# Crear un lienzo
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Establecer el título general
fig.suptitle('Análisis del comportamiento de los usuarios que concretaron un trato durante la promoción 618 entre abril y mayo', fontsize=16, fontweight='bold')

# Dibujar el primer gráfico circular
ax1.pie(tamaños_1, labels=etiquetas_1, autopct='%1.0f%%', startangle=90, colors=colores_1)

# Dibujar el segundo gráfico circular
ax2.pie(tamaños_2, labels=etiquetas_2, autopct='%1.0f%%', startangle=90, colors=colores_2)

# Hacer que los gráficos circulares se vean como círculos perfectos
for ax in [ax1, ax2]:
    ax.axis('equal')

plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Ajustar la distancia entre los subgráficos y la parte superior
plt.show()