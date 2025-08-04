import matplotlib.pyplot as plt
import numpy as np

# Datos
años = ["2022.07", "2023.07", "2024.07"]
valores = [86.7, 89.4, 92.0]

# Inicializar el lienzo
fig, ax = plt.subplots(figsize=(6, 1.5))  # Lienzo estrecho para simular un diseño de línea de tiempo

# Dibujar una línea horizontal (línea de tiempo)
ax.axhline(y=0.5, color='#83B48A', linewidth=2, zorder=1)

# Dibujar cajas verdes con valores
for i, (año, val) in enumerate(zip(años, valores)):
    # Dibujar un rectángulo verde
    rect = plt.Rectangle((i - 0.2, 0.2), 0.4, 0.6,
                         facecolor='#C9EBD9', edgecolor='#83B48A',
                         linewidth=2, zorder=2)
    ax.add_patch(rect)
    # Etiquetar el valor
    ax.text(i, 0.5, f"{val}", fontsize=12,
            ha='center', va='center', color='#333333')
    # Etiquetar el año
    ax.text(i, -0.3, año, fontsize=10,
            ha='center', va='top', color='#666666')

# Ocultar los ejes
ax.set_xlim(-0.5, len(años)-0.5)
ax.set_ylim(-0.5, 1.2)
ax.axis('off')

# Agregar un título
plt.title("Índice de Confianza del Consumidor - Voluntad de Consumo", fontsize=14, fontweight='bold', y=1.3)

plt.tight_layout()
plt.show()