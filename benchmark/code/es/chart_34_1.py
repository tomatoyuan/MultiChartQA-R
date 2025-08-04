import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

# Datos de años
años = np.arange(2015, 2027)
# Datos de tamaño del mercado simulados (en miles de millones de dólares estadounidenses, la tendencia general es similar y los valores se pueden ajustar)
tamaño_mercado = [29.4, 28, 30, 32, 31, 38, 39, 41, 43, 45, 47, 49.2]
# Etiquetas de años, manejar 2025E, 2026E
etiquetas_años = [str(año) if año < 2025 else f"{año}E" for año in años]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras
barras = ax.bar(años, tamaño_mercado, color='#667799', width=0.8)

# Etiquetar los valores en las barras
for barra, valor in zip(barras, tamaño_mercado):
    ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height(), f'{valor}',
            ha='center', va='bottom')

# Etiquetar la CAGR
ax.text(2022, 50, f'CAGR*: 4.04%', ha='left')

# Dibujar una flecha inclinada hacia arriba a un ángulo de 30 grados
x_inicio = 2023
y_inicio = 48
# Calcular las coordenadas finales del ángulo de 30 grados (dx = 3, dy = 3 * tan(30°))
angulo_rad = np.radians(60)
dx = 3
dy = dx * np.tan(angulo_rad)
x_fin = x_inicio + dx
y_fin = y_inicio + dy

# Usar FancyArrowPatch para dibujar una flecha inclinada de 30 grados
flecha = FancyArrowPatch((x_inicio, y_inicio), (x_fin, y_fin), 
                        arrowstyle='->', 
                        connectionstyle='arc3,rad=0', 
                        color='black', 
                        mutation_scale=15)
ax.add_patch(flecha)

# Establecer las marcas del eje x
ax.set_xticks(años)
ax.set_xticklabels(etiquetas_años)

# Establecer el rango del eje y
ax.set_ylim(0, 60)

# Establecer el título del gráfico
ax.set_title('Tamaño del mercado de ropa interior en China desde 2015 hasta 2026 (Miles de millones de dólares estadounidenses)')

# Mostrar el gráfico
plt.show()