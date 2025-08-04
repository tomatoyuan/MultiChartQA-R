import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2001, 2022)
# Número de ofertas de trabajo en Hong Kong (en decenas de miles), los datos pueden ser aproximadamente los mismos
vacancies = [1.7, 1.6, 2.1, 2.9, 3.7, 3.9, 4.8, 3.2, 3.5, 4.8, 5.5, 6.5, 7.2, 7.4, 7.1, 6.7, 7.4, 7.8, 5.4, 3.5, 6.1]

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de líneas
line, = ax.plot(years, vacancies, marker='o', color="#39C6BA", label="Número de ofertas de trabajo en Hong Kong (en decenas de miles)", linewidth=2)

# Agregar anotaciones de datos
for x, y in zip(years, vacancies):
    ax.annotate(f'{y}',
                xy=(x, y),
                xytext=(5, 5),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom',
                color="#39C6BA")

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
# Establecer la etiqueta del eje y
ax.set_ylabel("Número de ofertas de trabajo en Hong Kong (en decenas de miles)")
# Establecer el título
ax.set_title("Número de ofertas de trabajo en Hong Kong desde 2001 hasta 2021", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()