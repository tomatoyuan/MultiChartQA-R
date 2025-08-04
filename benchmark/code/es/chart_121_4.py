import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2019", "2020", "2021", "2022", "2023", "2024.9"]
# Ingresos operativos (en miles de millones de dólares estadounidenses)
operating_revenue = [2.41, 8.98, 17.79, 12.38, 17.14, 17.88]
# Beneficio neto (en miles de millones de dólares estadounidenses)
net_profit = [-1.07, 0.07, -36.86, -10.28, -5.41, 4.95]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar el gráfico de barras de ingresos operativos (naranja)
bars_rev = ax.bar(x, operating_revenue, color='orange', label='Ingresos Operativos (en miles de millones de dólares estadounidenses)', width=0.4)
# Dibujar el gráfico de barras de beneficio neto (amarillo)
bars_profit = ax.bar(x + 0.4, net_profit, color='gold', label='Beneficio Neto (en miles de millones de dólares estadounidenses)', width=0.4)

# Agregar etiquetas de valor de ingresos operativos
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 0.5, f'{rev}', ha='center', va='bottom')

# Agregar etiquetas de valor de beneficio neto, ajustar la posición según positivo o negativo para garantizar una visualización razonable
for i, profit in enumerate(net_profit):
    if profit < 0:
        ax.text(i + 0.4, profit - 1, f'{profit}', ha='center', va='top')
    else:
        ax.text(i + 0.4, profit + 0.5, f'{profit}', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Monto (en miles de millones de dólares estadounidenses)')
ax.set_xlabel('Año')
ax.set_xticks(x + 0.2)
ax.set_xticklabels(years)
ax.legend(loc='center left')

ax.set_title('Ingresos Operativos y Beneficio Neto de Robinhood desde 2019 hasta septiembre de 2024')
plt.tight_layout()
plt.show()