import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Datos
ciudades = ['Beijing', 'Shenzhen', 'Xi\'an', 'Wuhan', 'Shanghai', 'Chengdu', 'Changsha', 'Chongqing', 'Guangzhou', 'Dongguan']
hombres_solteros = [68, 75, 62, 58, 65, 57, 54, 51, 59, 53]  # Número de hombres solteros (en decenas de miles)
mujeres_solteras = [72, 68, 59, 56, 69, 61, 58, 53, 63, 50]  # Número de mujeres solteras (en decenas de miles)

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(14, 8), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Establecer parámetros del gráfico de barras
x = np.arange(len(ciudades))
ancho = 0.35
posiciones_barras_hombres = x - ancho/2
posiciones_barras_mujeres = x + ancho/2

# Definir color de gradiente
def gradient_color(color_base, alpha):
    """Generar un color de gradiente basado en el color base y la transparencia"""
    from matplotlib.colors import to_rgba
    return to_rgba(color_base, alpha)

# Dibujar gráfico de barras con gradiente
color_base_hombres = '#4361EE'
color_base_mujeres = '#3F37C9'

for i, (h, m) in enumerate(zip(hombres_solteros, mujeres_solteras)):
    # Gráfico de barras para hombres (con efecto de gradiente)
    ax.bar(posiciones_barras_hombres[i], h, ancho, 
           color=gradient_color(color_base_hombres, 0.9), 
           edgecolor='#2b49a0', linewidth=0.8)
    
    # Gráfico de barras para mujeres (con efecto de gradiente)
    ax.bar(posiciones_barras_mujeres[i], m, ancho, 
           color=gradient_color(color_base_mujeres, 0.9), 
           edgecolor='#282480', linewidth=0.8)

# Establecer título y etiquetas
ax.set_title('Las diez ciudades con mayor número de hombres y mujeres solteros en China', 
             fontsize=20, fontweight='bold', pad=20, color='#333333')
ax.set_xlabel('Ciudades', fontsize=16, labelpad=15, color='#555555')
ax.set_ylabel('Número de personas solteras (en decenas de miles)', fontsize=16, labelpad=15, color='#555555')

# Establecer marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(ciudades, rotation=30, ha='right', fontsize=14, color='#555555')

# Establecer rango y marcas del eje y
ax.set_ylim(0, max(max(hombres_solteros), max(mujeres_solteras)) * 1.1)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # Asegurarse de que las marcas del eje y sean enteros

# Agregar etiquetas de valor
def add_labels(posiciones, alturas, colores):
    for pos, altura, color in zip(posiciones, alturas, colores):
        ax.text(pos, altura + 1, f'{altura}', 
                ha='center', va='bottom', 
                fontsize=12, fontweight='bold', color=color)

add_labels(posiciones_barras_hombres, hombres_solteros, ['#2b49a0']*len(ciudades))
add_labels(posiciones_barras_mujeres, mujeres_solteras, ['#282480']*len(ciudades))

# Agregar líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7, color='#cccccc')

# Agregar leyenda
from matplotlib.patches import Patch
elementos_leyenda = [Patch(facecolor=color_base_hombres, edgecolor='#2b49a0', label='Hombres Solteros'),
                   Patch(facecolor=color_base_mujeres, edgecolor='#282480', label='Mujeres Solteras')]
ax.legend(handles=elementos_leyenda, loc='upper right', fontsize=14)

# Agregar línea de referencia horizontal
ax.axhline(y=60, color='#e0e0e0', linestyle='-', linewidth=1)

# Embellir el borde
for spine in ax.spines.values():
    spine.set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['bottom'].set_color('#cccccc')

# Agregar anotación de fuente de datos
ax.annotate('Fuente de datos: Datos ficticios (solo para ejemplo)',
            xy=(0.05, 0.01), xycoords='figure fraction',
            fontsize=10, color='#999999')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Guardar el gráfico (descomentar para guardar)
# plt.savefig('single_population_chart_beautiful.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())