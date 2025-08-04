import matplotlib.pyplot as plt

# Datos
etiquetas = ["Más de tres veces al día", "Una o dos veces al día", "De cuatro a seis veces a la semana", "De dos a tres veces a la semana", "Una vez a la semana o menos"]
tamaños = [8.91, 41.49, 39.23, 7.05, 3.32]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Establecer el título
ax.set_title("Frecuencia promedio de uso de aplicaciones de audiolibros por parte de los usuarios chinos en 2025")

# Ajustar el tamaño y el color del texto de anotación (opcional)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

plt.show()