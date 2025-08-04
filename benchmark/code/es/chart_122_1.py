import matplotlib.pyplot as plt
import numpy as np

# Datos
fuentes = [
    "Presentado por familiares y amigos", "Plataformas de vídeos cortos", "Plataformas de compartición de contenido", 
    "Conocido en bodas de otros", "Sitios web / APPs relacionados con bodas", "Búsqueda en Internet", "Publicidad"
]
proporciones = [43.8, 43.5, 38.8, 37.9, 36.5, 27.1, 25.9]

y = np.arange(len(fuentes))

fig, ax = plt.subplots(figsize=(8, 5))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion + 1, i, f'{proporcion}%', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(fuentes)
ax.set_xlabel('Proporción (%)')
ax.set_title('Encuesta sobre las fuentes de información de empresas de bodas en China')

plt.tight_layout()
plt.show()