import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
direcciones_mejora = ["Sabor", "Ingredientes", "Precio", "Fecha", "Especificación", "Empaque"]
proporciones = [71.5, 56.2, 56.0, 46.5, 40.8, 39.3]  # Proporción (%)

x = np.arange(len(direcciones_mejora))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='coral')
ax.set_title('Direcciones de mejora de las bebidas sin azúcar en el mercado según los consumidores chinos en 2023', fontsize=14)
ax.set_ylabel('Proporción (%)')
ax.set_xlabel('Direcciones de mejora')
ax.set_xticks(x)
ax.set_xticklabels(direcciones_mejora)
ax.set_ylim(0, 80)  # Ajustar el rango del eje y para ajustarse a la proporción máxima (71.5%)

# Agregar anotaciones numéricas
for i, prop in enumerate(proporciones):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

plt.tight_layout()
plt.show()