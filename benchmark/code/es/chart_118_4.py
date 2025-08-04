import matplotlib.pyplot as plt

# Datos
etiquetas = [
    "Mejora de eficiencia superior al 50%", "Mejora de eficiencia entre 40 - 50%", "Mejora de eficiencia entre 30 - 40%",
    "Mejora de eficiencia entre 20 - 30%", "Mejora de eficiencia entre 10 - 20%", "Mejora de eficiencia inferior al 10%"
]
tamaños = [12.53, 27.52, 31.61, 18.53, 6.54, 3.27]
# Colores correspondientes (trata de coincidir con la imagen original y ajusta según la situación real)
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']

fig, ax = plt.subplots(figsize=(10, 7))
# Dibuja un gráfico de dona, wedgeprops establece el ancho de la dona
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                              startangle=90, wedgeprops={"width": 0.4})

# Ajusta el tamaño y el color del texto de la anotación (opcional) para que la anotación sea más clara
for texto in textos:
    texto.set_fontsize(10)
for texto_automatico in textos_automaticos:
    texto_automatico.set_fontsize(9)
    texto_automatico.set_color('black')  # Hace que los valores sean más claros en los bloques de color

ax.set_title('La mejora de la eficiencia o calidad del trabajo de las empresas chinas por parte de los humanos digitales AI en 2025')

plt.tight_layout()
plt.show()