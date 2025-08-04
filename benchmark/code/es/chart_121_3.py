import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2018", "2019", "2020", "2021", "2022", "2023"]
# Ingresos operativos (en miles de millones de yuanes)
operating_revenue = [99.25, 170.41, 237.49, 359.83, 336.42, 336.44]
# Beneficio neto (en miles de millones de yuanes)
net_profit = [28.87, 52.28, 72.44, 104.30, 77.61, 78.79]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 6))

# Dibujar el gráfico de barras para los ingresos operativos
bars_rev = ax.bar(x, operating_revenue, color='brown', label='Ingresos Operativos (en miles de millones de yuanes)', width=0.4)
# Dibujar el gráfico de barras para el beneficio neto (desplazado a la derecha para evitar superposición)
bars_profit = ax.bar(x + 0.4, net_profit, color='gold', label='Beneficio Neto (en miles de millones de yuanes)', width=0.4)

# Añadir etiquetas para los valores de los ingresos operativos
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 10, f'{rev}', ha='center', va='bottom')

# Añadir etiquetas para los valores del beneficio neto
for i, profit in enumerate(net_profit):
    ax.text(i + 0.4, profit + 5, f'{profit}', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Monto (en miles de millones de yuanes)')
ax.set_xlabel('Año')
ax.set_xticks(x + 0.2)
ax.set_xticklabels(years)
ax.legend(loc='lower right')

# Añadir una caja de información en el lado derecho (simulando el estilo de la imagen original)
info_box_text = (
    "En 2022, la aplicación de China Galaxy Securities\n"
    "abrió 1.1084 millones de nuevas cuentas para el negocio de gestión de riqueza,\n"
    "con una participación de mercado del 7.48% en la apertura de cuentas."
)
# Dibujar la caja de información en el lado derecho del gráfico
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="orange", lw=2)
ax.text(5.8, 300, info_box_text, fontsize=10, bbox=bbox_props, va='top')

ax.set_title('Ingresos Operativos y Beneficio Neto de China Galaxy Securities de 2018 a 2023')
plt.tight_layout()
plt.show()