import matplotlib.pyplot as plt
import numpy as np

# --------------------- Datos del gráfico circular izquierdo ---------------------
etiquetas_pastel = ["Comer en el restaurante", "Entrega de comida en línea", "Comprar fuera y llevar a casa", "Proporción similar de online y offline"]
tamaños_pastel = [32.5, 23.3, 23.5, 20.7]
colores_pastel = ["#FFD700", "#FF7F50", "#32CD32", "#8B4513"]

# --------------------- Datos del gráfico de barras agrupadas derecho ---------------------
categorias_barras = ["Menos del 30% (excluyendo el 30%)", "30 - 40% (excluyendo el 40%)", "40 - 50% (excluyendo el 50%)", "50 - 80% (excluyendo el 80%)", "80 - 100%"]
valores_barras = [
    [32.2, 67.8],  # Primer grupo: Parte naranja, Parte de color claro
    [43.8, 56.2],
    [19.3, 80.7],
    [3.4, 96.6],
    [1.3, 98.7]
]
colores_barras = ["#FF7F50", "#FAF0E6"]  # Naranja, Beige claro

# Crear un lienzo con un diseño de 1 fila y 2 columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Dibujar el gráfico circular izquierdo ---------------------
porciones, textos, textos_automaticos = ax1.pie(tamaños_pastel, colors=colores_pastel, autopct='%1.1f%%', startangle=90)
ax1.set_title('Distribución de los tipos de proporción de consumo de catering nocturno entre los residentes chinos en 2023')
# Ajustar la leyenda
ax1.legend(porciones, etiquetas_pastel, title="Tipo de consumo", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de anotación
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white' if texto_automatico.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el gráfico de barras agrupadas derecho ---------------------
x = np.arange(len(categorias_barras))
base = np.zeros(len(categorias_barras))
for i in range(2):
    ax2.bar(x, [val[i] for val in valores_barras], bottom=base, color=colores_barras[i], label=etiquetas_pastel[i] if i == 0 else '')
    base += [val[i] for val in valores_barras]

ax2.set_title('Distribución de la proporción de consumo de catering nocturno en el día completo entre los residentes chinos en 2023')
ax2.set_ylabel('Proporción (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(categorias_barras, rotation=45, ha='right')
ax2.legend(title="Tipo de consumo", loc="upper left")

# Añadir anotaciones numéricas al gráfico de barras agrupadas
for i, (val1, val2) in enumerate(valores_barras):
    ax2.text(i, val1 / 2, f'{val1}%', ha='center', va='center', color='white')
    ax2.text(i, val1 + val2 / 2, f'{val2}%', ha='center', va='center', color='black')

# Simular cajas discontinuas amarillas (primeros dos grupos)
ax2.plot([x[0] - 0.3, x[0] + 0.3, x[0] + 0.3, x[0] - 0.3, x[0] - 0.3],
         [0, 0, 100, 100, 0],
         linestyle='--', color='gold', linewidth=2)
ax2.plot([x[1] - 0.3, x[1] + 0.3, x[1] + 0.3, x[1] - 0.3, x[1] - 0.3],
         [0, 0, 100, 100, 0],
         linestyle='--', color='gold', linewidth=2)

plt.suptitle('Proporción del consumo de catering nocturno en el consumo de catering diario entre los residentes chinos en 2023', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()