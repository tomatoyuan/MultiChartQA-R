# Importar bibliotecas necesarias
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Datos
años = np.array([2018, 2019, 2020, 2021, 2025])
escala_ventas = np.array([6531, 7562, 8848, 10458, 17218])

# Normalizar para el mapeo de colores
norm = mcolors.Normalize(vmin=min(escala_ventas), vmax=max(escala_ventas))
cmap = cm.get_cmap('BuGn')

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 5))

# Calcular tamaños de las burbujas (área): el área es proporcional al valor para evitar que sea demasiado grande
tamaño_burbujas = (escala_ventas / max(escala_ventas)) * 25000

# Dibujar un gráfico de burbujas
sc = ax.scatter(
    años, 
    [1]*len(años),  # Centrado verticalmente
    s=tamaño_burbujas,
    c=escala_ventas,
    cmap=cmap,
    alpha=0.8,
    edgecolors='white',
    linewidth=1.5
)

# Agregar anotaciones de texto (volumen de ventas)
for i, (x, y, val) in enumerate(zip(años, [1]*len(años), escala_ventas)):
    ax.text(x, y, f"{val}", ha="center", fontsize=10, fontweight="bold", color="#333")

# Agregar texto de anotación de CAGR
ax.annotate("CAGR 17% →", xy=(2018.2, 1.15), fontsize=10, color="#388e3c", weight="bold")
ax.annotate("→ CAGR 13.3%", xy=(2021.3, 1.15), fontsize=10, color="#1976d2", weight="bold")

# Embellir el eje x
ax.set_xticks(años)
ax.set_xticklabels(años, fontsize=11)
ax.set_xlim(2017.5, 2025.5)

# Ocultar el eje y
ax.set_yticks([])
ax.spines['left'].set_visible(False)

# Embellir el borde
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_alpha(0.2)

# Agregar un título
ax.set_title("Escala de ventas del mercado de circuitos integrados de China (100 millones de yuanes) de 2018 a 2025", fontsize=14, fontweight='bold', pad=20)

# Quitar las líneas de la cuadrícula, solo enfatizar burbujas + texto
ax.grid(False)

plt.tight_layout()
plt.show()