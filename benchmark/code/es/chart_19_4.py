import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ['Mujer', 'Hombre']
valores = [60, 40]
colores = ['#FF7B9C', '#7BC8F6']  # Rosa suave y azul

# Crear un gráfico
fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño del gráfico
ax.bar(etiquetas, valores, color=colores, edgecolor='black', linewidth=1.2, alpha=0.8)

# Agregar título y etiquetas
ax.set_title('Distribución de género de los consumidores "más arrepentidos"', fontsize=18, fontweight='bold', pad=20)
ax.set_ylabel('Porcentaje (%)', fontsize=14, labelpad=10)

# Establecer el rango y las marcas del eje y
ax.set_ylim(0, 100)
ax.set_yticks(np.arange(0, 101, 10))

# Agregar líneas de cuadrícula
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Embellir los ejes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Mostrar las etiquetas de los valores
for i, v in enumerate(valores):
    ax.text(i, v + 2, f'{v}%', ha='center', fontsize=14, fontweight='bold')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()