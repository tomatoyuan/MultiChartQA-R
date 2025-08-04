import matplotlib.pyplot as plt
import numpy as np

# Categorías de snacks
categorias = ['Bebidas dulces', 'Snacks masticables', 'Comidas fritas infladas', 'Yogur', 'Productos de panadería', 'Frutos secos', 'Snacks picantes', 'Alimentos con alto contenido de azúcar', 'Frutas secas y frutas confitadas']
# Porcentajes de selección correspondientes
porcentajes = [55, 43, 43, 42, 42, 39, 38, 36, 33]

x = np.arange(len(categorias))  # Coordenadas del eje x

fig, ax = plt.subplots()
# Dibujar un gráfico de barras
rects = ax.bar(x, porcentajes, color='green')

# Agregar título y etiquetas de los ejes
ax.set_title('Distribución de la selección de snacks de los "trabajadores punks con horas extras" cuando tienen antojo en el trabajo')
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=25, ha='right')
ax.set_ylabel('Porcentaje de selección (%)')

# Etiquetar los valores en las barras
for rect in rects:
    altura = rect.get_height()
    ax.annotate(f'{altura}%',
                xy=(rect.get_x() + rect.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()