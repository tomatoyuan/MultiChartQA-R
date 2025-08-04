import matplotlib.pyplot as plt
import numpy as np

# Escenarios de consumo
escenarios = ["Reunión de amigos", "Reunión familiar", "Entretenimiento empresarial", "Beber solo", "Cita de pareja"]
# Proporción de 18 - 29 años (%)
edad18_29 = [39.2, 21.1, 22.5, 13.2, 3.9]
# Proporción de 30 años y mayores (%)
edad30_mas = [43.7, 28.4, 15.7, 10.1, 2.2]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(7, 6))

# Dibujar un gráfico de barras horizontales para 18 - 29 años (verde)
y = np.arange(len(escenarios))
ancho_barra = 0.35
barras1 = ax.barh(y + ancho_barra/2, edad18_29, height=ancho_barra, color="#A4C639", label="Edad 18 - 29 (%)")
# Dibujar un gráfico de barras horizontales para 30 años y mayores (azul)
barras2 = ax.barh(y - ancho_barra/2, edad30_mas, height=ancho_barra, color="#87CEEB", label="Edad 30 y mayores (%)")

# Agregar etiquetas de datos para 18 - 29 años
for barra in barras1:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Agregar etiquetas de datos para 30 años y mayores
for barra in barras2:
    ancho = barra.get_width()
    ax.annotate(f'{ancho}%',
                xy=(ancho, barra.get_y() + barra.get_height() / 2),
                xytext=(5, 0),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='left', va='center')

# Dibujar cajas discontinuas amarillas para Entretenimiento empresarial y Beber solo
# Encontrar los índices de Entretenimiento empresarial y Beber solo
indice_inicio = escenarios.index("Entretenimiento empresarial")
indice_fin = escenarios.index("Beber solo")
# Calcular las coordenadas de la caja
y_min = y[indice_inicio] - ancho_barra/2 - 0.1
y_max = y[indice_fin] + ancho_barra/2 + 0.1
x_min = 0
x_max = max(max(edad18_29), max(edad30_mas)) + 5  # Ampliar el rango del eje x adecuadamente

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(escenarios)
# Establecer la etiqueta del eje x
ax.set_xlabel("Proporción (%)")
# Establecer el título
ax.set_title("Escenarios de consumo de licor (por edad)", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embellir el gráfico, ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()