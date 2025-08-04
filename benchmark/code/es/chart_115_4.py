import matplotlib.pyplot as plt
import numpy as np

# Principales formas de transformación digital
metodos = [
    "Utilizar inteligencia artificial y aprendizaje automático", "Adoptar servicios de computación en la nube y SaaS",
    "Desarrollar e implementar plataformas o sistemas digitales de forma independiente",
    "Realizar la transformación basándose en las empresas de la cadena de suministro (arriba y abajo)",
    "Realizar la transformación utilizando plataformas de comercio electrónico de terceros",
    "Comprar software o soluciones digitales generales",
    "Utilizar plataformas de Internet industrial construidas por empresas líderes de la cadena industrial",
    "Comprar software o soluciones digitales para industrias específicas"
]
# Proporciones correspondientes (%)
proporciones = [7.69, 15.60, 16.67, 17.52, 28.63, 42.95, 47.01, 53.85]

y = np.arange(len(metodos))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas a la derecha de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(metodos)
ax.set_xlabel('Proporción (%)')
ax.set_title('Principales formas de transformación digital de las empresas chinas en 2025')

plt.tight_layout()
plt.show()