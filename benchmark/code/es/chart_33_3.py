import matplotlib.pyplot as plt
import numpy as np

# Años
years = np.arange(2019, 2029)
# Participación del mercado online (datos de muestra, siguiendo la tendencia original)
online_share = [16, 20, 31, 33, 35, 36, 37, 47, 55, 60]
# Participación del mercado offline = 100 - online (simulación simplificada para asegurar la lógica total)
offline_share = [100 - x for x in online_share]

# Ancho de la barra
bar_width = 0.6

# Crear un lienzo
fig, ax = plt.subplots()

# Dibujar la participación offline (gris, correspondiente a la capa inferior del gráfico original)
offline_bars = ax.bar(years, offline_share, width=bar_width, color='#D3D3D3', label='Offline')
# Dibujar la participación online (azul, correspondiente a la capa superior del gráfico original)
online_bars = ax.bar(years, online_share, width=bar_width, bottom=offline_share, color='#4682B4', label='Online')

# Establecer las marcas del eje x
ax.set_xticks(years)
# Establecer la etiqueta del eje y
ax.set_ylabel('Participación del mercado (%)')
# Establecer el título
ax.set_title('Distribución de la participación del mercado de canales online y offline para productos de limpieza y cuidado del hogar de 2019 a 2028')
# Añadir una leyenda
ax.legend()

# Añadir etiquetas de datos para las barras offline
for bar, share in zip(offline_bars, offline_share):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height/2,
            f'{share}%', ha='center', va='center', color='black')

# Añadir etiquetas de datos para las barras online
for bar, share, base in zip(online_bars, online_share, offline_share):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., base + height/2,
            f'{share}%', ha='center', va='center', color='white')

# Mostrar el gráfico
plt.show()