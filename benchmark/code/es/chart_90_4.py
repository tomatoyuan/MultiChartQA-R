import matplotlib.pyplot as plt
import numpy as np

# Puntos de venta de la cerveza
puntos_venta = [
    "Sabor intenso", "Jugo de malta de alta concentración", "Cerveza elaborada con proceso tradicional", 
    "Lista de ingredientes pura", "Ingredientes naturales", "Bajo contenido alcohólico, sin resaca", 
    "Bajo impacto, como bajo en calorías, bajo en grasa, bajo en azúcar", "Vida útil más corta, más fresca", 
    "Cerveza elaborada con proceso de alta tecnología", "Cuerpo de la bebida de alto valor"
]
# Proporción de cada punto de venta (%)
porcentajes = [32.0, 26.0, 24.4, 23.0, 22.9, 22.4, 19.6, 19.2, 18.4, 16.0]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de barras horizontales
y = np.arange(len(puntos_venta))
ancho_barra = 0.6
barras = ax.barh(y, porcentajes, height=ancho_barra, color="#C6AE39")

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(puntos_venta)
# Establecer la etiqueta del eje x
ax.set_xlabel("Puntos de venta de la cerveza por los que los consumidores están dispuestos a pagar un precio más alto (%)")
# Establecer el título
ax.set_title("Los 10 principales puntos de venta de la cerveza por los que los consumidores están dispuestos a pagar un precio más alto", fontsize=14, fontweight="bold")

# Emprolijar el gráfico, ocultar los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()