import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import cm

# -------------------- Definición de Datos --------------------
plataformas = ["Douyin", "Bilibili", "WeChat", "Kuaishou", "Weibo", "Canales Internacionales", "Xiaohongshu", "Zhihu", "Otros"]
datos = [53.4, 48.6, 48.0, 24.9, 24.0, 19.5, 15.3, 11.3, 19.8]
x = np.arange(len(plataformas))

# -------------------- Configuración de Colores (Degradado Azul - Morado) --------------------
cmap = cm.get_cmap("cool")  # Degradado azul - morado
colores = [cmap(i / len(datos)) for i in range(len(datos))]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(9, 6))

# -------------------- Dibujar el gráfico de barras redondeado --------------------
altura_barra = 0.5
for i, (plataforma, valor) in enumerate(zip(plataformas, datos)):
    rect = patches.FancyBboxPatch(
        (0, i - altura_barra / 2),  # Punto de inicio (x, y)
        valor, altura_barra,        # Ancho, altura
        boxstyle="round,pad=0.1",
        linewidth=0,
        facecolor=colores[i],
        edgecolor="none",
        alpha=0.9
    )
    ax.add_patch(rect)

    # Agregar etiquetas de datos
    ax.text(valor + 1, i, f"{valor}%", va="center", ha="left",
            fontsize=10, fontweight="bold", color="#424242")

# -------------------- Embellir el gráfico --------------------
ax.set_xlim(0, max(datos) + 10)
ax.set_ylim(-0.5, len(plataformas) - 0.5)
ax.set_yticks(x)
ax.set_yticklabels(plataformas, fontsize=11, color="#333333")

ax.set_xticks([])
ax.set_xlabel("")  # No mostrar el eje x
ax.set_title("Plataformas preferidas por creadores chinos para la publicación de contenido", fontsize=14, fontweight="bold", pad=20)

# Ocultar el marco
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# Quitar las marcas de graduación
ax.tick_params(axis="both", which="both", length=0)

plt.tight_layout()
plt.show()