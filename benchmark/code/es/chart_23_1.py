import matplotlib.pyplot as plt
import numpy as np

# Datos
ciudades = ["Shenzhen", "Beijing", "Guangzhou", "Wuhan", "Changsha"]
ranking = [1, 2, 3, 4, 5]

# Crear un gráfico de barras horizontales
plt.figure(figsize=(10, 6))
barras = plt.barh(ciudades, ranking, color='#6CB4EE')

# Añadir números de ranking a cada barra
for i, v in enumerate(ranking):
    plt.text(v + 0.1, i, str(v), va='center', fontsize=12)

# Añadir título y etiquetas
plt.title('Lista de Ranking de Ciudades para Citas a Ciegas', fontsize=16, pad=15)
plt.xlabel('Ranking', fontsize=12, labelpad=10)
plt.ylabel('Ciudad', fontsize=12, labelpad=10)

# Establecer el rango del eje x
plt.xlim(0, max(ranking) + 1)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()