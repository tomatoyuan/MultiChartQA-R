import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023"]
salario_promedio = [4.8, 4.9, 5.3, 6.3, 7.1, 9.1, 9.6, 11.1, 11.8]
tasa_de_crecimiento = [23.1, 2.1, 8.2, 18.9, 12.7, 28.2, 5.5, 15.6, 6.3]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 7))

# Trazar el gráfico de barras del salario promedio
ax1.bar(x, salario_promedio, color='orange', label='Salario Promedio (Miles de Yuanes)')
ax1.set_ylabel('Salario Promedio (Miles de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, tasa_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento (%)')
ax2.legend(loc='center right')

# Añadir etiquetas para los valores del salario promedio
for i, salario in enumerate(salario_promedio):
    ax1.text(i, salario + 0.3, f'{salario}', ha='center', va='bottom')

# Añadir etiquetas para los valores de la tasa de crecimiento
for i, tasa in enumerate(tasa_de_crecimiento):
    ax2.text(i, tasa + 1, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Salarios de la Industria de Servicios Domésticos y sus Tasas de Crecimiento desde 2015 hasta 2023')

plt.tight_layout()
plt.show()