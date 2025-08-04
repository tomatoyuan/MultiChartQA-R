import matplotlib.pyplot as plt
import numpy as np

# Data in Spanish
etiquetas = ['Necesidad básica', 'Dar gusto a sí mismo', 'Mostrar gusto/personalidad', 'Renovar',
             'Recomendación\nde otras personas', 'Probar por curiosidad', 'Regalar a familiares\ny amigos', 'Compra impulsiva']
valores = [55, 42, 36, 36, 30, 21, 15, 11]

# Prepare angles and close the loop
num_vars = len(etiquetas)
angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angulos += angulos[:1]
valores += valores[:1]

# Create radar plot
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Draw radar shape
ax.plot(angulos, valores, color='blue', linewidth=2)
ax.fill(angulos, valores, color='blue', alpha=0.25)

# Hide default labels
ax.set_xticks([])
ax.set_yticklabels([])

# Annotate with outer labels and connecting lines
label_radius = max(valores) + 10
for angulo, etiqueta, valor in zip(angulos[:-1], etiquetas, valores[:-1]):
    # Calculate coordinates for point and label
    x_end = angulo
    y_end = valor

    x_label = angulo
    y_label = label_radius

    # Draw connecting line from point to outer label
    ax.plot([x_end, x_label], [y_end, y_label], color='gray', linewidth=0.8, linestyle='--')

    # Determine alignment based on angle
    rotation = np.rad2deg(angulo)
    if np.pi/2 < angulo < 3*np.pi/2:
        ha = 'right'
    else:
        ha = 'left'

    # Text label (multi-line: label + value)
    ax.text(x_label, y_label, f"{etiqueta}\n{valor}%", ha=ha, va='center', fontsize=10)

# Title and data source
fig.text(0.5, 1.05, 'Demandas de los consumidores en la industria de electrodomésticos',
         ha='center', fontsize=16, fontweight='bold')
plt.figtext(0.1, 0.01, "Fuente de datos: Magic Mirror Insights", ha="left", fontsize=10)
plt.tight_layout()
plt.show()