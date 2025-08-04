import matplotlib.pyplot as plt

# Datos
etiquetas = ["Todos los días", "4 - 5 veces a la semana", "1 - 3 veces a la semana", "Lectura irregular y fragmentada"]
tamaños = [19.96, 51.54, 21.93, 6.57]
# Colores correspondientes
colores = ["#FF7F27", "#4B53FF", "#32CD32", "#9400D3"]

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
segmentos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                              startangle=90, wedgeprops={"width": 0.4})

# Establecer el título
ax.set_title("Frecuencia de lectura de información de medios financieros por usuarios de noticias financieras chinas en 2025")

# Ajustar el tamaño y el color del texto de la anotación (opcional)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

plt.show()