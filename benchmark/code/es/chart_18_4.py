import matplotlib.pyplot as plt
import numpy as np

# Datos
paises = ["Corea del Sur", "Japón", "EE. UU.", "Egipto"]
costos = [31, 41, (11 + 17) / 2, 44]  # Tomar el promedio del rango para EE. UU.

# Esquema de colores
colores = ['#638EC6', '#7BC67B', '#FFBC52', '#FF6F6F']

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales, agregar transparencia y bordes
barras = ax.barh(paises, costos, color=colores, alpha=0.8, edgecolor='black', linewidth=0.8)

# Agregar un título y etiquetas
ax.set_title("Comparación de los costos de matrimonio en el extranjero", fontsize=16, pad=15)
ax.set_xlabel("Costo de matrimonio (en RMB 10,000)", fontsize=12, labelpad=10)
ax.set_ylabel("País", fontsize=12, labelpad=10)

# Agregar etiquetas numéricas
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 0.5, barra.get_y() + barra.get_height()/2,
            f'{ancho:.1f}', ha='left', va='center', fontsize=10)

# Establecer el estilo del eje
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)

# Establecer el estilo de las marcas
ax.tick_params(axis='both', which='major', labelsize=10)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

# Agregar una cuadrícula de fondo
plt.grid(axis='x', linestyle='--', alpha=0.3)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()