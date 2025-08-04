import matplotlib.pyplot as plt

# Datos de frecuencia de uso
etiquetas_frecuencia = ["Casi nunca se utiliza", "Se utiliza ocasionalmente", "Se utiliza cuando es necesario", "Se utiliza con frecuencia"]
tamaños_frecuencia = [10.0, 45.5, 33.7, 10.8]
colores_frecuencia = ["#FF9933", "#FF5733", "#FFD700", "#FFC300"]

# Datos de experiencia
etiquetas_experiencia = ["Mejoró la experiencia de compra", "Tuvo poco impacto en la experiencia de compra", "Empeoró la experiencia de compra", "No estoy seguro", "Otro (por favor especifique)"]
tamaños_experiencia = [33.3, 37.4, 25.2, 3.9, 0.2]
colores_experiencia = ["#FFB6C1", "#FF8C69", "#FFDAB9", "#D8BFD8", "#C0C0C0"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Dibujar el gráfico circular de frecuencia de uso
wedges, texts, autotexts = ax1.pie(tamaños_frecuencia, colors=colores_frecuencia, autopct='%1.1f%%', startangle=90)
ax1.set_title('Frecuencia de uso')
# Ajustar la leyenda y colocarla en el lado derecho del gráfico circular
ax1.legend(wedges, etiquetas_frecuencia, title="Categorías de frecuencia de uso", loc="center left", bbox_to_anchor=(1, 0.5))
# Hacer que el color del texto de la anotación sea más claro (distinguir entre sectores oscuros/claros)
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# Dibujar el gráfico circular de experiencia
wedges2, texts2, autotexts2 = ax2.pie(tamaños_experiencia, colors=colores_experiencia, autopct='%1.1f%%', startangle=90)
ax2.set_title('Experiencia')
ax2.legend(wedges2, etiquetas_experiencia, title="Categorías de experiencia", loc="center left", bbox_to_anchor=(1, 0.5))
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.suptitle('Frecuencia de uso y experiencia de los consumidores chinos con las \ncaracterísticas de intervención manual en comercio electrónico basado en IA en 2024', fontsize=14)
plt.tight_layout()
plt.show()