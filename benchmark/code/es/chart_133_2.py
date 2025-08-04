import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Leche materna artificial", "Leche en polvo a granel", "Crema ligera", "Queso", "Productos de suero", "Productos de crema", "Productos proteicos", "Leche envasada", "Yogur", "Leche condensada"]
valor_importacion = [42.1, 29.2, 10.3, 9.7, 8.6, 8.3, 6.1, 5.6, 0.5, 0.4]
tasa_crecimiento = [-5.0, -34.0, 7.4, 25.9, -10.6, -11.3, -10.5, -16.2, -0.7, -18.7]

x = np.arange(len(categorias))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Dibujar el gráfico de barras para el valor de importación
ax1.bar(x, valor_importacion, color='orange', label='Valor de importación (miles de millones de dólares estadounidenses)')
ax1.set_ylabel('Valor de importación (miles de millones de dólares estadounidenses)')
ax1.set_xlabel('Tipos de productos lácteos')
ax1.set_xticks(x)
ax1.set_xticklabels(categorias, rotation=45, ha='right')
ax1.legend(loc='center left')

# Crear un eje y secundario y dibujar el gráfico de línea para el crecimiento año tras año
ax2 = ax1.twinx()
ax2.plot(x, tasa_crecimiento, marker='o', color='gold', label='Crecimiento año tras año (%)', linewidth=2)
ax2.set_ylabel('Crecimiento año tras año (%)')
ax2.legend(loc='upper right')

# Añadir etiquetas para el valor de importación
for i, val in enumerate(valor_importacion):
    ax1.text(i, val + 1, f'{val}', ha='center', va='bottom')

# Añadir etiquetas para el crecimiento año tras año
for i, tasa in enumerate(tasa_crecimiento):
    ax2.text(i, tasa + 1, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Valor de importación y crecimiento año tras año de los principales productos lácteos en China en 2023')

plt.tight_layout()
plt.show()