import matplotlib.pyplot as plt
import numpy as np

# Formas de conocer sobre instituciones de exámenes físicos
canales = ["Organización de la empresa", "Introducción de familiares y amigos", "Información en el sitio web", "Publicidad fuera de línea", "Charlas de salud", "Medios propios", "Periódicos y revistas"]
# Proporción correspondiente (%)
proporciones = [37.93, 36.12, 34.85, 32.49, 31.94, 29.22, 27.22]

x = np.arange(len(canales))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas, centradas por encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(canales, rotation=15, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Formas en que los consumidores chinos de exámenes físicos se enteran de las instituciones de exámenes físicos en 2025')

plt.tight_layout()
plt.show()