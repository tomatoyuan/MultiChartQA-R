import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Establece la fuente
plt.rcParams['font.sans-serif'] = ['Arial']
plt.rcParams['axes.unicode_minus'] = False

# Definición de datos
factores = [
    {"name": "Mejorar la conversión de usuarios y aumentar el rendimiento", "percent": 50.4},
    {"name": "Costo de construcción y operación del dominio privado", "percent": 48.8},
    {"name": "Lograr eficazmente la captación de tráfico del dominio público", "percent": 46.3},
    {"name": "Mejorar la fidelidad de los usuarios a la marca", "percent": 43.9},
    {"name": "Métodos de operación diversos", "percent": 39.8},
    {"name": "Acceso conveniente al dominio privado", "percent": 37.4},
    {"name": "Integración de canales online y offline", "percent": 29.3},
    {"name": "Los datos del dominio privado se pueden precipitar y analizar", "percent": 27.6},
]

# Preparar los datos del mapa de calor
nombres_factores = [f["name"] for f in factores][::-1]  # Invierte la dirección del eje y
valores_porcentaje = np.array([f["percent"] for f in factores])[::-1].reshape(-1, 1)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 7))

# Utiliza una paleta de colores cálidos personalizada
cmap = sns.light_palette("orangered", as_cmap=True)

# Dibujar un mapa de calor
sns.heatmap(
    valores_porcentaje,
    annot=True,
    fmt=".1f",
    cmap=cmap,
    cbar=False,
    yticklabels=nombres_factores,
    xticklabels=["Atención (%)"],
    linewidths=0.5,
    linecolor="white",
    annot_kws={"fontsize": 10, "weight": "bold", "color": "#4B1E00"},
    ax=ax
)

# Establece el título
ax.set_title("Factores de interés para la planificación y operación del dominio privado de marcas/comerciantes en 2022", fontsize=14, fontweight="bold", pad=20)

# Embellir los ejes
ax.tick_params(axis='y', labelsize=10)
ax.tick_params(axis='x', labelsize=10)
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()