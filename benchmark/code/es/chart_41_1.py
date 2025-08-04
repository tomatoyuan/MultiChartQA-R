import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
# Datos del tamaño del mercado (aproximadamente simulados, cercanos a la situación real)
market_size = np.array([2000, 2500, 2700, 2800, 3000, 3300])  

# Crear un lienzo
fig, ax = plt.subplots()
# Dibujar un gráfico de barras, establecer el color en azul, similar a la imagen original
ax.bar(years, market_size, color='#4B79A1')  

# Agregar un título, coincidir con el formato del título de la imagen original
ax.set_title('Tamaño del mercado de consumo urbano (Gran Felino) desde 2020 hasta 2025', fontdict={'fontsize': 12})  
# Establecer la etiqueta del eje x
ax.set_xlabel('Año')  
# Establecer la etiqueta del eje y
ax.set_ylabel('Tamaño del mercado (Miles de millones de yuanes)')  

# Marcar la anotación de texto para la primera vez que supera los 300 mil millones en 2024, la posición se puede ajustar finamente
ax.text(2024, 3000 + 50, 'Superó los 300 mil millones por primera vez', ha='center', va='bottom', fontsize=10, color='orange')  

# Establecer las marcas del eje x, mostrar 2025 como 2025E
ax.set_xticks(years)
ax.set_xticklabels([str(year) + 'E' if year == 2025 else str(year) for year in years])

# Establecer el rango de las marcas del eje y para que la visualización sea más adecuada para los datos
ax.set_ylim(0, 3500)  

# Mostrar el gráfico
plt.show()