import matplotlib.pyplot as plt

# Datos
etiquetas = ["Meta", "Pico", "DPVR", "HTC", "HP Inc", "Otros"]
tamaños = [75, 6, 6, 5, 3, 5]
colores = ["#FF7F24", "#FFD700", "#32CD32", "#8B4513", "#808000", "#228B22"]

fig, ax = plt.subplots(figsize=(8, 8))
# Dibujar un gráfico de pastel, autopct muestra el porcentaje, pctdistance ajusta la posición del porcentaje, startangle establece el ángulo de inicio
segmentos, textos, textos_porcentaje = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%", 
                                              pctdistance=0.8, startangle=90)

# Ajustar el color del texto de las anotaciones a blanco (opcional, para que los valores sean más claros)
for texto_porcentaje in textos_porcentaje:
    texto_porcentaje.set_color("white")

ax.set_title("Participación del mercado de envíos de dispositivos de cascos de realidad virtual globales")

plt.tight_layout()
plt.show()