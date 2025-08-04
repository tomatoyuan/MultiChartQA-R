import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from pathlib import Path
import numpy as np

# Años
years = np.arange(2015, 2025)
# Producción de datos (en diez miles de toneladas)
outputs = [6210.97, 6379.48, 6445.33, 6457.66, 6480.36, 
           6549.02, 6690.29, 6865.91, 7116.24, 7366.50]

# Crear un lienzo y ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
bars = ax.bar(years, outputs, color='#FFA07A')  # Establecer el color del gráfico de barras

# Agregar anotaciones numéricas
for bar, output in zip(bars, outputs):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, 
            f'{output}', ha='center', va='bottom')

# Establecer el título y las etiquetas de los ejes
ax.set_title('Producción total de productos acuáticos en China desde 2015 hasta 2024')
ax.set_xlabel('Año')
ax.set_ylabel('Producción (en diez miles de toneladas)')

# Establecer el rango del eje y
ax.set_ylim(5600, 7600)  

# Mostrar el gráfico
plt.show()