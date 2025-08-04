import matplotlib.pyplot as plt
import numpy as np

# Años
years = [2016, 2017, 2018, 2019, 2020, 2021]
# Producción de vehículos de energía renovable (en 10,000 unidades, datos simulados)
production = [52, 79, 127, 124, 137, 355]
# Tasa de crecimiento (%, datos simulados)
growth_rates = [53.6, 59.9, -2.2, 10.0, 159.5]  # Nota: No hay tasa de crecimiento para 2016 (en comparación con el año anterior). De acuerdo con la lógica de los datos en la figura, los puntos de tasa de crecimiento comienzan en 2017.

# Crear un lienzo y subgráficos
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.set_ylim(0, 700)

# Dibujar un gráfico de barras (producción)
ax1.bar(years, production, color="#A4C639", label="Producción (en 10,000 unidades)")
ax1.set_ylabel("Producción (en 10,000 unidades)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Crear un eje y secundario para dibujar un gráfico de línea (tasa de crecimiento)
ax2 = ax1.twinx()

ax2.set_ylim(-100, 200)

# El eje x del gráfico de línea toma valores de 2017 a 2021 (correspondiente a los puntos de datos de tasa de crecimiento), lo cual es consistente con la figura original.
ax2.plot(years[1:], growth_rates, marker='o', color="#87CEEB", label="Tasa de crecimiento (%)", linewidth=2)
ax2.set_ylabel("Tasa de crecimiento (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Agregar etiquetas de datos al gráfico de barras
for x, y in zip(years, production):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),  # Ajustar finamente la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Agregar etiquetas de datos al gráfico de línea (Nota: Solo etiquetar de 2017 a 2021)
for x, y in zip(years[1:], growth_rates):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(-2, 15),  # Ajustar finamente la posición de la etiqueta
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Establecer las marcas de graduación del eje x
ax1.set_xticks(years)
# Establecer el título
ax1.set_title("Producción de vehículos de energía renovable en China de 2016 a 2021", fontsize=14, fontweight="bold")

# Combinar las leyendas (Nota: El gráfico de línea comienza en 2017, y la visualización de la leyenda debe ajustarse)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Embelezar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()