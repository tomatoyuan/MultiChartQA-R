import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
from matplotlib.collections import PatchCollection
import numpy as np

# Datos
tamaños = [88.08, 11.69, 0.18, 0.05]
etiquetas = ["Proporción de Video", "Proporción de Imagen - Texto", "Proporción de Mini - Programa", "Proporción de Atlas"]

# Esquema de colores personalizado
colores = [
    ["#1976d2", "#e3f2fd"],  # Proporción de Video: Azul oscuro y azul claro
    ["#f57c00", "#ffebee"],  # Proporción de Imagen - Texto: Naranja y naranja claro
    ["#388e3c", "#e8f5e9"],  # Proporción de Mini - Programa: Verde y verde claro
    ["#7b1fa2", "#f3e5f5"]   # Proporción de Atlas: Morado y morado claro
]

# Crear un efecto 3D
fig = plt.figure(figsize=(20, 10))
fig.subplots_adjust(top=0.85, bottom=0.15, wspace=0.3)

# Crear 4 sub - gráficos
ejes = []
for i in range(4):
    ax = fig.add_subplot(1, 4, i + 1, aspect='equal')
    ejes.append(ax)

# Dibujar gráficos de pastel 3D
for i, ax in enumerate(ejes):
    # Establecer colores
    colores_grafico = [colores[i][0], colores[i][1]]

    # Calcular ángulos
    theta1 = 0
    theta2 = 360 * tamaños[i] / 100

    # Crear un efecto 3D - Dibujar sectores de múltiples capas
    for altura in [0, 0.1, 0.2]:
        if tamaños[i] < 5:  # Engrosar y resaltar valores pequeños
            factor_altura = 0.3
        else:
            factor_altura = 0.1

        # Sector principal
        sector = Wedge((0, 0), 1, theta1, theta2, width=0.2,
                      facecolor=colores_grafico[0], edgecolor='w', linewidth=1)
        ax.add_patch(sector)

        # Sector inferior (parte de color claro)
        sector_inferior = Wedge((0, 0), 1, theta2, 360, width=0.2,
                             facecolor=colores_grafico[1], edgecolor='w', linewidth=1)
        ax.add_patch(sector_inferior)

        # Agregar efecto de borde 3D
        if altura > 0:
            borde = Wedge((0, 0), 1, theta1, theta2, width=0.2,
                         facecolor=colores_grafico[0], alpha=0.3)
            ax.add_patch(borde)

    # Establecer el título
    ax.set_title(etiquetas[i], fontsize=18, pad=20)

    # Agregar etiquetas de porcentaje
    if tamaños[i] >= 0.01:  # Mostrar solo etiquetas mayores al 0.1%
        angulo = theta1 + (theta2 - theta1) / 2
        x = 0.6 * np.cos(np.deg2rad(angulo))
        y = 0.6 * np.sin(np.deg2rad(angulo))
        ax.text(x, y, f"{tamaños[i]:.2f}%",
                ha='center', va='center', fontsize=12)

    # Establecer el rango de coordenadas
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

# Establecer el título principal
fig.suptitle("Canales de atención de noticias de la industria de estética médica en mayo", fontsize=28, fontweight='bold', y=0.85)

plt.tight_layout()
plt.show()