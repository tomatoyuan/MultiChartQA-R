import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2017", "2018", "2019", "2020", "2021", "2022", "2023"]
# Costos operativos (en miles de millones de yuanes)
operating_cost = [17343.1, 17790.9, 17198.7, 16446.5, 18463.0, 20525.4, 21906.8]
# Ingresos operativos (en miles de millones de yuanes)
operating_revenue = [14610.8, 15107.0, 14788.1, 14240.7, 16142.4, 17716.5, 21442.0]
# Tasa de crecimiento de los ingresos (%)
revenue_growth = [15.8, 3.4, -2.1, -3.7, 13.4, 9.8, 23.7]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

# Dibujar costos operativos (simulados con cajas discontinuas amarillas, primero dibujar las cajas de fondo para los costos)
for i in range(len(years)):
    # Dibujar cajas rectangulares discontinuas amarillas
    rect = plt.Rectangle((x[i] - 0.2, 0), 0.4, operating_cost[i], fill=False, edgecolor='gold', linestyle='--', linewidth=2)
    ax.add_patch(rect)
    # Etiquetar los valores de los costos operativos
    ax.text(x[i], operating_cost[i] + 500, f'{operating_cost[i]}', ha='center', va='bottom')

# Dibujar el gráfico de barras de los ingresos operativos
bars = ax.bar(x, operating_revenue, color='blue', label='Ingresos Operativos (en miles de millones de yuanes)', width=0.4)
# Etiquetar los valores de los ingresos operativos
for i, rev in enumerate(operating_revenue):
    ax.text(i, rev + 500, f'{rev}', ha='center', va='bottom')

# Dibujar las anotaciones circulares para la tasa de crecimiento de los ingresos (simulación aproximada, mostradas arriba con texto)
for i, growth in enumerate(revenue_growth):
    # La posición de la anotación circular está arriba de la barra, resaltada con un fondo circular (simplificado)
    circle = plt.Circle((x[i], operating_revenue[i] + 2000), 0.3, color='lightcoral', alpha=0.3)
    ax.add_artist(circle)
    ax.text(x[i], operating_revenue[i] + 1500, f'{growth}%', ha='center', va='center', fontsize=12, color='red')

ax.set_ylabel('Monto (en miles de millones de yuanes)')
ax.set_xlabel('Año')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('Ingresos y Costos Operativos de los Fabricantes de Vehículos Eléctricos de Acciones A en China desde 2017 hasta 2023')

plt.ylim(0, max(operating_cost) + 3000)  # Ajustar el rango del eje y para acomodar las anotaciones
plt.tight_layout()
plt.show()