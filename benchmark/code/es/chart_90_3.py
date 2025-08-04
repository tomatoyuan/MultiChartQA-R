import matplotlib.pyplot as plt
import numpy as np

# Factores de consideración de compra
factores = [
    "Sabor", "Concentración de mosto", "Evaluación de boca en boca", "Contenido de alcohol", "Ingredientes de elaboración",
    "Aroma/Color", "Conocimiento de la marca", "Proceso de elaboración", "Relación calidad - precio", "Riqueza de la espuma",
    "Nuevos sabores/nuevas sensaciones", "Conveniencia de compra", "Vida útil", "Apariencia de la botella/empaque",
    "Anunciantes, etc.", "Productos de edición limitada/co - branding", "Recomendaciones de KOL"
]
# Porcentaje de cada factor (%)
porcentajes = [
    38.4, 31.3, 29.4, 28.1, 27.3,
    27.0, 26.5, 25.8, 24.8, 22.7,
    20.5, 20.0, 17.9, 16.5,
    12.3, 11.4, 11.1
]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(12, 6))

# Dibujar un gráfico de barras
x = np.arange(len(factores))
ancho_barra = 0.6
barras = ax.bar(x, porcentajes, width=ancho_barra, color="#A4C639")

# Agregar bordes azules a "Sabor" y "Concentración de mosto"
for i in range(2):
    barras[i].set_edgecolor('blue')
    barras[i].set_linewidth(2)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas para una mejor visualización
ax.set_xticks(x)
ax.set_xticklabels(factores, rotation=45, ha='right')
# Establecer la etiqueta del eje y
ax.set_ylabel("Porcentaje (%)")
# Establecer el título
ax.set_title("Factores de consideración de compra de cerveza", fontsize=14, fontweight="bold")

# Emprolijar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()