import matplotlib.pyplot as plt
import numpy as np

# Niveles de ciudades
ciudades = ['Ciudades de primer nivel', 'Ciudades de segundo nivel', 'Ciudades de tercer nivel', 'Ciudades de cuarto nivel']
x = np.arange(len(ciudades))

# Eje Y izquierdo: Datos del gráfico de barras (Proporción de atención)
valores_barras = [33, 17, 22, 15]  # Corresponde al eje izquierdo (0% - 40%)

# Eje Y derecho: Datos del gráfico de línea (Proporción de atención de otra dimensión)
valores_linea = [33, 17, 22, 15]  # Corresponde al eje derecho (0% - 40%)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras, eje izquierdo
barras = ax1.bar(x, valores_barras, color='#1f77ff', width=0.5)
ax1.set_ylabel('Proporción de atención', fontsize=12)
ax1.set_ylim(0, 40)
ax1.set_yticks(np.arange(0, 41, 5))
ax1.set_xticks(x)
ax1.set_xticklabels(ciudades, fontsize=12)
ax1.set_title('Proporción de atención de la industria de la leche en polvo por nivel de ciudad en febrero', fontsize=15)

# Crear el eje derecho para dibujar el gráfico de línea
ax2 = ax1.twinx()
linea, = ax2.plot(x, valores_linea, color='orange', linewidth=3, marker='o', markersize=8)
ax2.set_ylabel('Proporción de atención de otra dimensión', fontsize=12)
ax2.set_ylim(0, 40)
ax2.set_yticks(np.arange(0, 41, 5))

# Añadir etiquetas de datos al gráfico de línea
for i, (x_val, y_val) in enumerate(zip(x, valores_linea)):
    # Ajustar la posición de la etiqueta según el tamaño del valor para evitar superposiciones
    if i in [0, 2]:  # Para evitar superposiciones con el gráfico de barras, ajustar la posición de algunas etiquetas
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(10, 5),  # Desplazamiento hacia la parte superior derecha
                    textcoords="offset points",
                    ha='left', va='bottom',
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))
    else:
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, 10),  # Desplazamiento hacia arriba
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# Embelezar el borde del gráfico
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Añadir una leyenda
lineas, etiquetas = ax1.get_legend_handles_labels()
lineas2, etiquetas2 = ax2.get_legend_handles_labels()
ax2.legend(lineas + lineas2, ['Proporción de atención', 'Proporción de atención de otra dimensión'], loc='upper right')

plt.tight_layout()
plt.show()