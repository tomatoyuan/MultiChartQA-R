import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Proporción de la escala de ingresos de la industria de servicios domésticos en el PIB (%)
proporciones = [0.25, 0.33, 0.36, 0.40, 0.47, 0.55, 0.64, 0.73, 0.92, 0.88, 0.89, 0.92]

x = np.arange(len(años))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de línea
linea, = ax.plot(x, proporciones, color='gold', marker='o', label='Proporción de los ingresos de la industria de servicios domésticos en el PIB')

# Agregar anotaciones numéricas
for i, prop in enumerate(proporciones):
    ax.text(i, prop + 0.01, f'{prop}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Proporción (%)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(años)
ax.set_ylim(0.2, 1.0)  # Establecer el rango del eje y para mostrar mejor los datos

ax.legend()
ax.set_title('Proporción de la escala de ingresos de la industria de servicios domésticos chinos en el PIB desde 2012 hasta 2023')

plt.tight_layout()
plt.show()