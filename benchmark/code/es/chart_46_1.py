import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ["Sillas ergonómicas", "Escritorios eléctricos para trabajar de pie", "Lámparas de cuidado ocular"]
# Datos en 2023 (miles de millones de yuanes)
valores_2023 = [3, 2, 9]
# Datos en 2024 (miles de millones de yuanes)
valores_2024 = [4.5, 3.5, 12]
# Tasas de crecimiento año tras año
tasas_crecimiento = ["+43%", "+33%", "+26%"]

x = np.arange(len(categorias))  # Posiciones del eje x
ancho = 0.35  # Ancho de las barras

fig, ax = plt.subplots()
# Dibujar el gráfico de barras para 2023
rects2023 = ax.bar(x - ancho/2, valores_2023, ancho, label='2023', color='lightblue')
# Dibujar el gráfico de barras para 2024
rects2024 = ax.bar(x + ancho/2, valores_2024, ancho, label='2024', color='steelblue')

# Función para agregar etiquetas de valores
def agregar_etiquetas(rects, valores):
    for rect, valor in zip(rects, valores):
        altura = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., altura + 0.2,
                f'{valor}', ha='center', va='bottom')

# Agregar etiquetas de valores a los gráficos de barras de ambos años
agregar_etiquetas(rects2023, valores_2023)
agregar_etiquetas(rects2024, valores_2024)

# Agregar texto de la tasa de crecimiento año tras año
for i in range(len(categorias)):
    if tasas_crecimiento[i].startswith('+'):
        color_flecha = 'red' if tasas_crecimiento[i] == '+43%' else 'black'
        ax.text(x[i] + ancho/2 + 0.1, valores_2024[i] - 1, tasas_crecimiento[i], 
                color=color_flecha, fontweight='bold')
    else:
        ax.text(x[i] + ancho/2, valores_2024[i] + 0.2, tasas_crecimiento[i], ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=10, ha='right')
# Establecer el rango del eje y
ax.set_ylim([0, 15])
# Agregar marcas en el eje y
ax.set_yticks(np.arange(0, 16, 5))
# Agregar leyenda
ax.legend()

# Establecer el título del gráfico
ax.set_title('Tamaño del mercado online (miles de millones de yuanes) y \ntasa de crecimiento año tras año de los "Tres Grandes" en el estudio de 2023 a 2024')
plt.tight_layout()  # Asegurar una disposición adecuada
plt.show()