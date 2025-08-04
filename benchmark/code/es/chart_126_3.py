import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", 
         "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
# Volumen total de transacciones (en miles de millones de yuanes)
transaction_volume = [0.5, 9.4, 52.0, 191.0, 350.0, 805.0, 1230.0, 1770.0, 
                      2954.3, 3953.2, 6000.0, 8600.0, 9651.2, 11154.0, 11386.0, 14418.0]
# Tasa de crecimiento (%)
growth_rate = [np.nan, 1770.0, 455.6, 267.3, 83.2, 130.0, 52.8, 43.9, 
               66.9, 33.8, 51.8, 43.3, 12.2, 15.6, 2.1, 26.6]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(14, 8))

# Trazar el gráfico de barras del volumen total de transacciones
ax1.bar(x, transaction_volume, color='orange', label='Volumen total de transacciones (en miles de millones de yuanes)')
ax1.set_ylabel('Volumen total de transacciones (en miles de millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='center left')

# Crear un eje y secundario y trazar el gráfico de línea de la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x, growth_rate, marker='o', color='gold', label='Tasa de crecimiento (%)')
ax2.set_ylabel('Tasa de crecimiento (%)')
ax2.legend(loc='center right')

# Añadir anotaciones para el volumen total de transacciones
for i, vol in enumerate(transaction_volume):
    ax1.text(i, vol + 200, f'{vol}', ha='center', va='bottom')

# Añadir anotaciones para la tasa de crecimiento (Nota: no hay tasa de crecimiento en 2009, comenzar desde 2010)
for i, rate in enumerate(growth_rate):
    if i > 0:  # Saltar 2009
        ax2.text(x[i], rate + 10, f'{rate}%', ha='center', va='bottom')

ax1.set_title('Volumen total de transacciones del "Double Eleven" en las plataformas de comercio electrónico chinas desde 2009 hasta 2024')

plt.tight_layout()
plt.show()