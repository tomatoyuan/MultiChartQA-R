import matplotlib.pyplot as plt
import numpy as np

# 数据
etiquetas = ['Reclamaciones de Seguro', 'Tipos de Seguro', 'Duración del Seguro', 'Monto del Seguro']
valores = [41, 25, 22, 12]
colores = ['#ff7f9f', '#ffbf7f', '#7fffaa', '#7fbfff']  # Colores correspondientes

# Ajustar la posición del eje x, aumentar el espaciado
x = np.arange(len(etiquetas)) * 1.2  # Ampliar el espaciado del eje x (espaciado original × 1.2)

# Crear el lienzo y aumentar adecuadamente el ancho
fig, ax = plt.subplots(figsize=(10, 6))  # Ampliar el lienzo para acomodar un espaciado más ancho
rectangulos = ax.bar(x, valores, color=colores, width=0.8)  # Controlar el ancho de las barras, evitar que sean demasiado anchas

# Agregar etiquetas de valores
for rectangulo in rectangulos:
    altura = rectangulo.get_height()
    ax.annotate('{}%'.format(altura),
                xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento de la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Configurar las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, fontsize=10)  # Puedes reducir adecuadamente el tamaño de la fuente
ax.set_ylabel('Ratio de Atención')
ax.set_title('¿En qué se centran las personas al comprar un seguro?')

# Ajustar el rango del eje x, evitar que las etiquetas de los extremos queden pegadas al borde
ax.set_xlim(x[0] - 0.8, x[-1] + 0.8)

plt.tight_layout()  # Ajustar automáticamente la disposición
plt.show()