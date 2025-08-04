import matplotlib.pyplot as plt
import numpy as np

# Datos (categorías y porcentajes correspondientes, aproximadamente cercanos a los datos originales)
etiquetas = ["Mayor énfasis en el rendimiento de comodidad y salud", "Mayor énfasis en el valor de marca y la calidad",
             "Mayor énfasis en el placer propio", "Mayor énfasis en la funcionalidad en escenarios específicos",
             "Mayor énfasis en las funciones compuestas de los productos"]
porcentajes = [76.0, 59.2, 52.7, 49.4, 49.1]

# Establecer la posición de cada barra (utilizar coordenadas del eje y para gráficos de barras horizontales)
posicion_y = np.arange(len(etiquetas))

# Crear una figura y un objeto de eje
fig, ax = plt.subplots(figsize=(8, 5))  # Ajustar el tamaño para que se ajuste a la escala del gráfico original

# Dibujar un gráfico de barras horizontales. Elegir un color claro similar al del gráfico original. Aquí, se usa #D3D3D3 (un color gris, que se puede ajustar según la situación real)
ax.barh(posicion_y, porcentajes, color='#D3D3D3')

# Establecer las marcas y etiquetas del eje y para mostrar las categorías a la izquierda
ax.set_yticks(posicion_y)
ax.set_yticklabels(etiquetas)

# Establecer la etiqueta del eje x (porcentaje) y ajustar la fuente y otros estilos para que se asemejen más al estilo del gráfico original
ax.set_xlabel('Porcentaje (%)', fontsize=10)

# Agregar etiquetas de datos para mostrar los valores de porcentaje a la derecha de cada barra
for i, v in enumerate(porcentajes):
    ax.text(v + 1, i, f'{v}%', va='center', fontsize=9)

# Ocultar los bordes superior y derecho para que se asemeje más al estilo simple del gráfico original
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Establecer el título (coincidente con el título del gráfico original)
ax.set_title('Las actitudes de consumo de ropa interior de los consumidores avanzan continuamente, y las demandas diversas y personalizadas aumentan', fontsize=12, pad=15)

# Ajustar el diseño para evitar que las etiquetas se amontonen
plt.tight_layout()

# Mostrar el gráfico
plt.show()