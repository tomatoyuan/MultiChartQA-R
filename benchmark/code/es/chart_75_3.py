import matplotlib.pyplot as plt
import numpy as np

# Años
years = ["2017", "2018", "2019", "2020", "2021"]
# Volumen de consumo de granos de café verde (en miles de toneladas), los datos pueden ser aproximadamente los mismos
bean_consumption = [13.5, 9.9, 12.9, 14.4, 21.9]
# Volumen de importación de productos de café (en miles de toneladas), los datos pueden ser aproximadamente los mismos
import_volume = [3.3, 3.6, 3.8, 4.0, 3.9]

# Corrección: Asegurarse de que las longitudes de los dos datos de tasa de crecimiento sean iguales (ambas son 1 menos que los datos originales)
# Tasa de crecimiento del consumo de granos de café verde (%), los datos pueden ser aproximadamente los mismos
bean_growth_rate = [-26.7, 30.3, 11.6, 52.1]  # Eliminar el primer punto de datos incorrecto
# Tasa de crecimiento de las importaciones de productos de café (%), los datos pueden ser aproximadamente los mismos
import_growth_rate = [9.1, 5.6, 5.3, -2.5]

# Crear un lienzo y subgráficos con un eje y dual
fig, ax1 = plt.subplots(figsize=(8, 6))
ax2 = ax1.twinx()

ax1.set_ylim(0, 40)
ax2.set_ylim(-200, 100)

# Dibujar el gráfico de barras del consumo de granos de café verde
x = np.arange(len(years))
bar_width = 0.35
bean_bars = ax1.bar(x - bar_width / 2, bean_consumption, width=bar_width, color="#A4C639", label="Consumo de granos de café verde (en miles de toneladas)")
# Dibujar el gráfico de barras del volumen de importación de productos de café
import_bars = ax1.bar(x + bar_width / 2, import_volume, width=bar_width, color="#64B5F6", label="Volumen de importación de productos de café (en miles de toneladas)")

# Dibujar el gráfico de líneas de las tasas de crecimiento (a partir de 2018 porque no hay datos de tasa de crecimiento para 2017)
growth_x = x[1:]  # Corresponde a 2018 - 2021
bean_growth_line, = ax2.plot(growth_x, bean_growth_rate, marker='o', color="#A4C639", label="Tasa de crecimiento del consumo de granos de café verde (%)", linewidth=2, linestyle='--')
import_growth_line, = ax2.plot(growth_x, import_growth_rate, marker='o', color="#64B5F6", label="Tasa de crecimiento de las importaciones de productos de café (%)", linewidth=2, linestyle='--')

# Agregar etiquetas de datos (gráfico de barras)
for bar in bean_bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

for bar in import_bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Agregar etiquetas de datos (gráfico de líneas)
for x_val, y_val in zip(growth_x, bean_growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="#A4C639")

for x_val, y_val in zip(growth_x, import_growth_rate):
    ax2.annotate(f'{y_val}%',
                 xy=(x_val, y_val),
                 xytext=(0, 5),
                 textcoords='offset points',
                 ha='center', va='bottom',
                 color="black")

# Configurar los ejes y el título
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.set_ylabel("Cantidad (en miles de toneladas)", color="#333333")
ax2.set_ylabel("Tasa de crecimiento (%)", color="#333333")
ax1.set_title("Consumo de granos de café verde e importación de productos de café en China de 2017 a 2021", fontsize=14, fontweight="bold")

# Combinar las leyendas
handles, labels = ax1.get_legend_handles_labels()
handles.extend([bean_growth_line, import_growth_line])
labels.extend([bean_growth_line.get_label(), import_growth_line.get_label()])
ax1.legend(handles, labels, loc='upper left')

# Embellir el gráfico
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()