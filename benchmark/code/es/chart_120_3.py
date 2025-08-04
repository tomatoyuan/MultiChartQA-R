import matplotlib.pyplot as plt
import numpy as np

# Sugerencias para la mejora y datos de proporción correspondientes
sugerencias = [
    "Falta de enseñanza y otros conocimientos introductorios", "La información relevante no se actualiza a tiempo",
    "El contenido está desordenado y no está lo suficientemente refinado", "Falta de funciones de entretenimiento",
    "La aplicación no se ejecuta lo suficientemente suavemente", "Operación inconveniente"
]
proporciones = [47.59, 44.92, 42.25, 37.97, 36.90, 28.34]

y = np.arange(len(sugerencias))

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas a la derecha de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion + 1, i, f'{proporcion}%', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(sugerencias)
ax.set_xlabel('Proporción (%)')
ax.set_title('Encuesta sobre sugerencias de mejora de los usuarios de las aplicaciones autónomas de empresas de valores chinas')

plt.tight_layout()
plt.show()