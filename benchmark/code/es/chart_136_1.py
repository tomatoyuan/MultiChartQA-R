import matplotlib.pyplot as plt
import numpy as np

# Datos de ventas del lado izquierdo
años_ventas = ["2019", "2020", "2021", "2022", "2023"]
ventas = [96.0, 85.0, 102.0, 103.0, 107.0]

# Datos de flujo de clientes del lado derecho
años_flujo = ["2020", "2021", "2022", "2023"]
flujo = [650.0, 670.0, 600.0, 750.0]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Dibujar el gráfico de barras de ventas del lado izquierdo
x_ventas = np.arange(len(años_ventas))
barras = ax1.bar(x_ventas, ventas, color='orange', label='Ventas (Millones de piezas)')
ax1.set_ylabel('Ventas (Millones de piezas)')
ax1.set_xlabel('Año')
ax1.set_xticks(x_ventas)
ax1.set_xticklabels(años_ventas)
ax1.legend(loc='upper left')
# Agregar etiquetas de valores de ventas
for i, venta in enumerate(ventas):
    ax1.text(i, venta + 1, f'{venta}', ha='center', va='bottom')

# Dibujar el gráfico de área de flujo de clientes del lado derecho
x_flujo = np.arange(len(años_flujo))
ax2.fill_between(x_flujo, flujo, color='gold', label='Flujo de Clientes (Millones de personas)')
ax2.set_ylabel('Flujo de Clientes (Millones de personas)')
ax2.set_xlabel('Año')
ax2.set_xticks(x_flujo)
ax2.set_xticklabels(años_flujo)
ax2.legend(loc='upper left')
# Agregar etiquetas de valores de flujo de clientes
for i, f in enumerate(flujo):
    ax2.text(i, f + 10, f'{f}', ha='center', va='bottom')

ax1.set_title('Ventas de Pandora desde 2019 - 2023')
ax2.set_title('Flujo de Clientes de Pandora desde 2020 - 2023')

plt.tight_layout()
plt.show()