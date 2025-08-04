import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

# Datos
grupos = ["Gourmet", "Ama de casa", "Entusiasta de la tecnología", "Amante de la música", "Viajero de mochila", 
          "Fanático militar", "Decorador de interiores", "Fanático de los deportes", "Familia financiera", "Jugador"]
valores = [1.2359, 1.1635, 1.0763, 1.0363, 1.0128, 
          1.0078, 0.9645, 0.8671, 0.7860, 0.5915]

# Mapeo de símbolos (marcadores incorporados en matplotlib)
marcadores = ['o', 's', '^', 'D', 'p', '*', 'h', 'v', 'X', 'P']
tamaños_marcadores = [100, 80, 90, 70, 85, 95, 80, 90, 75, 85]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 8), facecolor="#f0f8ff")
ax.set_facecolor("#f0f8ff")

# Dibujar un gráfico de barras (utilizando colores degradados)
cmap = plt.cm.get_cmap('Blues', 12)
for i, (valor, grupo) in enumerate(zip(valores, grupos)):
    indice_color = int(valor * 5) if valor > 1 else int(valor * 5) + 2
    color = cmap(indice_color)
    
    ax.barh(i, valor, height=0.6, color=color, edgecolor='white', alpha=0.85)
    ax.text(valor + 0.02, i, f"{valor:.4f}", 
            ha="left", va="center", color='navy', fontsize=10, fontweight='bold')

# Establecer el título
ax.set_title("Distribución de interés de la opinión pública sobre tormentas de lluvia (Diferenciación)", 
             fontdict={"fontsize":20, "fontweight":"bold", "color":"navy"},
             pad=20)
ax.text(0, 1.02, "Qué grupos se preocupan más por las tormentas de lluvia", 
        transform=ax.transAxes, fontsize=14, color='navy')

# Agregar símbolos y etiquetas de categoría
for i, (grupo, marcador, tamaño) in enumerate(zip(grupos, marcadores, tamaños_marcadores)):
    indice_color = int(valores[i] * 5) if valores[i] > 1 else int(valores[i] * 5) + 2
    color = cmap(indice_color)
    
    ax.scatter(-0.05, i, marker=marcador, s=tamaño, color=color, edgecolor='white', zorder=3)
    ax.text(0.01, i, grupo, fontsize=12, ha="left", va="center", 
            color='navy', fontweight='bold')

# Agregar una línea de referencia (Diferenciación = 1)
ax.axvline(x=1, color='navy', linestyle='--', alpha=0.5, linewidth=1.5)
ax.text(1.01, -0.8, "Diferenciación = 1", fontsize=10, color='navy', alpha=0.8)

# Ocultar los ejes
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Establecer el rango del eje x
ax.set_xlim(-0.1, 1.5)
ax.set_ylim(-1, 10)

# Agregar una leyenda (moverla hacia abajo)
elementos_leyenda = [
    Line2D([0], [0], color=cmap(8), lw=10, label='Diferenciación > 1: Más preocupados'),
    Line2D([0], [0], color='navy', linestyle='--', lw=1.5, label='Diferenciación = 1: Nivel promedio'),
    Line2D([0], [0], color=cmap(3), lw=10, label='Diferenciación < 1: Menos preocupados')
]
ax.legend(handles=elementos_leyenda, 
          loc='lower right',  # Posicionarla en la esquina inferior derecha
          bbox_to_anchor=(1, -0.1),  # Moverla hacia abajo un 10% de la altura
          frameon=False, 
          fontsize=10, 
          labelcolor='navy')

# Agregar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.3, color='lightblue')

plt.tight_layout()
plt.show()