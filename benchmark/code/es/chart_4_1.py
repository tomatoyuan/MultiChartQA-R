import matplotlib.pyplot as plt
import numpy as np

# Generar fechas completas de mayo (del 1 al 31)
fechas = [f"5/{i}" for i in range(1, 32)]
x = np.arange(len(fechas))  # Usado para la posición del eje x

# Datos de atención a la cirugía plástica (eje y izquierdo, unidad: millones)
cirugia_plastica = [
    6.5, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
    7.0, 7.0, 7.0, 7.0, 9.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0,
    7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0
]

# Datos de proporción de cirugía plástica nasal (eje y derecho, unidad: %)
cirugia_nasal = [
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0
]

# Datos de proporción de cirugía plástica ocular (eje y derecho, unidad: %)
cirugia_ocular = [
    5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0,
    5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0
]

# Datos de proporción de cuidado de la piel (eje y derecho, unidad: %)
cuidado_piel = [
    15.0, 15.0, 15.0, 15.0, 15.0, 14.0, 15.0, 15.0, 15.0, 15.0, 15.0,
    15.0, 15.0, 15.0, 15.0, 13.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0,
    15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 16.0
]

# Crear un lienzo y ejes dobles
fig, ax1 = plt.subplots(figsize=(14, 7))  # Aumentar el tamaño del lienzo
ax2 = ax1.twinx()

# Dibujar el gráfico de barras de cirugía plástica (eje izquierdo)
ancho_barra = 0.6
barras = ax1.bar(
    x,
    cirugia_plastica,
    color="#1f77b4",  # Azul profesional
    width=ancho_barra,
    label="Cirugía Plástica"
)
ax1.set_ylabel("Atención (Millones)", color="#1f77b4", fontsize=12, fontweight="bold")
ax1.set_ylim(0, 10)
ax1.set_yticks(np.arange(0, 11, 1))
ax1.tick_params(axis="y", labelcolor="#1f77b4", labelsize=10)

# Agregar etiquetas numéricas encima del gráfico de barras
for barra in barras:
    altura = barra.get_height()
    ax1.text(
        barra.get_x() + barra.get_width()/2., altura + 0.1,
        f'{altura:.1f}',
        ha='center', va='bottom', fontsize=9
    )

# Dibujar el gráfico de línea de cirugía plástica nasal (eje derecho)
ax2.plot(
    x,
    cirugia_nasal,
    color="#2ca02c",  # Verde profesional
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="Cirugía Plástica Nasal"
)

# Dibujar el gráfico de línea de cirugía plástica ocular (eje derecho)
ax2.plot(
    x,
    cirugia_ocular,
    color="#ff7f0e",  # Naranja profesional
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="Cirugía Plástica Ocular"
)

# Dibujar el gráfico de línea de cuidado de la piel (eje derecho)
ax2.plot(
    x,
    cuidado_piel,
    color="#d62728",  # Rojo profesional
    marker="o",
    markersize=5,
    linestyle="-",
    linewidth=2,
    label="Cuidado de la Piel"
)
ax2.set_ylabel("Proporción (%)", color="black", fontsize=12, fontweight="bold")
ax2.set_ylim(0, 18)
ax2.set_yticks(np.arange(0, 20, 2))
ax2.tick_params(axis="y", labelcolor="black", labelsize=10)

# Establecer las marcas de graduación del eje x (mostrar una marca cada 3 días para evitar la sobrecarga)
ax1.set_xticks(x[::3])  # Mostrar una marca cada 3 días
ax1.set_xticklabels(fechas[::3], fontsize=10, rotation=45, ha="right")  # Rotar 45 grados y alinear a la derecha

# Agregar una cuadrícula (solo en la dirección y del eje izquierdo)
ax1.grid(axis="y", linestyle="--", color="gray", alpha=0.4)

# Combinar las leyendas (colocarlas en la parte inferior)
lineas_ax1, etiquetas_ax1 = ax1.get_legend_handles_labels()
lineas_ax2, etiquetas_ax2 = ax2.get_legend_handles_labels()
ax1.legend(
    lineas_ax1 + lineas_ax2,
    etiquetas_ax1 + etiquetas_ax2,
    loc="lower center",
    ncol=4,
    bbox_to_anchor=(0.5, -0.2),
    frameon=False,
    fontsize=11
)

# Establecer el título
ax1.set_title("Tendencia de Atención de Búsqueda de la Industria de la Estética Médica en Mayo", fontsize=16, fontweight="bold", y=1.05)

# Agregar color de fondo para distinguir diferentes áreas
for i in range(0, len(fechas), 6):
    if i % 12 == 0:
        ax1.axvspan(i - 0.5, i + 5.5, alpha=0.05, color='gray')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()