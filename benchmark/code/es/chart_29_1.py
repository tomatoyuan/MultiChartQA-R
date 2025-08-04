import matplotlib.pyplot as plt
import numpy as np

# Datos de fechas
fechas = ["14 de", "15 de", "16 de", "17 de", "18 de", "19 de"]
# Datos de popularidad (unidad: diez mil)
valores_popularidad = [4698, 3708, 3131, 2204, 2325, 2892]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')

# Establecer el estilo de la cuadrícula
ax.grid(True, linestyle='--', alpha=0.7, color='#dddddd')

# Dibujar un gráfico de líneas con un color degradado
x = np.arange(len(fechas))
line, = ax.plot(x, valores_popularidad, marker='o', markersize=8, 
                color='#1e88e5', linewidth=3, alpha=0.8)

# Agregar etiquetas de datos
for i, (fecha, valor) in enumerate(zip(fechas, valores_popularidad)):
    ax.annotate(f'{valor}',
                xy=(i, valor),
                xytext=(0, 10),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1e88e5", alpha=0.8))

# Establecer las etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(fechas, fontsize=11)

# Establecer el rango y la etiqueta del eje y
ax.set_ylim(0, max(valores_popularidad) * 1.1)
ax.set_ylabel('Popularidad (diez mil)', fontsize=12, labelpad=10)

# Agregar un título
ax.set_title('Tendencia de popularidad de la Copa Mundial en la primera ronda de la fase de grupos', fontsize=16, pad=15, fontweight='bold')

# Agregar un color de fondo
ax.set_facecolor('#f8f9fa')

# Agregar flechas de tendencia
for i in range(len(x)-1):
    ax.annotate('',
                xy=(x[i+1], valores_popularidad[i+1]),
                xytext=(x[i], valores_popularidad[i]),
                arrowprops=dict(arrowstyle='->', color='#1e88e5', lw=1.5, alpha=0.6))

# Agregar una leyenda
ax.legend(['Tendencia de popularidad'], loc='upper right', frameon=True, framealpha=0.9)

# Agregar una nota al pie
plt.figtext(0.5, 0.01, 'Fuente de datos: Ejemplo ficticio', ha='center', fontsize=9, color='#666666')

# Optimizar el diseño
plt.tight_layout(pad=2)

# Guardar el gráfico (opcional)
# plt.savefig('tendencia_popularidad_copamundial.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()