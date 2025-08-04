import matplotlib.pyplot as plt
import numpy as np

# Nombres de las ciudades
ciudades = ["Chengdu", "Wuhan", "Suzhou", "Nanjing", "Tianjin", "Guangzhou", "Hangzhou", "Shanghai", "Beijing", "Shenzhen"]
# Costo del matrimonio (unidad: diez mil yuanes)
costos = [55, 65, 94, 102, 108, 128, 178, 200, 202, 208]

x = np.arange(len(ciudades))  # Se utiliza para establecer la posición del gráfico de barras en el eje x

# Crear un lienzo y un objeto de eje
fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras, establecer el color en blanco y el borde en rosa
barras = ax.bar(x, costos, color='white', edgecolor='pink')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(ciudades)
# Establecer la etiqueta del eje y
ax.set_ylabel("Costo del Matrimonio (Diez Mil Yuanes)")
# Establecer el título
ax.set_title("Las 10 Ciudades con Mayor Costo de Matrimonio en China")
# Establecer la unidad que se mostrará junto al título
ax.text(0.95, 1.05, "Unidad: Diez Mil Yuanes", transform=ax.transAxes, ha='right', va='bottom')

# Etiquetar los valores en cada barra
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, f'{altura}',
            ha='center', va='bottom')

# Establecer el color de fondo en rosa
ax.set_facecolor('pink')
# Eliminar los bordes superior y derecho
for espina in ['top', 'right']:
    ax.spines[espina].set_visible(False)

plt.show()