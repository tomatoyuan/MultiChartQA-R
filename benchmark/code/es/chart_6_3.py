import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
categorias = ["Ciudades de primer nivel", "Ciudades de segundo nivel", "Ciudades de tercer nivel", "Ciudades de cuarto nivel"]
porcentajes = [42, 20, 17, 12]  # Datos de proporción
tazas_de_crecimiento = [2, 3, -8, -7]   # Datos de tasa de crecimiento

# Crear un lienzo y dos ejes Y
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

# Dibujar un gráfico de barras para las proporciones
x = np.arange(len(categorias))
barras = ax1.bar(
    x, porcentajes, 
    color="blue", 
    width=0.5, 
    label="Proporción"
)
ax1.set_ylabel("Proporción (%)", fontsize=12, color="blue")
ax1.set_ylim(0, 45)
ax1.tick_params(axis="y", labelcolor="blue")

# Dibujar un gráfico de línea para las tasas de crecimiento
ax2.plot(
    x, tazas_de_crecimiento, 
    color="orange", 
    marker="o", 
    label="Tasa de crecimiento"
)
ax2.set_ylabel("Tasa de crecimiento (%)", fontsize=12, color="orange")
ax2.set_ylim(-10, 4)
ax2.tick_params(axis="y", labelcolor="orange")

# Establecer las marcas y etiquetas del eje X
ax1.set_xticks(x)
ax1.set_xticklabels(categorias)

# Establecer el título
plt.title("Proporción de atención y tasa de crecimiento de la industria de servicios legales por nivel de ciudad en mayo", fontsize=14, y=1.02)

# Añadir etiquetas de datos de proporción al gráfico de barras (solo mantener las etiquetas de datos de barras)
for barra in barras:
    altura = barra.get_height()
    ax1.annotate(
        f'{altura}%',  # Mostrar el símbolo de porcentaje
        xy=(barra.get_x() + barra.get_width() / 2, altura),
        xytext=(0, 5),  # Desplazarse hacia arriba 5 puntos para evitar solapamiento con la parte superior de la barra
        textcoords="offset points",
        ha='center', va='bottom',
        fontsize=10,
        color='blue',  # Mismo color que el gráfico de barras para mejorar la relevancia
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", alpha=0.8)  # Caja de fondo blanco para una visualización destacada
    )

# Ajustar la posición de la leyenda a la parte inferior del gráfico
fig.legend(
    loc="lower center", 
    bbox_to_anchor=(0.5, -0.05),
    ncol=2, 
    frameon=False
)

# Optimizar el diseño
plt.subplots_adjust(bottom=0.2)
plt.tight_layout()

# Mostrar el gráfico
plt.show()