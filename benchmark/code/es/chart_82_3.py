import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2015, 2022)
# Tasa de penetración del fitness online (%), los datos pueden ser aproximadamente los mismos
penetration = [0.0, 0.8, 17.5, 21.7, 33.2, 42.7, 45.5]

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar el gráfico de línea
line, = ax.plot(years, penetration, marker='o', color="#A4C639", label="Tasa de penetración del fitness online en China (%)", linewidth=2)

# Añadir anotaciones de datos
for x, y in zip(years, penetration):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(years)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel("Tasa de penetración (%)")
# Establecer el título
ax.set_title("Tasa de penetración del fitness online en China de 2015 a 2021", fontsize=14, fontweight="bold")

# Añadir una leyenda
ax.legend()

# Mejorar la apariencia del gráfico ocultando los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()