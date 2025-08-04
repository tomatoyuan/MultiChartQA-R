import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
etiquetas = ["Muy Satisfecho", "Bastante Satisfecho", "Promedio", "Poco Satisfecho"]
tamaños = [27.2, 58.3, 14.0, 0.5]
# Colores correspondientes, se pueden ajustar según la imagen original
colores = ["#4BA6FF", "#FF9933", "#FFCC33", "#FF6666"]

fig, ax = plt.subplots(figsize=(6, 6))
# Dibujar un gráfico circular, establecer el ángulo de inicio, si se separa, etc.
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%",
                                               startangle=90, wedgeprops={"width": 0.4})

# Ajustar el estilo del texto de la anotación
for texto in textos:
    texto.set_fontsize(12)
for texto_auto in textos_automaticos:
    texto_auto.set_fontsize(10)
    texto_auto.set_color("black")

ax.set_title("Encuesta sobre la satisfacción del público chino con su propia salud", fontsize=14, y=1.05)
plt.show()