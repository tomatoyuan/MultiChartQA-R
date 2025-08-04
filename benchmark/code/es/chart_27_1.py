import matplotlib.pyplot as plt
import numpy as np

# Nombres de las telenovelas
etiquetas = ["Cruzar océanos para verte", "Borde de la navaja", "En nombre del pueblo", "En la cima de las nubes"]
# Datos de índice de búsqueda correspondientes
valores = [16693, 75744, 243831, 60535]
# Establecer colores para cada grupo de datos (se pueden ajustar según sea necesario)
colores = ['c', 'orange', 'r', 'm']

x = np.arange(len(etiquetas))  # Coordenadas del eje x

fig, ax = plt.subplots()
# Dibujar un gráfico de barras
barras = ax.bar(x, valores, color=colores)

# Agregar etiquetas numéricas sobre las barras
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, altura, str(altura),
            ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=45, ha='right', fontsize=11)
# Establecer el título del gráfico
ax.set_title('Índice de búsqueda de telenovelas de primavera', fontsize=14, fontweight='bold')
# Establecer la etiqueta del eje y (no se establece aquí ya que el gráfico original no está claro, se puede completar según sea necesario)
# ax.set_ylabel('Índice de búsqueda')

plt.show()