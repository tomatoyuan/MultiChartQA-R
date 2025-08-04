import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2010, 2021)
# Valor total de equipos por encima de 10.000 yuanes (en diez miles de yuanes), los datos pueden ser aproximadamente iguales
values = [61623, 73154, 120292, 155770, 164474, 240805, 318904, 468174, 642335, 748276, 746559]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
bars = ax.bar(years, values, color='#A4C639', width=0.6)

# Agregar etiquetas de datos
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),
                textcoords='offset points',
                ha='center',
                va='bottom',
                color='#A4C639')

# Agregar una caja de texto explicativa
text_str = "El valor total de equipos por encima de 10.000 yuanes en hospitales de rehabilitación ha ido aumentando año tras año, \nlo que indica un desarrollo general positivo del mercado urbano de dispositivos médicos de rehabilitación."
bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="green", lw=1)
ax.text(0.09, 0.70, text_str, transform=ax.transAxes, fontsize=12,
        bbox=bbox_props, color='green')

# Configurar los ejes y el título
ax.set_xlabel('Año')
ax.set_ylabel('Valor total de equipos por encima de 10.000 yuanes (en diez miles de yuanes)')
ax.set_title('Valor total de equipos por encima de 10.000 yuanes en hospitales de rehabilitación chinos desde 2010 - 2020', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# Mejora visual: Ocultar los bordes superior y derecho
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()