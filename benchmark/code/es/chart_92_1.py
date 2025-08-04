import matplotlib.pyplot as plt
import numpy as np

# Años
years = [2016, 2017, 2018, 2019, 2020, 2021]
# Gasto de consumo per cápita en transporte y comunicaciones de los residentes (yuan, datos simulados)
expenditures = [2338, 2499, 2675, 2862, 2761, 3156]
# Tasa de crecimiento (%, datos simulados)
growth_rates = [12.0, 6.9, 7.0, 7.0, -3.5, 14.3]

# Crear un lienzo y subgráficos
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.set_ylim(0, 6000)

# Dibujar un gráfico de barras (gasto de consumo)
ax1.bar(years, expenditures, color="#A4C639", label="Gasto de consumo per cápita en transporte y comunicaciones de los residentes (yuan)")
ax1.set_ylabel("Gasto de consumo (yuan)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Crear un eje y secundario para dibujar un gráfico de línea (tasa de crecimiento)
ax2 = ax1.twinx()

ax2.set_ylim(-50, 25)

ax2.plot(years, growth_rates, marker='o', color="#87CEEB", label="Tasa de crecimiento (%)", linewidth=2)
ax2.set_ylabel("Tasa de crecimiento (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Agregar etiquetas de datos al gráfico de barras
for x, y in zip(years, expenditures):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Agregar etiquetas de datos al gráfico de línea
for x, y in zip(years, growth_rates):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Establecer las marcas del eje x
ax1.set_xticks(years)
# Establecer el título
ax1.set_title("Gasto de consumo per cápita en transporte y comunicaciones de los residentes chinos de 2016 a 2021", fontsize=14, fontweight="bold")

# Combinar leyendas
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Embelezar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()