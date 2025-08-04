import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Datos de años
years = np.arange(2002, 2018)
# Datos de volumen de pasajeros correspondientes a cada año (aproximadamente cercanos a los datos originales)
passenger_volumes = [1.28, 1.35, 1.37, 1.37, 1.44, 1.56, 
                     1.96, 1.92, 2.1, 2.2, 2.2, 2.4, 
                     2.66, 2.95, 3.25, 3.56]

# Crear una figura
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras, establecer el color para que sea cercano al esquema de color verde claro del gráfico original
bar_rects = ax.bar(years, passenger_volumes, color='#87E8DE')

# Establecer las marcas del eje x
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=10)

# Establecer la etiqueta del eje y
ax.set_ylabel('Número de Pasajeros Transportados (en cientos de millones)', fontsize=12)
# Establecer el título
ax.set_title('Volumen Anual de Pasajeros del Festival de la Primavera del Ferrocarril Nacional (Unidad: cientos de millones de pasajeros)', fontsize=14, pad=20)

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Etiquetar los valores en las barras
for rect in bar_rects:
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width() / 2, height, f'{height}',
            ha='center', va='bottom', fontsize=9)

# Agregar algunos elementos decorativos, usar gráficos puros en lugar de imágenes
hot_air_balloon = patches.Circle((2003.5, 3.3), 0.15, color='#FF7E79')
ax.add_patch(hot_air_balloon)

# Dibujar la cesta y las cuerdas del globo aerostático
basket = patches.Rectangle((2003.35, 3.15), 0.3, 0.1, color='#A0522D')
ax.add_patch(basket)

# Dibujar las cuerdas
ax.plot([2003.35, 2003.425], [3.3, 3.15], color='#8B4513', linewidth=1)
ax.plot([2003.65, 2003.575], [3.3, 3.15], color='#8B4513', linewidth=1)

plt.tight_layout()
plt.show()