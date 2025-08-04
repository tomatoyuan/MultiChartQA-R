import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2011, 2022)
# Costo total de logística (trillones)
logistics_cost = [8.4, 9.4, 10.2, 10.6, 10.8, 11.1, 12.1, 13.3, 14.6, 14.9, 16.7]
# Proporción del PIB (%)
gdp_ratio = [17.2, 17.4, 17.1, 16.5, 15.7, 14.9, 14.7, 14.8, 14.7, 14.7, 14.6]

# Crear un lienzo con un eje y secundario
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 32)
ax2.set_ylim(5, 20)

# Dibujar un gráfico de barras para el costo total de logística
ax1.bar(years, logistics_cost, width=0.6, color="#C63982", label="Costo total de logística (trillones)")
# Dibujar un gráfico de línea para la proporción del PIB
ax2.plot(years, gdp_ratio, marker='o', color="#64B5F6", label="Proporción del PIB (%)", linewidth=2)

# Agregar etiquetas de datos al gráfico de barras
for x, y in zip(years, logistics_cost):
    ax1.annotate(f'{y}',
                 xy=(x, y),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Agregar etiquetas de datos al gráfico de línea
for x, y in zip(years, gdp_ratio):
    ax2.annotate(f'{y}%',
                 xy=(x, y),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#64B5F6")

# Establecer etiquetas de los ejes y título
ax1.set_xlabel("Año")
ax1.set_ylabel("Costo total de logística (trillones)", color="#C63982")
ax2.set_ylabel("Proporción del PIB (%)", color="#64B5F6")
ax1.set_title("Costo total de logística y su proporción del PIB en China desde 2011 hasta 2021", fontsize=14, fontweight="bold")

# Establecer las marcas del eje x
ax1.set_xticks(years)
ax1.set_xticklabels(years)

# Combinar las leyendas
handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1 + handles2, labels1 + labels2, loc='upper left')

# Embelezar el gráfico ocultando los bordes superior y derecho
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()