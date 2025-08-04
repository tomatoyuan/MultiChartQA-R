import matplotlib.pyplot as plt
import numpy as np

# Factores de decisión
etiquetas = ['Parámetros relacionados con la función', 'Diseño de apariencia/Grado de moda', 'Reseñas de usuarios/Boca a boca', 'Precio/Actividades de promoción', 
             'Conocimiento de la marca', 'Servicio post - venta', 'Endoso de celebridades/KOL', 'Ediciones limitadas/Co - diseñadas']
# Datos de proporción correspondientes a cada factor
valores = [89, 61, 45, 35, 27, 19, 5, 3]

# Establece las posiciones de las coordenadas x para el gráfico de barras
x = np.arange(len(etiquetas))  
# Dibuja el gráfico de barras y establece el ancho de las barras, etc.
fig, ax = plt.subplots()
rectangulos = ax.bar(x, valores, width=0.5, color=['pink', 'pink', 'gray', 'gray', 'gray', 'gray', 'gray', 'gray'])

# Establece las marcas y etiquetas del eje
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=45, ha='right')  # Gira las etiquetas para evitar solapamientos
ax.set_ylabel('Proporción (%)')
ax.set_title('Factores de decisión cuando los consumidores compran ropa funcional')

# Anota los valores en las barras
for rectangulo in rectangulos:
    altura = rectangulo.get_height()
    ax.annotate('{}%'.format(altura),
                xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
                xytext=(0, 3),  # Distancia vertical del valor desde la parte superior de la barra
                textcoords="offset points",
                ha='center', va='bottom')

plt.tight_layout()  # Ajusta automáticamente el diseño para evitar que las etiquetas se muestren incompletas, etc.
plt.show()