import matplotlib.pyplot as plt
import numpy as np

# Factores de consideración
factores = ["Contenido del audiolibro", "Voz y habilidad del narrador", "Duración del audiolibro", "Si el audiolibro está adaptado de un IP", "Precio del audiolibro", "Frecuencia de actualización del audiolibro"]
# Proporciones correspondientes (%)
proporciones = [40.82, 38.70, 34.71, 34.57, 34.04, 33.38]

x = np.arange(len(factores))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(8, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(factores, rotation=30, ha='right', fontsize=11)
ax.set_ylabel('Proporción (%)')
ax.set_title('Principales consideraciones de los usuarios chinos de audiolibros al elegir audiolibros en 2025')

plt.tight_layout()
plt.show()