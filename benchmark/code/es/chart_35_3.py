import matplotlib.pyplot as plt

# Datos
etiquetas = ['Enfermedades cardiovasculares y cerebrovasculares', 'Cáncer', 'Enfermedades respiratorias crónicas', 'Otros']
tamaños = [53, 27, 10, 10]  # La proporción de la parte de "Otros" para que el total sea 100. Los datos pueden ser aproximadamente cercanos.
colores = ['#008060', '#80e0a0', '#c0ffe0', '#d9d9d9']  # Los colores deben ser lo más cercanos posible al gráfico original.

# Dibujar un gráfico de pastel
fig, ax = plt.subplots()
ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90, colors=colores)
ax.set_title('Composición de las causas de muerte de las enfermedades crónicas')

# Ajustar la posición de la leyenda (simular el estilo de anotación del gráfico original y se puede ajustar según sea necesario)
manejadores, etiquetas_leyenda = ax.get_legend_handles_labels()
ax.legend(manejadores, etiquetas_leyenda, loc='arriba a la derecha', bbox_to_anchor=(-0.1, 1.1))

plt.show()