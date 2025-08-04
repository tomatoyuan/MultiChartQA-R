import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
# Número de tiendas (en diez mil, datos simulados)
store_count = [339, 506, 602, 579, 657, 906, 917, 891]
# Tasa de crecimiento interanual (%, datos simulados)
growth_rate = [49.3, 19.0, -3.8, 13.5, 37.9, 1.2, -2.8]

# Crear un lienzo y subgráficos
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 2000)

# Dibujar un gráfico de barras (número de tiendas)
ax1.bar(years, store_count, color="#A4C639", label="Número de Tiendas (en diez mil)")
ax1.set_ylabel("Número de Tiendas (en diez mil)", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# Crear un eje y secundario para dibujar un gráfico de líneas (tasa de crecimiento)
ax2 = ax1.twinx()

ax2.set_ylim(-125, 100)

ax2.plot(years[:-1], growth_rate, marker='o', color="#87CEEB", label="Tasa de Crecimiento Interanual (%)", linewidth=2)
ax2.set_ylabel("Tasa de Crecimiento Interanual (%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# Agregar etiquetas de datos al gráfico de barras
for x, y in zip(years, store_count):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#A4C639")

# Agregar etiquetas de datos al gráfico de líneas
for x, y in zip(years[:-1], growth_rate):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),  
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="black")

# Establecer las etiquetas de las marcas del eje x
ax1.set_xticks(years)
# Establecer el título
ax1.set_title("Número de Tiendas de Catering Chinas desde 2014 hasta 2021", fontsize=14, fontweight="bold")

# Combinar leyendas
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Embelezar el gráfico ocultando los bordes superior y derecho
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()