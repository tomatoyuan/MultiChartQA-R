import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2019, 2024)
# Población miope en China (en cientos de millones)
myopia_pop = [6.0, 6.5, 6.9, 6.9, 7.0]
# Población total en China (en cientos de millones)
total_pop = [14.1, 14.2, 14.6, 14.6, 14.6]
# Proporción de la población miope (%)
myopia_ratio = [42.6, 45.8, 47.3, 47.3, 47.9]

x = np.arange(len(years))  # Posiciones de las marcas en el eje x

fig, ax1 = plt.subplots(figsize=(12, 6))  # Ajustar el tamaño del gráfico

# Ajustar el ancho y la posición del gráfico de barras para evitar superposiciones
width = 0.35
rects1 = ax1.bar(x - width/2, myopia_pop, width, label='Población miope en China (en cientos de millones)', color='greenyellow', alpha=0.8)
rects2 = ax1.bar(x + width/2, total_pop, width, label='Población total en China (en cientos de millones)', color='dodgerblue', alpha=0.8)

ax1.set_ylabel('Población (en cientos de millones)', fontsize=12)
ax1.set_xlabel('Año', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years, fontsize=11)
ax1.legend(loc='lower center')
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # Agregar líneas de cuadrícula

# Crear un segundo eje y para dibujar un gráfico de línea
ax2 = ax1.twinx()
ax2.plot(x, myopia_ratio, marker='o', markersize=8, label='Proporción de la población miope (%)', color='blue', linewidth=2.5)
ax2.set_ylabel('Proporción (%)', fontsize=12)
ax2.set_ylim(40, 50)  # Ajustar el rango del eje y
ax2.legend(loc='upper left')

# Agregar etiquetas numéricas al gráfico de barras
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax1.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 5),  # Desplazamiento vertical
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10)

autolabel(rects1)
autolabel(rects2)

# Agregar etiquetas numéricas al gráfico de línea
for i, ratio in enumerate(myopia_ratio):
    ax2.annotate(f'{ratio}%',
                 xy=(x[i], ratio),
                 xytext=(0, 8),  # Desplazamiento vertical
                 textcoords="offset points",
                 ha='center', va='bottom',
                 fontsize=10,
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7))

plt.title('Población miope y su proporción en China desde 2019 hasta 2023', fontsize=15, pad=15)
plt.tight_layout()  # Optimizar el diseño
plt.show()