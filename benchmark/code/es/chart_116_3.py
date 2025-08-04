import matplotlib.pyplot as plt

# Datos
etiquetas = ["Darán consideración especial", "Considerarán, pero no como factor principal", "No considerarán"]
tamaños = [47.01, 39.58, 13.41]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32']

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
segmentos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                               startangle=90, wedgeprops={"width": 0.4})

# Ajustar la posición y el estilo del texto de anotación (opcional)
for texto_automatico in textos_automaticos:
    texto_automatico.set_horizontalalignment('center')
    texto_automatico.set_verticalalignment('center')

ax.set_title('Consideración de productos agrícolas locales conocidos por los consumidores chinos en 2025')

plt.show()