# Datos
etiquetas = ["Beneficiado en gran medida", "Obtuvo algo", "Poca sensación"]
tamaños = [35.76, 53.31, 10.93]
# Colores correspondientes
colores = ["#FF7F27", "#4B53FF", "#32CD32"]

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# Dibujar un gráfico de dona, wedgeprops establece el ancho de la dona
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                              startangle=90, wedgeprops={"width": 0.4})

# Establecer el título
ax.set_title("Percepción de los usuarios chinos en 2025 sobre el aprendizaje de música para cultivar estética y pensamiento")

# Ajustar el tamaño y el color del texto de la anotación (opcional)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

plt.show()