import matplotlib.pyplot as plt
import numpy as np

# Gráfico 3: Tasa de crecimiento de pedidos de delivery y cantidad de productos
etiquetas = ['2022.7-2023.6', '2023.7-2024.6']
tasa_crecimiento_pedidos = [13.21, 20.16]     # Tasa de crecimiento de pedidos de delivery
tasa_crecimiento_productos = [15.16, 18.28]  # Tasa de crecimiento de productos gastronómicos

x = np.arange(len(etiquetas))
ancho = 0.35

fig, ax = plt.subplots(figsize=(7, 4.5))

# Gráfico de barras
barra1 = ax.bar(x - ancho/2, tasa_crecimiento_pedidos, ancho, label='Tasa de crecimiento de \npedidos de delivery', color='#8BC34A')
barra2 = ax.bar(x + ancho/2, tasa_crecimiento_productos, ancho, label='Tasa de crecimiento de \nproductos gastronómicos', color='#388E3C')

# Anotación de valores
for barra in barra1:
    altura = barra.get_height()
    ax.annotate(f'{altura:.2f}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

for barra in barra2:
    altura = barra.get_height()
    ax.annotate(f'{altura:.2f}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom', fontsize=10)

# Configuración del gráfico
ax.set_ylabel('Tasa de crecimiento (%)', fontsize=12)
ax.set_title('Tasa de crecimiento de la cantidad de pedidos \nde delivery (Meituan) y de productos gastronómicos', fontsize=13, weight='bold')
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, fontsize=11)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=10, frameon=False)
# Anotación de la fuente de datos

plt.tight_layout()
plt.show()