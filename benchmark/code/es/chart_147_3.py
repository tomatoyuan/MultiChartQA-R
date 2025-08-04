import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
años = ["2019", "2020", "2021", "2022", "2023P", "2024P"]  # "P" para "Predicción"
tamaño_del_mercado = [1945.3, 2283.0, 2793.7, 3387.1, 4020.8, 4744.5]  # Tamaño del mercado (en miles de millones de yuanes)
tasas_de_crecimiento = [17.4, 22.4, 21.2, 18.7, 18.0]  # Tasa de crecimiento año tras año (%)

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(10, 7))

# Dibujar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='coral', label='Tamaño del Mercado (miles de millones de yuanes)')
ax1.set_ylabel('Tamaño del Mercado (miles de millones de yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='center left')

# Crear un eje y secundario para la tasa de crecimiento
ax2 = ax1.twinx()
ax2.plot(x[1:], tasas_de_crecimiento, marker='o', color='gold', label='Tasa de Crecimiento Anual (%)', linewidth=2)
ax2.set_ylabel('Tasa de Crecimiento Anual (%)')
ax2.legend(loc='center right')

# Anotaciones del gráfico de líneas (cerca de la línea, evitando superposiciones)
etiquetas_de_tasa = [17.4, 22.4, 21.2, 18.7, 18.0]
for i, tasa in enumerate(etiquetas_de_tasa):
    # Ajustar posición según el valor de la tasa
    if tasa > 20:  # Tasas altas: anotar debajo de la línea
        ax2.text(x[1+i], tasa, f'{tasa}%', 
                 ha='center', va='top', color='black', fontsize=9)
    else:  # Tasas bajas: anotar encima de la línea
        ax2.text(x[1+i], tasa, f'{tasa}%', 
                 ha='center', va='bottom', color='black', fontsize=9)

# Anotaciones del tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 50, f'{tamaño}', ha='center', va='bottom', color='black')

ax1.set_title('Tamaño y predicción del mercado de alimentos funcionales para adelgazar en China (2019-2024)')
plt.tight_layout()
plt.show()