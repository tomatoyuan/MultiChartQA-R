import matplotlib.pyplot as plt
import numpy as np

# Descripciones de opiniones sobre el desarrollo de la industria de las cajas sorpresa
opiniones = ["Los consumidores son propensos a la adicción y gastan mucho dinero", 
             "Los precios son irrazonables y algunos productos tienen una importante prima", 
             "El mercado de la cadena de valor inferior está muy especulativo y sobrevalorado, y el desarrollo de la industria está en un estado caótico", 
             "Los efectos son exagerados y los propios productos de cajas sorpresa carecen de sentido de historia y utilidad práctica", 
             "Algunos productos son plagios en el diseño, con mala calidad y trabajo deficiente"]
# Proporciones correspondientes (%)
proporciones = [34.03, 34.95, 41.67, 43.52, 44.68]

y = np.arange(len(opiniones))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Añadir anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(opiniones)
ax.set_xlabel('Proporción (%)')
ax.set_title('Opiniones de los coleccionistas chinos sobre el desarrollo de la industria de las cajas sorpresa en 2025')

plt.tight_layout()
plt.show()