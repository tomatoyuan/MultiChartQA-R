import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Datos
etiquetas = ['Post-05', 'Post-00', 'Post-95', 'Post-90', 'Post-85', 'Post-80', 'Antes de 80']
valores = [105, 73, 115, 115, 110, 80, 80]

# Configuración de colores: rosa claro -> rosa oscuro degradado
cmap = mcolors.LinearSegmentedColormap.from_list("gradiente_rosa", ["#fddde6", "#ec6fa8"])
colores = [cmap(i / (len(valores) - 1)) for i in range(len(valores))]

# Dibujo del gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(etiquetas, valores, color=colores)

# Línea auxiliar y anotaciones
ax.axhline(100, color='deeppink', linestyle='--', linewidth=1.5)
for barra, val in zip(barras, valores):
    va = 'bottom' if val >= 100 else 'top'
    ax.text(barra.get_x() + barra.get_width()/2, val + (2 if val >= 100 else -5), f'{val}',
            ha='center', va=va, fontsize=12, color='black')

# Título y descripción
ax.set_title('Encuesta de preocupación por la salud bucal de mujeres de diferentes generaciones', fontsize=14)
ax.set_ylabel('TGI')
ax.set_ylim(50, 130)
ax.text(-0.5, 110, 'Alta preocupación\nTGI>100', color='deeppink', fontsize=10)
ax.text(-0.5, 90, 'Baja preocupación\nTGI<100', color='deeppink', fontsize=10)

plt.tight_layout()
plt.show()