import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
factores = ["Sabor", "Precio", "Empaque", "Promoción", "Otros"]
proporciones = [66.2, 63.2, 44.1, 42.1, 0.5]  # Proporción (%)

x = np.arange(len(factores))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='coral', width=0.6)
ax.set_title('Factores que influyen en la compra de bebidas sin azúcar por parte de los consumidores chinos en 2023', fontsize=14)
ax.set_ylabel('Proporción de atención (%)')
ax.set_xticks(x)
ax.set_xticklabels(factores)
ax.set_ylim(0, 75)  # Ajustar el rango del eje y para una mejor visualización de los datos

# Agregar anotaciones numéricas
for i, prop in enumerate(proporciones):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=12)

plt.tight_layout()
plt.show()