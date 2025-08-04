import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023P", "2024P", "2025P"]
tamaño_del_mercado = [15.9, 26.5, 49.1, 148.3, 278.0, 392.0, 675.0, 1126.5, 1802.7, 2296.6, 2808.8]  # Tamaño del mercado (en miles de millones de yuanes)
crecimiento_anual = [66.7, 85.3, 202.0, 87.5, 41.0, 72.2, 66.9, 60.0, 27.4, 22.3]  # Tasa de crecimiento año tras año (%), tenga en cuenta que no hay crecimiento año tras año para 2015 (o se puede ajustar según los requisitos). Aquí, los datos de la tasa de crecimiento comienzan en 2016, alineándose con la lógica del gráfico

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Trazar el eje y izquierdo (tamaño del mercado, gráfico de barras)
ax1.bar(x, tamaño_del_mercado, color="#ee8208", width=0.6, label="Tamaño del Mercado (en miles de millones de yuanes)")
ax1.set_ylabel("Tamaño del Mercado (en miles de millones de yuanes)", color="#ee8208")
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.tick_params(axis="y", labelcolor="#ee8208")

# Crear el eje y derecho (tasa de crecimiento año tras año, gráfico de línea)
ax2 = ax1.twinx()
ax2.plot(x[1:], crecimiento_anual, color="#ffd700", marker="o", label="Tasa de Crecimiento Año tras Año (%)")  # Comenzar a trazar la línea desde 2016, correspondiente a x[1:]
ax2.set_ylabel("Tasa de Crecimiento Año tras Año (%)", color="#ffd700")
ax2.tick_params(axis="y", labelcolor="#ffd700")

# Agregar anotaciones de valor del tamaño del mercado (en el gráfico de barras)
for i, tamaño in enumerate(tamaño_del_mercado):
    ax1.text(x[i], tamaño + 50, f'{tamaño}', ha="center", va="bottom", color="#ee8208")

# Agregar anotaciones de valor de la tasa de crecimiento año tras año (en los puntos del gráfico de línea)
for i, crecimiento in enumerate(crecimiento_anual):
    ax2.text(x[i + 1], crecimiento + 2, f'{crecimiento}%', ha="center", va="bottom", color="#ffd700")  # Corresponde a x[1:], por lo que el índice es +1

# Combinar leyendas
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="center left")

ax1.set_title("2015 - 2025 Tamaño y Pronóstico del Mercado de Pago por Conocimiento en China", fontsize=14)
plt.tight_layout()
plt.show()