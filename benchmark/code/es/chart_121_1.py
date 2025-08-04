import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2018", "2019", "2020", "2021", "2022", "2023", "2024.9"]
# Ingresos operativos (en miles de millones de yuanes)
operating_revenue = [227.19, 299.49, 352.00, 428.17, 354.71, 361.41, 290.00]
# Beneficio neto (en miles de millones de yuanes)
net_profit = [67.08, 86.37, 111.22, 150.13, 115.07, 121.77, 95.23]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras de ingresos operativos
ax1.bar(x, operating_revenue, color='brown', label='Ingresos Operativos (Miles de Millones de Yuanes)', width=0.4)
ax1.set_ylabel('Ingresos Operativos (Miles de Millones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar el gráfico de barras de beneficio neto
ax2 = ax1.twinx()
ax2.bar(x + 0.4, net_profit, color='gold', label='Beneficio Neto (Miles de Millones de Yuanes)', width=0.4)
ax2.set_ylabel('Beneficio Neto (Miles de Millones de Yuanes)')
ax2.legend(loc='upper right')

# Agregar etiquetas de valor de ingresos operativos
for i, rev in enumerate(operating_revenue):
    ax1.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# Agregar etiquetas de valor de beneficio neto
for i, profit in enumerate(net_profit):
    ax2.text(i + 0.4, profit + 5, f'{profit}', ha='center', va='bottom')

ax1.set_title('Ingresos Operativos y Beneficio Neto de Guotai Junan desde 2018 hasta septiembre de 2024')
plt.tight_layout()
plt.show()