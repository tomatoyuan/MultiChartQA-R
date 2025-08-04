import matplotlib.pyplot as plt
import numpy as np

# Años
years = [2000, 2005, 2010, 2014, 2020]
# Tasas de obesidad en adultos (%)
obesity_rates = [7.0, 8.0, 9.9, 10.5, 14.6]
# Tasas de sobrepeso en adultos (%)
overweight_rates = [22.8, 29.1, 32.1, 32.7, 35.0]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(7, 5))

# Dibujar el gráfico de líneas (Tasa de sobrepeso en adultos, verde)
overweight_line, = ax.plot(years, overweight_rates, marker='o', color="#A4C639", label="Tasa de Sobrepeso en Adultos (%)", linewidth=2)
# Dibujar el gráfico de líneas (Tasa de obesidad en adultos, azul)
obesity_line, = ax.plot(years, obesity_rates, marker='o', color="#87CEEB", label="Tasa de Obesidad en Adultos (%)", linewidth=2)

# Agregar etiquetas de datos (Tasa de sobrepeso en adultos)
for x, y in zip(years, overweight_rates):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Agregar etiquetas de datos (Tasa de obesidad en adultos)
for x, y in zip(years, obesity_rates):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#87CEEB")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(years)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Tasa (%)")
# Establecer el título
ax.set_title("Tasas de Obesidad y Sobrepeso en Adultos en China desde 2000 hasta 2020", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Emprolijar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()