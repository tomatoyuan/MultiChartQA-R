import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rcParams
from pathlib import Path
import numpy as np

# Datos de años
años = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024])
# Datos de tasa de penetración de Internet
tasas = np.array([59.6, 64.5, 70.4, 73.0, 75.6, 77.5, 78.6])

# Crear un gráfico de barras
fig, ax = plt.subplots()
barras = ax.bar(años, tasas, color='orange')

# Etiquetar el valor de cada barra
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2., altura,
            f'{altura}',
            ha='center', va='bottom')

# Establecer el título del gráfico y las etiquetas de los ejes
ax.set_title('Tasa de penetración de Internet en China desde 2018 hasta 2024')
ax.set_xlabel('Año')
ax.set_ylabel('Tasa de penetración (%)')

# Mostrar el gráfico
plt.show()