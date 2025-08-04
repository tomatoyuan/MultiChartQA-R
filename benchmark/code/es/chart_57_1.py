import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
años = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
proporciones = [10.5, 11.0, 6.4, 9.5, 9.1, 7.7, 7.7]  # Proporción del presupuesto de marketing (%)

# Configuración de colores (similar al verde de la imagen original)
color_linea = "#a5d6a7"
color_tendencia = "#dcdcdc"  # Color de la línea de tendencia

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))

# -------------------- Graficar el gráfico de línea --------------------
ax.plot(
    años, 
    proporciones, 
    color=color_linea, 
    marker="o", 
    linewidth=2, 
    markersize=5,
    label="Presupuesto de marketing promedio como porcentaje de los ingresos operativos"
)

# -------------------- Graficar la línea de tendencia (línea discontinua) --------------------
# Calcular la tendencia de ajuste lineal
z = np.polyfit(años, proporciones, 1)
p = np.poly1d(z)
ax.plot(años, p(años), color=color_tendencia, linestyle="--", linewidth=1)

# -------------------- Agregar anotaciones de datos --------------------
for i, val in enumerate(proporciones):
    ax.text(
        años[i], val + 0.2, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Agregar anotación inferior --------------------
ax.annotate(
    "El aumento de la incertidumbre macroeconómica conduce a una disminución de la proporción del presupuesto de marketing empresarial",
    xy=(0.5, -0.25),  # Posición de la anotación (centrada en la parte inferior)
    xycoords="axes fraction",
    ha="center",
    va="top",
    fontsize=12,
    color="#424242",
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8)
)

# -------------------- Embellir el gráfico --------------------
# Establecer etiquetas del eje x (años)
ax.set_xticks(años)
ax.set_xticklabels(años, fontsize=10, color="#424242")

# Establecer el rango del eje y (0 - 12%)
ax.set_ylim(0, 12)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar leyenda
ax.legend(
    loc="center right", 
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Agregar título
ax.set_title(
    "Presupuesto de marketing promedio como porcentaje de los \ningresos operativos de las empresas globales desde 2019 - 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()