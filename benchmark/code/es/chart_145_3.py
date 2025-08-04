import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
elementos = [
    "Elementos tradicionales chinos y estilo de moda nacional", "Elementos del zodíaco", "Innovación y creatividad",
    "Minimalismo", "Elementos tecnológicos", "Tendencias de influencers en Internet", "Cómics y animación", "Otros"
]
porcentajes = [62.2, 41.6, 38.7, 37.4, 28.9, 23.8, 19.8, 0.3]

# Calcular el número de cuadrados correspondientes a cada elemento
conteos_cuadros = [int(p / 3) + (1 if p % 3 > 1.5 else 0) for p in porcentajes]

# Aumentar el ancho del gráfico para adaptarse al texto desplazado a la derecha
fig, ax = plt.subplots(figsize=(14, 6))  # El ancho se aumenta de 10 a 14
ax.set_xlim(0, max(conteos_cuadros) + 15)  # Aumentar el rango del eje x para dejar espacio al texto desplazado
ax.set_ylim(0, len(elementos) * 1.5)
ax.set_axis_off()  # Ocultar los ejes

# Dibujar cuadrados naranjas y anotaciones con texto desplazado a la derecha
for i, (elemento, perc, cuadros) in enumerate(zip(elementos, porcentajes, conteos_cuadros)):
    # Dibujar cuadrados
    for j in range(cuadros):
        ax.add_patch(plt.Rectangle((j + 1, i * 1.5 + 0.3), 0.8, 0.8, color='orange'))

    # Desplazamiento del texto: ajustar la coordenada x de cuadros + 2 a cuadros + 5
    # Dibujar el nombre del elemento
    ax.text(cuadros + 5, i * 1.5 + 0.7, elemento, fontsize=12, va='center')
    # Dibujar el valor del porcentaje (desplazarlo aún más a la derecha para evitar solapamiento con el nombre del elemento)
    ax.text(cuadros + 5 + len(elemento) * 0.3, i * 1.5 + 0.7, f'{perc}%', ha='left', va='center', fontsize=12, color='orange')

ax.set_title('Preferencias de los consumidores por los elementos de los regalos de la Fiesta de Año Nuevo Chino en 2023', fontsize=14, y=1.05)
plt.tight_layout()
plt.show()