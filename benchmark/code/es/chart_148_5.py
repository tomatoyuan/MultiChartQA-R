import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
escenarios = ["Reunión de ocio", "Trabajo/Estudio", "Cena", "Ejercicio", "Partidos de e - deportes", "Cuando se lanzan nuevos productos", "Conducción"]
proporciones = [62.8, 53.1, 42.4, 42.0, 28.6, 28.1, 25.6]  # Proporción (%)

x = np.arange(len(escenarios))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='coral')
ax.set_title('Escenarios de consumo de bebidas sin azúcar por los consumidores chinos en 2023', fontsize=14)
ax.set_ylabel('Proporción (%)')
ax.set_xlabel('Escenarios de consumo')
ax.set_xticks(x)
ax.set_xticklabels(escenarios, rotation=45, ha='right')  # Rotar las etiquetas del eje x para evitar solapamiento
ax.set_ylim(0, 70)  # Ajustar el rango del eje y para ajustarse a la proporción máxima (62.8%)

# Agregar anotaciones numéricas
for i, prop in enumerate(proporciones):
    ax.text(x[i], prop + 1, f'{prop}%', ha='center', va='bottom', color='black', fontsize=11)

# Agregar una leyenda
ax.legend(barras, ['Proporción'], loc='upper right')

plt.tight_layout()
plt.show()