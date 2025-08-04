import matplotlib.pyplot as plt
import numpy as np

# Años y fechas
years = ["2020/3/31", "2021/3/31", "2022/3/31", "2023/3/31", "2024/3/31"]
# Ingresos operativos totales (en miles de millones de yuanes)
operating_revenue = [518.5, 593, 802.4, 828.9, 985.5]
# Beneficio neto atribuible a la empresa matriz (en miles de millones de yuanes)
net_profit = [26.51, 50.93, 54.44, 47.14, 58.92]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(8, 6))

# Trazar el gráfico de barras de los ingresos operativos totales
ax.bar(x, operating_revenue, color='orange', label='Ingresos Operativos Totales (Miles de Millones de Yuanes)', width=0.6)
# Trazar el gráfico de barras del beneficio neto atribuible a la empresa matriz
ax.bar(x, net_profit, color='red', label='Beneficio Neto Atribuible a la Empresa Matriz (Miles de Millones de Yuanes)', width=0.2)

# Agregar etiquetas para los valores de los ingresos operativos totales
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# Agregar etiquetas para los valores del beneficio neto atribuible a la empresa matriz
for i, profit in enumerate(net_profit):
    ax.text(i, profit + 2, f'{profit}', ha='center', va='bottom')

ax.set_ylabel('Monto (Miles de Millones de Yuanes)')
ax.set_xlabel('Fecha')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Ingresos Operativos y Beneficio Neto Atribuible a la Empresa Matriz de Chow Tai Fook de 2020 a 2024')

plt.tight_layout()
plt.show()