import matplotlib.pyplot as plt
import numpy as np

# Razones para elegir la reproducción a doble velocidad
razones = ["Mala calidad de video", "Está acostumbrado a la reproducción a doble velocidad y se siente más cómodo", "La velocidad de habla del actor es demasiado lenta, lo que afecta el ritmo de visualización", 
           "Algún contenido es aburrido o prolijo, no quiere verlo detenidamente", "Ahorrar tiempo y comprender rápidamente la trama"]
# Proporciones correspondientes (%)
proporciones = [29.33, 41.71, 45.71, 46.29, 50.10]

y = np.arange(len(razones))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(razones)
ax.set_xlabel('Proporción (%)')
ax.set_title('Razones por las que los espectadores de dramas de televisión chinos eligen la reproducción a doble velocidad en 2025')

plt.tight_layout()
plt.show()