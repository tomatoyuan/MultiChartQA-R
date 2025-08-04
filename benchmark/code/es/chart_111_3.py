import matplotlib.pyplot as plt

# Datos
etiquetas = ["Optimista, calidad de drama decente", "Neutral", "Pesimista, calidad de drama preocupante"]
tamaños = [49.63, 33.83, 16.54]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32']

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Establecer el título
ax.set_title("Opiniones de los espectadores de dramas de televisión chinos sobre la industria de dramas domésticos en 2025")

# Ajustar el tamaño y el color del texto de anotación (opcional)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

plt.show()