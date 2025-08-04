import matplotlib.pyplot as plt

# Datos
etiquetas = ["Hogar Inteligente", "Materiales de Alta Calidad", "Ecológico y Amigable con el Medio Ambiente", "Personalización Personalizada"]
tamaños = [29.09, 22.85, 25.35, 22.71]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0']

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                              startangle=90, wedgeprops={"width": 0.4})

# Ajustar la posición y el estilo del texto de la anotación (opcional) para que la anotación sea más clara
for texto_automatico in textos_automaticos:
    texto_automatico.set_horizontalalignment('center')
    texto_automatico.set_verticalalignment('center')

ax.set_title('Opiniones de los consumidores chinos sobre las tendencias de desarrollo futuro de la industria del mobiliario doméstico en 2025')

plt.show()