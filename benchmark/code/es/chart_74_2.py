import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2016", "2017", "2018", "2019", "2020", "2021"]
# Tasa de crecimiento de la economía digital (%)
digital_economy_growth = [18.9, 20.3, 20.9, 15.6, 9.7, 16.2]
# Tasa de crecimiento del PIB (%)
gdp_growth = [6.8, 6.9, 6.7, 6.0, 2.2, 8.1]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Trazar el gráfico de línea de la tasa de crecimiento de la economía digital
digital_line, = ax.plot(years, digital_economy_growth, marker='o', color="#A4C639", label="Tasa de crecimiento de la economía digital (%)", linewidth=2)
# Trazar el gráfico de línea de la tasa de crecimiento del PIB
gdp_line, = ax.plot(years, gdp_growth, marker='o', color="#64B5F6", label="Tasa de crecimiento del PIB (%)", linewidth=2)

# Agregar etiquetas de datos para la tasa de crecimiento de la economía digital
for x, y in zip(years, digital_economy_growth):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Agregar etiquetas de datos para la tasa de crecimiento del PIB
for x, y in zip(years, gdp_growth):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# Establecer la etiqueta del eje y
ax.set_ylabel("Tasa de crecimiento (%)")
# Establecer el título
ax.set_title("Tasa de crecimiento de la economía digital y del PIB de China desde 2016 hasta 2021", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Emprolijar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()