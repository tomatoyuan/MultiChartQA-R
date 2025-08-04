import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Número de nacimientos (en diez mil personas)
nacimientos = [1635, 1640, 1687, 1655, 1786, 1723, 1523, 1465, 1200, 1062, 956, 902]

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, nacimientos, color='gold')

# Agregar anotaciones numéricas
for i, nacimiento in enumerate(nacimientos):
    ax.text(i, nacimiento + 20, f'{nacimiento}', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Número de nacimientos (en diez mil personas)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)

ax.set_title('Número de nacimientos en China desde 2012 hasta 2023')

plt.tight_layout()
plt.show()