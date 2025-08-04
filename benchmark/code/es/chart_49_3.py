import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ['Productos de té']
mat2023 = [100]  # Datos hipotéticos de MAT2023, se pueden reemplazar con valores reales
mat2024 = [118]  # Datos hipotéticos de MAT2024 basados en +18%, se pueden reemplazar con valores reales
tasa_de_crecimiento = 18  # Tasa de crecimiento

x = np.arange(len(categorias))  # Posiciones del eje x del gráfico de barras
ancho = 0.35  # Ancho del gráfico de barras

fig, ax = plt.subplots()
rects1 = ax.bar(x - ancho/2, mat2023, ancho, label='MAT2023', color='lightgreen')
rects2 = ax.bar(x + ancho/2, mat2024, ancho, label='MAT2024', color='green')

# Agregar flecha y texto de la tasa de crecimiento
flecha_x = x[0]
flecha_y = max(mat2023 + mat2024) * 0.6  # Posición de la flecha, se puede ajustar
ax.annotate(f'+{tasa_de_crecimiento}%', xy=(flecha_x, mat2023[0]), xytext=(flecha_x, flecha_y),
            arrowprops=dict(facecolor='orange', shrink=0.05),
            ha='center', va='bottom', fontsize=14, color='orange')

# Función para agregar etiquetas de valor
def agregar_etiquetas(rects):
    for rect in rects:
        altura = rect.get_height()
        ax.annotate(f'{altura}',
                    xy=(rect.get_x() + rect.get_width() / 2, altura),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom')

# Agregar etiquetas de valor a ambas barras
agregar_etiquetas(rects1)
agregar_etiquetas(rects2)

# Establecer etiquetas del eje, etc.
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()

plt.title('Tamaño del mercado de consumo de productos de té en línea en Taobao y Tmall de MAT2023 a MAT2024')
plt.show()