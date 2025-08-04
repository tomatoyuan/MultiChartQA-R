import matplotlib.pyplot as plt

# Preparación de datos
etiquetas = ["100 - 1000 yuan", "1001 - 2000 yuan", "2001 - 4000 yuan", "4001 - 8000 yuan", "8001 - 10000 yuan", "Más de 10000 yuan"]
tamaños = [20.1, 26.3, 32.7, 14.2, 5.3, 1.4]
colores = ["blue", "orange", "gray", "yellow", "cyan", "green"]

fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico circular
porciones, textos, textos_automaticos = ax.pie(tamaños, colors=colores, autopct='%1.1f%%', startangle=140)

ax.set_title('Proporción del gasto en pérdida de peso de los usuarios chinos de Internet en 2023')

# Ajustar la leyenda
ax.legend(porciones, etiquetas, title="Rango de gasto", loc="center left", bbox_to_anchor=(1, 0.5))

# Ajustar el color del texto de anotación (hacer el texto de anotación de las porciones de color oscuro blanco y el de las porciones de color claro negro para mayor claridad)
for texto_automatico in textos_automaticos:
    texto_automatico.set_color('white' if texto_automatico.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()