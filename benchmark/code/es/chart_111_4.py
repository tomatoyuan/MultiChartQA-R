import matplotlib.pyplot as plt
import numpy as np

# Tipos de medios efectivos
medios = ["Fortalecer la supervisión del mercado de telenovelas", "Innovar el contenido del guión", "Mejorar la actuación de los actores", "Reducir las interrupciones comerciales", 
          "Rodar temas diversos", "Mejorar el nivel de producción", "Aumentar los costos de producción"]
# Proporciones correspondientes (%)
proporciones = [39.01, 37.78, 37.28, 33.46, 33.09, 31.85, 31.48]

x = np.arange(len(medios))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(medios, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Medios efectivos para que los espectadores de telenovelas chinas mejoren la calidad y las audiencias de las telenovelas domésticas en 2025')

plt.tight_layout()
plt.show()