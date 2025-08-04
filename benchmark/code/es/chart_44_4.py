import matplotlib.pyplot as plt
import numpy as np

# Categorías de snacks
categorias = ['Bebidas dulces', 'Botanas masticables', 'Alimentos fritos embutidos', 'Yogur', 'Productos de panadería', 'Frutos secos', 'Botanas picantes', 'Alimentos con alto contenido de azúcar', 'Frutas secas y frutas confitadas']
# Porcentajes de selección correspondientes
porcentajes = [55, 43, 43, 42, 42, 39, 38, 36, 33]

# Crear un lienzo y un subgráfico, ajustar el tamaño
fig, ax = plt.subplots(figsize=(12, 6))

# Establecer colores con degradado
cmap = plt.cm.get_cmap('viridis', len(categorias))
colores = [cmap(i) for i in range(len(categorias))]

# Dibujar un gráfico de barras, agregar transparencia y bordes
rects = ax.bar(categorias, porcentajes, color=colores, alpha=0.8, edgecolor='black', linewidth=0.8)

# Agregar un título y etiquetas de los ejes, establecer el tamaño de fuente
ax.set_title('Distribución de selección de snacks de los trabajadores con horas extras cuando tienen hambre en el trabajo', fontsize=16, pad=15)
ax.set_ylabel('Porcentaje de selección (%)', fontsize=14, labelpad=10)

# Establecer el rango del eje y
ax.set_ylim(0, max(porcentajes) * 1.1)

# Establecer líneas de cuadrícula
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Etiquetar los valores en las barras, ajustar la posición y el estilo
for rect in rects:
    altura = rect.get_height()
    ax.annotate(f'{altura}%',
                xy=(rect.get_x() + rect.get_width() / 2, altura),
                xytext=(0, 5),  # Desplazamiento vertical
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))

# Embellir el borde del gráfico
for spine in ax.spines.values():
    spine.set_linewidth(0.5)

# Rotar las etiquetas del eje x para que sean más legibles
plt.xticks(rotation=30, ha='right', fontsize=11)

# Ajustar el diseño
plt.tight_layout()

plt.show()