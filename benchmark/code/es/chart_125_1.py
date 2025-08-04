import matplotlib.pyplot as plt

# Datos
etiquetas = ["Dos años", "Tres años", "Cuatro años y más", "Dentro de un año"]
tamaños = [49.0, 33.7, 9.3, 8.0]
colores = ["#8B4513", "#FFA07A", "#32CD32", "#FF8C00"]

fig, ax = plt.subplots(figsize=(6, 6))
# Dibujar un gráfico de pastel, autopct muestra el porcentaje, startangle establece el ángulo de inicio
porciones, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%", startangle=90)

# Ajustar el color del texto de la anotación a blanco para mayor claridad
for texto_automatico in textos_automaticos:
    texto_automatico.set_color("white")

ax.set_title("Frecuencia con la que los consumidores chinos cambian de teléfono móvil")
plt.show()