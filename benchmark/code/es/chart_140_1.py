import matplotlib.pyplot as plt
import numpy as np

# Datos de la situación de compra
etiquetas_compra = ["Comprado", "No comprado, planea comprar", "No comprado, no planea comprar", "Todavía observando"]
tamaños_compra = [51.8, 11.8, 2.9, 33.5]
colores_compra = ["#4169E1", "#00CED1", "#FF6347", "#9370DB"]

# Datos del rango de precios de compra
etiquetas_precio = ["Por debajo de 100,000", "100,000 - 200,000", "210,000 - 400,000", "410,000 - 600,000", "610,000 - 800,000", "Por encima de 800,000"]
tamaños_precio = [8.7, 38.7, 37.1, 8.9, 3.9, 2.7]
colores_precio = ["#90EE90", "#1E90FF", "#FFD700", "#32CD32", "#4B0082", "#8B4513"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico de clasificación de la situación de compra (simular la visualización de clasificación con un gráfico circular porque son datos de proporción única)
porciones1, textos1, textos_auto1 = ax1.pie(tamaños_compra, colors=colores_compra, autopct='%1.1f%%', startangle=90)
ax1.set_title('Situación de compra')
ax1.legend(porciones1, etiquetas_compra, title="Estado de compra", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de la anotación
for texto_auto in textos_auto1:
    texto_auto.set_color('white' if texto_auto.get_position()[1] > 0.5 else 'black')

# Dibujar el gráfico circular del rango de precios de compra
porciones2, textos2, textos_auto2 = ax2.pie(tamaños_precio, colors=colores_precio, autopct='%1.1f%%', startangle=90)
ax2.set_title('Rango de precios de compra')
ax2.legend(porciones2, etiquetas_precio, title="Rango de precios", loc="center left", bbox_to_anchor=(1, 0.5))
for texto_auto in textos_auto2:
    texto_auto.set_color('white' if texto_auto.get_position()[1] > 0.5 else 'black')

plt.suptitle('Encuesta de 2023 sobre la situación de compra y el rango de precios de compra de vehículos de energía nueva en China', fontsize=14)
plt.tight_layout()
plt.show()