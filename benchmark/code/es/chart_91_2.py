import matplotlib.pyplot as plt
import numpy as np

# Nodos de tiempo simulados (simplificado, se puede refinar según la situación real)
fechas = np.arange(2017, 2022, 0.5)
# Datos de precios simulados (tendencia general, se puede ajustar)
precios = [1.8, 1.6, 1.9, 1.8, 1.7, 1.8, 1.7, 1.8, 1.9, 1.8]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 4))

ax.set_ylim(0, 8)

# Dibujar un gráfico de línea
ax.plot(fechas, precios, color="#A4C639", label="Acero inoxidable: Bobina 304/2B 1*1219*C: Wuxi (10,000 yuan/ton)", linewidth=2)

# Simular la etiquetación de nodos clave (ejemplo, se puede completar según la situación real)
fechas_clave = [2017, 2021]
precios_clave = [1.8, 2.2]
for x, y in zip(fechas_clave, precios_clave):
    ax.annotate(f'{y}', xy=(x, y), xytext=(5, 5), textcoords="offset points", ha='center', va='bottom', color="#A4C639")

# Establecer las marcas del eje x (simplificado para mostrar años, se puede refinar)
ax.set_xticks(np.arange(2017, 2022))
ax.set_xticklabels([f"{year}.1" for year in range(2017, 2022)])  # Simular el formato de tiempo del gráfico original

# Establecer la etiqueta del eje y
ax.set_ylabel("Precio (10,000 yuan/ton)")
# Establecer el título
ax.set_title("Tendencia de precios del acero inoxidable en China de 2017 a 2021", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Mejorar la apariencia del gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()