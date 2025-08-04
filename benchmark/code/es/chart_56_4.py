import matplotlib.pyplot as plt
import numpy as np

# Datos
factores = ["Calidad del producto", "Precio del producto", "Marca", "Imagen de la plataforma", "Reputación del presentador"]
porcentajes = [76.9, 64.1, 59.3, 42.5, 39.3]
colores = ["#a5d6a7"]  # Color verde uniforme, se puede ajustar según sea necesario

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 4))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(factores, porcentajes, color=colores*len(factores))

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height()/2,
            f'{ancho}%', ha='left', va='center', fontsize=9, fontweight='bold')

# Mejorar la configuración
ax.set_title("Factores que influyen en las decisiones de compra de los consumidores en el comercio electrónico de transmisión en vivo", fontsize=12, fontweight='bold')
ax.set_xlabel("Factores que influyen en las decisiones de compra (%)", fontsize=10)
ax.set_xticks(np.arange(0, max(porcentajes)+10, 10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(["Factores que influyen en las decisiones de compra (%)"], loc='lower right')

plt.tight_layout()
plt.show()