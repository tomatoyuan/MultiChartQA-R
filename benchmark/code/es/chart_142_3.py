import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2020", "2021", "2022", "2023", "2024P", "2025P"]  # "P" para "Previsión" en lugar de "E" de "Estimado"
tamaño_del_mercado = [240.0, 360.0, 1116.0, 2845.8, 5197.4, 8287.0]
tasa_de_crecimiento = [np.nan, 50.0, 210.0, 155.0, 82.6, 59.4]  # No hay datos año - a - año para 2020, marcado con np.nan

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras del tamaño del mercado
ax1.bar(x, tamaño_del_mercado, color='orange', label='Tamaño del Mercado (Miles de Millones de Yuan)')
ax1.set_ylabel('Tamaño del Mercado (Miles de Millones de Yuan)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.legend(loc='upper left')

# Crear un eje y secundario y dibujar el gráfico de línea del crecimiento año - a - año
ax2 = ax1.twinx()
ax2.plot(x[1:], tasa_de_crecimiento[1:], marker='o', color='gold', label='Crecimiento Año - a - Año (%)', linewidth=2)  # No hay datos año - a - año para 2020, comenzar desde 2021
ax2.set_ylabel('Crecimiento Año - a - Año (%)')
ax2.legend(loc='center right')

# Añadir anotaciones para los valores del tamaño del mercado
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(i, tamaño + 100, f'{tamaño}', ha='center', va='bottom')

# Añadir anotaciones para los valores del crecimiento año - a - año (sin datos para 2020, comenzar desde 2021)
for i, tasa in enumerate(tasa_de_crecimiento[1:], start=1):
    ax2.text(i, tasa + 5, f'{tasa}%', ha='center', va='bottom')

ax1.set_title('Tamaño y Previsión del Mercado de Comercio Electrónico de Transmisión en Vivo Transfronterizo en China desde 2020 hasta 2025')

plt.tight_layout()
plt.show()