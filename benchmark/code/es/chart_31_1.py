import matplotlib.pyplot as plt
import numpy as np

# 1. Preparar los datos
# Nombres de las ciudades
ciudades = ["Beijing", "Xiamen", "Hangzhou", "Harbin"]
# Simular los valores de popularidad de búsqueda aquí (unidad: 10,000 veces)
popularidad_busqueda = [8, 6, 4, 2]

x = np.arange(len(ciudades))  # Se utiliza para ubicar las barras de cada ciudad en el eje X

# 2. Crear un gráfico
fig, ax = plt.subplots()
# Dibujar un gráfico de barras y establecer el color, el ancho y otros estilos de las barras
rects = ax.bar(x, popularidad_busqueda, color=['#FF6347', '#FFA07A', '#FFD700', '#FFFF00'])

# 3. Personalizar el contenido del gráfico
ax.set_xticks(x)  # Establecer las posiciones de las marcas en el eje X
ax.set_xticklabels(ciudades)  # Usar los nombres de las ciudades como etiquetas de las marcas en el eje X
ax.set_ylabel("Popularidad de Búsqueda (10,000 veces)")  # Establecer el título del eje Y y agregar la unidad
ax.set_title("Distribución Regional de la Búsqueda de Seguridad Turística durante Fines de Semana Cortos", fontsize=14, fontweight='bold')  # Establecer el título del gráfico

# Etiquetar los valores en las barras y agregar la unidad
for rect in rects:
    altura = rect.get_height()
    ax.annotate(f'{altura}K',  # Agregar "K" para representar 10,000
                xy=(rect.get_x() + rect.get_width() / 2, altura),
                xytext=(0, 3),  # La distancia vertical de la etiqueta del valor desde la parte superior de la barra
                textcoords="offset points",
                ha='center', va='bottom')

# 4. Mostrar el gráfico
plt.show()