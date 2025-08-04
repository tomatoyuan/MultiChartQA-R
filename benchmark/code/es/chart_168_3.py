import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# 数据
canales = ['Canal de comercio \n'
           'electrónico en línea',
           'Grandes superficies y \n'
           'supermercados tradicionales',
           'Compras grupales \n'
           'en la comunidad',
           'Tiendas de comestibles y\n'
           ' tiendas de conveniencia',
           'Tiendas de membresía \n'
           'de almacén',
           'Supermercados de alta gama']
valores = [80.5, 63.5, 39.9, 31.2, 20.8, 16.7]

# Degradado de colores (de marrón claro a marrón oscuro)
colores = plt.cm.PuBu(np.linspace(0.4, 0.9, len(canales)))

# Crear la figura
fig, ax = plt.subplots(figsize=(8, 6))
barras = ax.barh(canales, valores, color=colores)

# Establecer el área del borde, un poco más alejado de las barras
ax.add_patch(patches.Rectangle(
    (-5, -0.5),  # Desplazamiento a la izquierda
    100,          # Ancho que cubra el valor máximo + desplazamiento
    1,         # Altura ligeramente mayor que una sola línea
    linewidth=2,
    edgecolor='saddlebrown',
    facecolor='none',
    linestyle='dotted'
))

# Etiquetas de los valores
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height() / 2,
            f'{ancho:.1f}%', va='center', fontsize=10, color='black')

# Configuración de estilo
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel('Proporción (%)', fontsize=12)
ax.set_title('Distribución de canales de compra de papel higiénico por los consumidores', fontsize=14, pad=15)

# Fuente de los datos
plt.figtext(0.5, -0.05, 'Fuente de datos: Encuesta de tendencias de papel higiénico para\n'
                        ' consumidores chinos realizada por CBNData en marzo de 2024\n'
                        'Explicación de los datos: ¿Cuáles son los canales por los que compra papel higiénico? N = 1000',
            ha='center', fontsize=9)

plt.tight_layout()
plt.show()