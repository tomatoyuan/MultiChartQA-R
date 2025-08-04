import matplotlib.pyplot as plt
import numpy as np

# Períodos de visualización
periodos_de_visualizacion = ["Fines de semana y festivos", "Cuando se está ocioso y aburrido", "Durante el tiempo fragmentado habitual", "Antes de dormir", "Cuando se sufre insomnio o está estresado", "Durante las comidas"]
# Proporciones correspondientes (%)
proporciones = [41.73, 41.36, 37.65, 31.36, 30.74, 26.67]

x = np.arange(len(periodos_de_visualizacion))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(8, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar etiquetas numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(periodos_de_visualizacion, rotation=20, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Períodos de visualización de los espectadores de dramas de televisión chinos en 2025')

plt.tight_layout()
plt.show()