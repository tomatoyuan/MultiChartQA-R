import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
años = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023P", "2024P", "2025P"]
escala_usuarios = [0.5, 1.0, 1.9, 3.0, 3.6, 4.2, 4.8, 5.3, 5.7, 6.1, 6.4]  # Escala de usuarios (cientos de millones de personas)
crecimiento_anual = [100.0, 95.8, 56.9, 20.7, 17.4, 14.1, 10.5, 8.5, 7.1, 4.8]  # Tasa de crecimiento año tras año (%), tenga en cuenta que no hay datos de crecimiento año tras año para 2015 (o lógicamente, la tasa de crecimiento en 2016 corresponde al cambio de 2015 - 2016, aquí alineado con los datos del gráfico)

x = np.arange(len(años))

fig, ax1 = plt.subplots(figsize=(12, 8))

# Dibujar el eje y izquierdo (escala de usuarios, gráfico de barras)
ax1.bar(x, escala_usuarios, color="#ee8208", width=0.6, label="Escala de Usuarios (Cientos de Millones de Personas)")
ax1.set_ylabel("Escala de Usuarios (Cientos de Millones de Personas)", color="#ee8208")
ax1.set_xticks(x)
ax1.set_xticklabels(años)
ax1.tick_params(axis="y", labelcolor="#ee8208")

# Crear el eje y derecho (tasa de crecimiento año tras año, gráfico de líneas)
ax2 = ax1.twinx()
ax2.plot(x[1:], crecimiento_anual, color="#ffd700", marker="o", label="Tasa de Crecimiento Año tras Año (%)")  # La tasa de crecimiento comienza desde 2016 (x[1:]) correspondiente a los datos
ax2.set_ylabel("Tasa de Crecimiento Año tras Año (%)", color="#ffd700")
ax2.tick_params(axis="y", labelcolor="#ffd700")

# Agregar anotaciones de valores de la escala de usuarios (en el gráfico de barras)
for i, escala in enumerate(escala_usuarios):
    ax1.text(x[i], escala + 0.2, f'{escala}', ha="center", va="bottom", color="#ee8208")

# Agregar anotaciones de valores de la tasa de crecimiento año tras año (en los puntos del gráfico de líneas)
for i, crecimiento in enumerate(crecimiento_anual):
    ax2.text(x[i + 1], crecimiento + 2, f'{crecimiento}%', ha="center", va="bottom", color="#ffd700")  # Corresponde a x[1:], índice +1 para alineación

# Combinar leyendas
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="center left")

ax1.set_title("Escala y Previsión de Consumidores de Pago por Conocimiento Chinos de 2015 a 2025", fontsize=14)
plt.tight_layout()
plt.show()