import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

# Datos
etiquetas = ["Sexo opuesto con relación no determinada", "Novia", "Esposa"]
valores = [1348, 621, 266]
total = sum(valores)
porcentajes = [f"{v/total*100:.1f}%" for v in valores]

# Establecer colores más cercanos a la imagen original
colores = ["#FF85A2", "#FFB3C1", "#FFD1DC"]  # Esquema de colores rosa suave
color_borde = "#FF4D6D"  # Color del borde

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras, agregar efectos de borde y sombra
rectangulos = ax.bar(
    etiquetas, valores, 
    color=colores, 
    edgecolor=color_borde, 
    linewidth=2, 
    width=0.6,
    alpha=0.9,
    zorder=3  # Asegurarse de que las barras se muestren por encima de la cuadrícula
)

# Agregar líneas de cuadrícula para que sea más claro
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)

# Agregar valores y porcentajes encima de las barras
for i, rectangulo in enumerate(rectangulos):
    altura = rectangulo.get_height()
    ax.text(
        rectangulo.get_x() + rectangulo.get_width()/2., altura + 10,
        f"{valores[i]}\n({porcentajes[i]})",
        ha='center', va='bottom',
        fontsize=12, fontweight='bold'
    )

# Establecer el título y las etiquetas de los ejes
ax.set_title("Proporción de objetos de regalos de hombres", fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel("Cantidad", fontsize=14, labelpad=10)

# Ajustar el rango del eje y para que el gráfico sea más bonito
ax.set_ylim(0, max(valores) * 1.1)

# Establecer las marcas de los ejes y los estilos
ax.tick_params(axis='both', which='major', labelsize=12)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# Agregar color de fondo
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#ffffff')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()