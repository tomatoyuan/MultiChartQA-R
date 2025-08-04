import matplotlib.pyplot as plt

# Datos
etiquetas = ["Muy optimista", "Algo optimista", "Neutral", "Algo pesimista", "Muy pesimista"]
tamaños = [20.84, 47.66, 21.22, 5.82, 4.46]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
segmentos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                              startangle=90, wedgeprops={"width": 0.4})

# Ajustar la posición y el estilo del texto de la anotación (opcional) para que la anotación sea más clara
for texto_automatico in textos_automaticos:
    texto_automatico.set_horizontalalignment('center')
    texto_automatico.set_verticalalignment('center')

ax.set_title('Opiniones de los consumidores chinos sobre las perspectivas de desarrollo futuro del comercio minorista de productos agrícolas en 2025')

plt.show()