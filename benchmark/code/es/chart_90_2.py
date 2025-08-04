import matplotlib.pyplot as plt
import numpy as np

# Trimestres
trimestres = ["2021T2", "2021T3", "2021T4", "2022T1"]
ventas = np.array([7.0, 5.0, 4.2, 10.9])

# Tamaño de las burbujas (área) se magnifica en función de las ventas para una mejor visualización
tamanos = ventas * 1000  

# Colores de las burbujas, colores en gradiente
colores = ['#a8d5a2', '#82c97b', '#5eb852', '#3f9137']

fig, ax = plt.subplots(figsize=(7, 5))

# Valores del eje x para las posiciones del diagrama de dispersión
x = np.arange(len(trimestres))

# Dibujar el diagrama de burbujas
dispersión = ax.scatter(x, ventas, s=tamanos, c=colores, alpha=0.7, edgecolors='white', linewidth=1.5)

# Añadir etiquetas de datos
for i, val in enumerate(ventas):
    ax.text(x[i], val + 0.3, f'{val} mil millones', ha='center', fontsize=10, fontweight='bold', color='#2e2e2e')

# Establecer el eje x
ax.set_xticks(x)
ax.set_xticklabels(trimestres, fontsize=11, color="#424242")

# Ocultar las marcas del eje y
ax.set_yticks([])

# Añadir texto para indicar las ventas totales
ventas_totales = ventas.sum()
ax.text(0.5, 0.9, f"Ventas totales en los últimos 4 trimestres: {ventas_totales:.1f} mil millones",
        transform=ax.transAxes, fontsize=12, color='#388e3c', ha='center', va='bottom', fontweight='bold')

# Título
ax.set_title("Diagrama de Burbujas de Ventas de Cerveza en Comercio Electrónico desde 2021T2 hasta 2022T1", fontsize=14, fontweight='bold')

# Embellir: Ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

# plt.tight_layout()
plt.show()