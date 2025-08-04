import matplotlib.pyplot as plt
import numpy as np

# Años
years = [2022, 2023, 2024]
# Participación del canal en línea
online_shares = [41, 41, 43]
# Participación del canal fuera de línea (calculada como 100 - participación del canal en línea, ya que el total es 100%)
offline_shares = [100 - x for x in online_shares]

x = np.arange(len(years))  # Posiciones del eje x para el gráfico de barras
width = 0.35  # Ancho de cada barra

fig, ax = plt.subplots(figsize=(10, 6))  # Ajustar el tamaño de la figura para un mejor diseño
# Dibujar las barras del canal fuera de línea
rects_offline = ax.bar(x - width/2, offline_shares, width, label='Canal Fuera de Línea', color='#D9C8B1')
# Dibujar las barras del canal en línea
rects_online = ax.bar(x + width/2, online_shares, width, label='Canal en Línea', color='#F7C8AA')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(years)
# Establecer la etiqueta del eje y
ax.set_ylabel('Participación (%)')
# Establecer el título
ax.set_title('Comparación de la Participación de los Canales en Línea y Fuera de Línea de Productos de Cuidado de la Piel de 2022 - 2024')

# Ajustar el límite del eje y para crear espacio para la leyenda
ax.set_ylim(0, 110)  # Aumentar el límite superior al 110%

# Etiquetar los valores en las barras
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Desplazamiento de la posición de la etiqueta del valor
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects_offline)
autolabel(rects_online)

# Colocar la leyenda fuera del gráfico para evitar superposiciones
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),  # Posicionar la leyenda debajo del gráfico
          fancybox=True, shadow=True, ncol=2)  # Usar 2 columnas para una mejor apariencia

plt.tight_layout()  # Ajustar el diseño para asegurar que todo quepa
plt.show()