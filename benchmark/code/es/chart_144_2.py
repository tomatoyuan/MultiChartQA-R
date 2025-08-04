import matplotlib.pyplot as plt
import numpy as np

# --------------------- Datos del Gráfico Circular Izquierdo ---------------------
etiquetas_pastel = ["$501 - $1000", "$1001 - $3000", "$500 y por debajo", "$3001 y por encima"]
tamaños_pastel = [49.5, 41.4, 6.5, 2.6]
colores_pastel = ["#D2691E", "#F4A460", "#CD853F", "#FFDEAD"]

# --------------------- Datos del Gráfico de Barras Agrupadas Derecho ---------------------
etiquetas_barras = ["3 veces a la semana o más", "1 - 2 veces a la semana", "1 - 2 veces al mes", "Una vez cada pocos meses", "Casi no consume en la ciudad universitaria"]
tamaños_barras = [
    [13.5, 86.5],  # Primer grupo: Naranja abajo, color claro arriba
    [51.8, 48.2],
    [29.5, 70.5],
    [3.6, 96.4],
    [1.6, 98.4]
]
colores_barras = ["#D2691E", "#FAF0E6"]  # Naranja, beige claro

# Crear un lienzo con un diseño de 1 fila y 2 columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Dibujar el Gráfico Circular Izquierdo ---------------------
wedges, textos, autotextos = ax1.pie(tamaños_pastel, colors=colores_pastel, autopct='%1.1f%%', startangle=90)
ax1.set_title('Consumo mensual promedio de los principales grupos de consumidores en ciudades universitarias chinas desde 2023')
# Ajustar la leyenda
ax1.legend(wedges, etiquetas_pastel, title="Rango de consumo", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de las anotaciones
for autotexto in autotextos:
    autotexto.set_color('white' if autotexto.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el Gráfico de Barras Agrupadas Derecho ---------------------
# Dibujar el gráfico de barras agrupadas (en forma apilada)
x = np.arange(len(etiquetas_barras))
base = np.zeros(len(etiquetas_barras))
for i in range(2):
    ax2.bar(x, [tamaño[i] for tamaño in tamaños_barras], bottom=base, color=colores_barras[i], label=etiquetas_pastel[i] if i == 0 else '')
    base += [tamaño[i] for tamaño in tamaños_barras]

ax2.set_title('Frecuencia de consumo de los principales grupos de consumidores en ciudades universitarias chinas en 2023')
ax2.set_ylabel('Proporción (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(etiquetas_barras)
ax2.legend(title="Rango de consumo", loc="upper left")

# Agregar anotaciones numéricas al gráfico de barras agrupadas
for i, (tamaño1, tamaño2) in enumerate(tamaños_barras):
    ax2.text(i, tamaño1 / 2, f'{tamaño1}%', ha='center', va='center', color='white')
    ax2.text(i, tamaño1 + tamaño2 / 2, f'{tamaño2}%', ha='center', va='center', color='black')

# Simular una caja discontinua amarilla (segundo grupo)
ax2.plot([x[1] - 0.3, x[1] + 0.3, x[1] + 0.3, x[1] - 0.3, x[1] - 0.3],
         [0, 0, 100, 100, 0],
         linestyle='--', color='gold', linewidth=2)

plt.suptitle('Análisis del comportamiento de los principales grupos de consumidores en ciudades universitarias chinas: Rango y frecuencia de consumo', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()