import matplotlib.pyplot as plt
import numpy as np

# Datos
causas = ["Razones emocionales", "Usar demasiado el teléfono móvil antes de dormir", "Presión laboral",
          "Problemas de salud personal", "Presión en la vida", "Problemas ambientales", "Problemas de dieta",
          "Postura incorrecta al dormir"]
proporciones = [47.3, 37.7, 37.4, 32.7, 32.0, 30.8, 27.7, 21.9]

y = np.arange(len(causas))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar etiquetas numéricas a la derecha de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion + 1, i, f'{proporcion}%', va='center')

ax.set_yticks(y)
ax.set_yticklabels(causas)
ax.set_xlabel('Proporción (%)')
ax.set_title('Principales razones de la mala calidad del sueño entre los residentes chinos')

plt.tight_layout()
plt.show()