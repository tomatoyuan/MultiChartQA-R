import matplotlib.pyplot as plt
import numpy as np

# Datos
expectativas = [
    "Efectos del producto de larga duración", "Productos con eficacia compuesta", "Mayores promociones/descuentos",
    "Diseño de embalaje más bonito y creativo", "Productos asequibles", "Más nuevas marcas domésticas",
    "Más canales de compra para una compra conveniente", "Mejor actitud de servicio de los guías de compra/vendedores", "Mejor servicio postventa"
]
porcentajes = [61.1, 41.2, 40.9, 39.6, 31.0, 29.5, 28.7, 17.0, 10.4]

x = np.arange(len(expectativas))

fig, ax = plt.subplots(figsize=(10, 7))

# Dibujar un gráfico de barras
barras = ax.barh(x, porcentajes, color='orange')  # Un gráfico de barras horizontales es más adecuado para mostrar este tipo de datos
ax.set_xlabel('Proporción esperada (%)')
ax.set_ylabel('Contenido esperado')
ax.set_yticks(x)
ax.set_yticklabels(expectativas)
ax.invert_yaxis()  # Mostrar la primera expectativa en la parte superior
ax.set_title('Encuesta sobre las expectativas de los consumidores chinos para el desarrollo de la industria cosmética en 2023')

# Agregar etiquetas numéricas
for barra in barras:
    longitud = barra.get_width()
    ax.text(longitud + 1, barra.get_y() + barra.get_height() / 2,
            f'{longitud}%', ha='left', va='center')

plt.tight_layout()
plt.show()