import matplotlib.pyplot as plt
import numpy as np

# Tipos de manualidades hechas a mano
tipos_manualidades = ["Manualidades de la serie Gundam", "Manualidades de tipo juego", "Manualidades de personajes virtuales", 
                      "Manualidades de las series de películas de Marvel y DC", "Manualidades de modelos de automóvil", 
                      "Manualidades de anime doméstico (por ejemplo, Qin Shi Ming Yue)", 
                      "Manualidades de anime japonés (por ejemplo, Naruto)"]
# Proporciones correspondientes (%)
proporciones = [28.94, 30.09, 32.41, 36.81, 37.04, 38.66, 38.89]

y = np.arange(len(tipos_manualidades))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(tipos_manualidades)
ax.set_xlabel('Proporción (%)')
ax.set_title('Tipos de manualidades favoritos de los consumidores de manualidades chinos en 2025')

plt.tight_layout()
plt.show()