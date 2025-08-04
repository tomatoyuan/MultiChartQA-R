import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2015, 2024)
# Tasa de penetración del mercado (%), los datos pueden ser aproximadamente los mismos
penetration = [51.6, 55.6, 59.6, 63.9, 72.2, 77.1, 82.0, 85.2, 88.6]

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de línea
line, = ax.plot(years, penetration, marker='o', color="#C63982", label="Tasa de penetración (%)", linewidth=2)

# Agregar anotaciones de datos
for x, y in zip(years, penetration):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom',
                color="#C63982")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(years)
ax.set_xticklabels([f"{year}" for year in years])
# Establecer la etiqueta del eje y
ax.set_ylabel("Tasa de penetración (%)")
# Establecer el título
ax.set_title("Tasa de penetración y pronóstico del mercado de pañales para bebés en China de 2015 a 2023", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embellir el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()