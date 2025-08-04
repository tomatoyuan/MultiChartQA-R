import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -------------------- Definición de Datos --------------------
categorias = [
    "Promover el desarrollo cerebral",
    "Problemas de inmunidad",
    "Promover la digestión gastrointestinal",
    "Fortalecer los huesos/Promover el desarrollo óseo",
    "Problemas de crecimiento y desarrollo",
    "Promover el desarrollo visual"
]
porcentajes = [73.5, 72.3, 68.1, 64.5, 63.9, 53.6]

# -------------------- Mapeo de Colores: Esquema de Colores de Gradiente --------------------
# Usar mapa de colores (plasma/magma/turbo, etc.)
cmap = cm.get_cmap("plasma")
norm = mcolors.Normalize(vmin=min(porcentajes), vmax=max(porcentajes))
colores = [cmap(norm(p)) for p in porcentajes]

# -------------------- Crear el Canvas --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# -------------------- Dibujar un Gráfico de Barras Horizontales de "Estilo de Barra de Progreso" --------------------
y = np.arange(len(categorias))

barras = ax.barh(
    y, 
    porcentajes, 
    color=colores, 
    height=0.5,
    edgecolor="gray",
    linewidth=1.2
)

# Agregar texto de porcentaje
for i, (barra, valor) in enumerate(zip(barras, porcentajes)):
    ax.text(
        valor + 1, barra.get_y() + barra.get_height() / 2,
        f"{valor:.1f}%",
        va="center", ha="left",
        fontsize=10, fontweight="bold", color="#333333"
    )

# -------------------- Embellir el Gráfico --------------------
ax.set_yticks(y)
ax.set_yticklabels(categorias, fontsize=12, color="#333333")

# Ocultar las marcas del eje x
ax.set_xticks([])
# Remover bordes adicionales
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)

# Agregar título
ax.set_title("Preocupaciones de salud en el estadio infantil de 0 - 3 años (%)", fontsize=14, fontweight="bold", pad=20)

# Agregar espacio en blanco
plt.tight_layout()
plt.show()