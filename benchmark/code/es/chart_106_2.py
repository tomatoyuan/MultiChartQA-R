import matplotlib.pyplot as plt

# Datos
etiquetas = ["Menos de 3 veces al mes", "1 - 2 veces a la semana", "3 - 4 veces a la semana", "Más de 5 veces a la semana"]
tamaños = [9.92, 49.60, 29.22, 11.26]
# Colores correspondientes
colores = ["#FF7F27", "#4B53FF", "#32CD32", "#9467BD"]

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
segmentos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                              startangle=90, wedgeprops={"width": 0.4})

# Establecer el título
ax.set_title("Frecuencia de consumo de agua embotellada por los consumidores chinos en 2025")

# Ajustar el tamaño y el color del texto de anotación (opcional)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

plt.show()