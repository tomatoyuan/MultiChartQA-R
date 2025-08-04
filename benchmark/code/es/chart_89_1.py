import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
trimestres = ["2021T2", "2021T3", "2021T4", "2022T1"]
ventas = [64.3, 69.5, 91.2, 81.2]

# Ejes
x = np.arange(len(trimestres))

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de área con degradado
# Usar fill_between para crear el degradado inferior
ax.plot(x, ventas, color="#4CAF50", linewidth=2.5, marker='o', label="Ventas")
ax.fill_between(x, ventas, color="#C8E6C9", alpha=0.8)

# Agregar etiquetas de datos
for i, val in enumerate(ventas):
    ax.text(x[i], val + 1.5, f"{val}", ha='center', va='bottom', fontsize=10, fontweight='bold', color="#388E3C")

# Agregar una descripción de texto de las ventas totales
ventas_totales = sum(ventas)
ax.text(0.5, 0.9, f"Las ventas totales superaron los {ventas_totales:.0f} mil millones en los últimos 4 trimestres",
        transform=ax.transAxes, fontsize=12, color='#0288D1', ha='center', va='bottom', fontweight='bold')

# Configurar el eje x
ax.set_xticks(x)
ax.set_xticklabels(trimestres, fontsize=11)

# Ocultar las marcas de graduación del eje y y solo establecer el rango
ax.set_yticks([])
ax.set_ylim(0, max(ventas) + 15)

# Agregar un título
ax.set_title("Tendencia de las ventas de comercio electrónico de bebidas alcohólicas de grano de 2021T2 a 2022T1", fontsize=14, fontweight="bold", pad=15)

# Mejora visual: Quitar el marco
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# Líneas de cuadrícula (para mejorar la legibilidad)
ax.grid(axis='y', linestyle='--', alpha=0.2)

plt.tight_layout()
plt.show()