import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024P", "2025P"]
# Tamaño del mercado (trillones de yuanes)
tamaño_mercado = [22.6, 27.2, 31.3, 35.8, 39.2, 45.5, 50.2, 56.1, 63.2, 70.8]
# Crecimiento interanual (%)
crecimiento_interanual = [20.4, 21.4, 15.1, 14.4, 9.5, 16.1, 10.3, 11.7, 12.7, 12.1]

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(10, 6))

# Dibujar el gráfico de barras del tamaño del mercado (simular el estilo del icono, aproximar con símbolos personalizados)
for i in range(len(años)):
    # Dibujar el gráfico de barras del símbolo "¥" que representa el tamaño del mercado (simplificado como un rectángulo naranja + símbolo de texto)
    rect = plt.Rectangle((x[i] - 0.2, 0), 0.4, tamaño_mercado[i], color='orange')
    ax1.add_patch(rect)
    ax1.text(x[i], tamaño_mercado[i] + 1, f'¥{tamaño_mercado[i]}', ha='center', va='bottom')

ax1.set_ylabel('Tamaño del Mercado (Trillones de Yuanes)')
ax1.set_xlabel('Año')
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.set_ylim(0, max(tamaño_mercado) + 5)  # Reservar espacio para las etiquetas
ax1.legend(['Tamaño del Mercado (Trillones de Yuanes)'], loc='upper left')

# Crear un eje y secundario y dibujar el gráfico de línea del crecimiento interanual
ax2 = ax1.twinx()
ax2.plot(x, crecimiento_interanual, marker='o', color='gold', label='Crecimiento Interanual (%)')
ax2.set_ylabel('Crecimiento Interanual (%)')
ax2.legend(loc='upper right')

# Agregar etiquetas para los valores de crecimiento interanual
for i, crecimiento in enumerate(crecimiento_interanual):
    ax2.text(i, crecimiento + 0.5, f'{crecimiento}%', ha='center', va='bottom')

ax1.set_title('Escala total de la economía digital de China y pronóstico de 2016 a 2025')

plt.tight_layout()
plt.show()