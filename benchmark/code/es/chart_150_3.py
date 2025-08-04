import matplotlib.pyplot as plt

# Preparación de datos
etiquetas = ["1 - 3 veces", "4 - 6 veces", "7 - 9 veces", "10 veces y más"]
tamaños = [41.0, 45.0, 10.0, 4.0]  # Proporción (%)
colores = ["lightpink", "coral", "sandybrown", "brown"]  # Esquema de colores, similar a la imagen original

fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de pastel
wedges, textos, autotextos = ax.pie(
    tamaños, 
    colors=colores, 
    autopct='%1.1f%%', 
    startangle=140,  # Ajustar el ángulo de inicio para que la distribución del gráfico de pastel sea más razonable
    pctdistance=0.8  # Ajustar la posición de la etiqueta para evitar solaparse con la leyenda
)

ax.set_title('Distribución de la frecuencia de consumo semanal de usuarios de servicios de vida local en China en 2023', fontsize=14)

# Establecer la leyenda (misma posición y estilo que la imagen original)
ax.legend(
    wedges, 
    etiquetas, 
    title="Frecuencia de consumo semanal", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5)
)

# Optimizar el color del texto de la etiqueta (usar texto blanco para las rebanadas oscuras y texto negro para las claras)
for autotexto in autotextos:
    autotexto.set_color('white' if autotexto.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()