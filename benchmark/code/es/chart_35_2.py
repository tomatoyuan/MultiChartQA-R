import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Muertes por enfermedades crónicas', 'Muertes por otras causas']
tamaños = [88.5, 100 - 88.5]  # Proporciones, la suma es 100
colores = ['#008040', '#D3D3D3']  # Verde y gris similares al gráfico original

# Crear una figura y ejes
fig, ax = plt.subplots()

# Dibujar un gráfico de donut, wedgeprops se utiliza para establecer el ancho del anillo
ax.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90,
       colors=colores, wedgeprops={'width': 0.3})

# Establecer el título
ax.set_title('Proporción de muertes causadas por enfermedades crónicas en el total de muertes en China en 2019', y=-0.15, fontsize=12, fontweight='bold')

# Hacer que el gráfico de pastel sea circular
ax.axis('equal')

# Mostrar el gráfico
plt.show()