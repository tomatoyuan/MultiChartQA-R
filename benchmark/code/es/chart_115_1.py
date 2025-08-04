import matplotlib.pyplot as plt

# Datos
etiquetas = ["No, en absoluto", "Sí, la transformación digital se ha considerado e implementado en la estrategia empresarial"]
tamaños = [13.81, 86.19]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF']

fig, ax = plt.subplots()
# Dibujar un gráfico de donut, wedgeprops establece el ancho del donut
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Establecer el título
ax.set_title("Estado de las empresas chinas que incorporan la transformación digital en sus planes empresariales en 2025")

# Ajustar el tamaño y el color del texto de la anotación (opcional)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

plt.show()