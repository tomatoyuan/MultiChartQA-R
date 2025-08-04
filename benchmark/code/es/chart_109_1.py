import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2018", "2019", "2020", "2021", "2022", "2023", "2024"]
# Tasa de crecimiento interanual (%)
tasas_de_crecimiento = [30.4, 19.1, 8.9, 11.3, 3.6, 12.9, 6.4]

x = np.arange(len(años))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(8, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, tasas_de_crecimiento, color='orange')

# Agregar anotaciones numéricas
for i, tasa in enumerate(tasas_de_crecimiento):
    ax.text(i, tasa + 1, f'{tasa}', ha='center')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.set_ylabel('Tasa de crecimiento interanual (%)')
ax.set_title('Cambios en la tasa de crecimiento interanual de las ventas online rurales de China desde 2018 hasta 2024')

plt.tight_layout()
plt.show()