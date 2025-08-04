import matplotlib.pyplot as plt
import numpy as np

# Datos de autonomía esperada
etiquetas_autonomia = ["150 - 250 km", "250 - 350 km", "350 - 500 km", "Más de 500 km"]
tamaños_autonomia = [7.1, 41.2, 29.5, 22.2]
colores_autonomia = ["#87CEFA", "#C0C0C0", "#4169E1", "#1E3A78"]

# Datos de rendimiento de seguridad esperado
etiquetas_seguridad = ["Medidas de protección del tren motriz", "Seguridad de los neumáticos", "Airbags", "Sistema de estacionamiento automático"]
tamaños_seguridad = [65.7, 59.7, 58.8, 56.5]
colores_seguridad = ["#87CEFA", "#6495ED", "#4682B4", "#1E3A78"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico circular de la autonomía esperada
porciones, textos, textos_automaticos = ax1.pie(tamaños_autonomia, colors=colores_autonomia, autopct='%1.1f%%', startangle=90)
ax1.set_title('Expectativas de los consumidores chinos sobre la autonomía de los vehículos eléctricos en 2023')
ax1.legend(porciones, etiquetas_autonomia, title="Rango de autonomía", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de la anotación
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white' if texto_automatico.get_position()[1] > 0.5 else 'black')

# Dibujar el gráfico de barras del rendimiento de seguridad esperado (simulado ya que hay datos de proporción única)
x = np.arange(len(etiquetas_seguridad))
ax2.bar(x, tamaños_seguridad, color=colores_seguridad, width=0.5)
ax2.set_title('Expectativas de los consumidores chinos sobre el rendimiento de seguridad de los vehículos eléctricos en 2023')
ax2.set_ylabel('Proporción esperada (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(etiquetas_seguridad, rotation=15, ha='right')
# Añadir anotaciones numéricas para el rendimiento de seguridad
for i, tamaño in enumerate(tamaños_seguridad):
    ax2.text(i, tamaño + 1, f'{tamaño}%', ha='center', va='bottom')
ax2.legend(etiquetas_seguridad, title="Elementos de rendimiento de seguridad", loc="center right")

plt.suptitle('Encuesta sobre las expectativas de los consumidores chinos sobre los vehículos eléctricos en 2023', fontsize=14)
plt.tight_layout()
plt.show()