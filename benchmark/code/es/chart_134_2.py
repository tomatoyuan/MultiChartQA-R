import matplotlib.pyplot as plt
import numpy as np

# Izquierda: Datos de frecuencia de uso
etiquetas_freq = ["Usado a menudo", "Diariamente", "Ocasionalmente", "Usado raramente"]
tamaños_freq = [62.3, 23.4, 12.6, 1.7]
colores_freq = ["#FF7F24", "#FFD700", "#90EE90", "#FFC0CB"]

# Derecha: Datos de aceptación de precio
etiquetas_precio = ["50 yuan - 99 yuan", "100 yuan - 149 yuan", "150 yuan y más", "Por debajo de 50 yuan"]
tamaños_precio = [46.1, 41.2, 7.0, 5.7]
colores_precio = ["#FF7F24", "#FFD700", "#90EE90", "#8B4513"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico circular izquierdo para la frecuencia de uso
wedges, textos, autotextos = ax1.pie(tamaños_freq, colors=colores_freq, autopct='%1.1f%%', startangle=90)
ax1.set_title('Frecuencia de uso de cosméticos \nprotectores solares por los consumidores chinos')
# Ajustar la posición de la leyenda para que las etiquetas sean más claras
ax1.legend(wedges, etiquetas_freq, title="Frecuencia de uso", loc="center left", bbox_to_anchor=(1, 0.5))

# Dibujar el gráfico circular derecho para la aceptación de precio (con efecto 3D, similar a la imagen original)
wedges2, textos2, autotextos2 = ax2.pie(tamaños_precio, colors=colores_precio, autopct='%1.1f%%', startangle=90,
                                      explode=[0, 0, 0, 0.1], shadow=True)
ax2.set_title('Aceptación de precio de los consumidores chinos para los \ncosméticos protectores solares (tomando una botella de 60g como ejemplo)')
ax2.legend(wedges2, etiquetas_precio, title="Rango de precios", loc="center left", bbox_to_anchor=(1, 0.5))

# Optimizar el color del texto de las etiquetas automáticas (distinguir entre sectores oscuros/claros)
for autotexto in autotextos + autotextos2:
    autotexto.set_color('white' if autotexto.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()