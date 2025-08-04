import matplotlib.pyplot as plt
import numpy as np

# Años
años = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# Ventas de MPV (en 10,000 vehículos, datos simulados)
ventas = [49.8, 49.3, 130.5, 191.4, 210.7, 249.7, 207.1, 173.5, 138.4, 105.4, 105.5]
# Tasa de crecimiento anual (%, datos simulados)
tasas_de_crecimiento = [11.7, -0.9, 164.5, 46.7, 10.1, 18.5, -17.1, -16.2, -20.2, -23.8, 0.1]

# Crear un lienzo y subgráficos
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 500)

# Dibujar un gráfico de barras (ventas de MPV)
ax1.bar(años, ventas, color="#A4C639", label="Ventas de MPV (10,000 vehículos)")
ax1.set_ylabel("Ventas de MPV (10,000 vehículos)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Crear un eje y secundario para dibujar un gráfico de línea (tasa de crecimiento)
ax2 = ax1.twinx()

ax2.set_ylim(-200, 200)

ax2.plot(años, tasas_de_crecimiento, marker='o', color="#87CEEB", label="Tasa de Crecimiento Anual (%)", linewidth=2)
ax2.set_ylabel("Tasa de Crecimiento Anual (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Agregar etiquetas de datos al gráfico de barras
for x, y in zip(años, ventas):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Agregar etiquetas de datos al gráfico de línea
for x, y in zip(años, tasas_de_crecimiento):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Establecer marcas de graduación en el eje x
ax1.set_xticks(años)
# Establecer el título
ax1.set_title("Ventas y Tasa de Crecimiento de MPV en China de 2011 a 2021", fontsize=14, fontweight="bold")

# Combinar leyendas
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

# Mejorar la apariencia del gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()