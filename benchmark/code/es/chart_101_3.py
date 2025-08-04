import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
tipos_de_contenido = ["Vídeos cortos", "Transmisiones en vivo", "Gráficos y textos", "Audio", "Otros"]
proporciones = [75.7, 25.6, 22.0, 13.2, 7.6]  # Proporción (%)
colores = ["#ff7f27"]  # Naranja, similar al esquema de colores de la imagen original

x = np.arange(len(tipos_de_contenido))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(x, proporciones, color=colores * len(tipos_de_contenido))
ax.set_title('Distribución de tipos de contenido consumidos por usuarios que pagan por conocimiento en 2022', fontsize=14)
ax.set_xlabel('Proporción (%)')
ax.set_ylabel('Tipos de contenido')
ax.set_yticks(x)
ax.set_yticklabels(tipos_de_contenido)
ax.set_xlim(0, 80)  # Ajustar el rango del eje x para ajustarse a la proporción máxima (75.7%)

# Agregar anotaciones numéricas
for i, prop in enumerate(proporciones):
    ax.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

plt.tight_layout()
plt.show()