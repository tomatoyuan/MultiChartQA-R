import numpy as np
import matplotlib.pyplot as plt

# Datos
periodos = ['MAT2206', 'MAT2306', 'MAT2406']
ventas = [100, 110, 115]
precio_promedio = [150, 145, 155]

x = np.arange(len(periodos))

fig, ax1 = plt.subplots(figsize=(8, 5))

# Gráfico de barras: Ventas
barras = ax1.bar(x, ventas, width=0.4, color='lightgray', label='Ventas')
ax1.set_ylabel('Ventas (millones de yuanes)', fontsize=11)
ax1.set_ylim(0, 160)

# Agregar etiquetas de valores en la parte superior de las barras
for i, barra in enumerate(barras):
    altura = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2, altura + 3, f'{ventas[i]}',
             ha='center', va='bottom', fontsize=9)

# Gráfico de línea: Precio promedio
ax2 = ax1.twinx()
linea, = ax2.plot(x, precio_promedio, color='blue', marker='o', linewidth=2, label='Precio promedio')
ax2.set_ylabel('Precio promedio (yuanes)', fontsize=11)
ax2.set_ylim(60, 160)

# Etiquetar los valores en la línea
for i, precio in enumerate(precio_promedio):
    ax2.text(x[i], precio + 3, f'{precio}', ha='center', va='bottom', fontsize=9, color='blue')

# Etiquetar flecha (tendencia)
ax2.annotate('', xy=(2, precio_promedio[2]), xytext=(1, precio_promedio[1]),
             arrowprops=dict(arrowstyle='->', color='green', lw=2))

# Configurar el eje X
ax1.set_xticks(x)
ax1.set_xticklabels(periodos, fontsize=11)

# Título
plt.title("General en línea | Ventas de probióticos (millones de yuanes) y precio promedio (yuanes)", fontsize=13)

# Combinar leyendas
lineas = [barras, linea]
etiquetas = [l.get_label() for l in lineas]
ax1.legend(lineas, etiquetas, loc='upper left', fontsize=10)

plt.ylim(0, 190)

plt.tight_layout()
plt.show()