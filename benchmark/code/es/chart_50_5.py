import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2023", "2024", "2025p", "2026p", "2027p", "2028p"]
# Envíos globales (en diez miles de unidades)
global_shipments = [34, 234, 585, 1070, 1730, 2600]
# Envíos a China (en diez miles de unidades)
china_shipments = [10, 36, 108, 324, 648, 972]

x = np.arange(len(years))  # Posiciones de las marcas en el eje X
width = 0.35  # Ancho de cada barra en el grupo

fig, ax = plt.subplots()

# Dibujar el gráfico de barras de envíos globales
rects1 = ax.bar(x - width/2, global_shipments, width, label='Envíos Globales (en diez miles de unidades)', color='greenyellow')
# Dibujar el gráfico de barras de envíos a China
rects2 = ax.bar(x + width/2, china_shipments, width, label='Envíos a China (en diez miles de unidades)', color='dodgerblue')

# Agregar título y etiquetas de los ejes
ax.set_title('Escala y Previsión de Envíos de Gafas de IA desde 2023 hasta 2028')
ax.set_xticks(x)
ax.set_xticklabels(years)

# Agregar etiquetas numéricas a cada barra
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Agregar leyenda
ax.legend()

plt.show()