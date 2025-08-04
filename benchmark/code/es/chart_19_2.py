import matplotlib.pyplot as plt
import numpy as np

# Datos
regiones = ["Guangdong", "Zhejiang", "Shandong", "Beijing", "Jiangsu", "Shanghai", "Hubei", "Henan", "Anhui", "Hunan", "Jiangxi", "Fujian"]
# Valores de cantidad simulados, ordenados en orden descendente
valores = [30, 28, 25, 24, 23, 22, 20, 12, 11, 10, 9, 8]

# Definir grupos de colores (rosa, naranja, azul claro), ordenados por tamaño numérico
colores = ["#f9cbda"] * 3 + ["#f7c253"] * 4 + ["#c7e3ed"] * 5

# Crear un lienzo y un objeto de eje
fig, ax = plt.subplots(figsize=(10, 8))

# Invertir el eje y para que los valores más grandes estén en la parte superior
ax.invert_yaxis()

# Dibujar un gráfico de barras horizontales
barras = ax.barh(regiones, valores, color=colores, edgecolor='none', alpha=0.85)

# Establecer el título y las etiquetas
ax.set_title("Distribución regional de consumidores con arrepentimientos de compra", fontsize=16, fontweight="bold", pad=20)
ax.set_xlabel("Número de consumidores", fontsize=12, labelpad=10)

# Establecer el tamaño de las etiquetas de las divisiones
ax.tick_params(axis='both', which='major', labelsize=11)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar etiquetas numéricas a cada barra
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 0.5, barra.get_y() + barra.get_height()/2,
            f'{ancho}', ha='left', va='center', fontsize=10)

# Agregar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()