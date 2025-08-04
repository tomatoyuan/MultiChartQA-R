import matplotlib.pyplot as plt

# Datos
etiquetas = ["Menos de 1000 yuan", "1001 - 5000 yuan", "5001 - 10000 yuan", "10000 - 30000 yuan", "Más de 30000 yuan", "Sin ingresos"]
tamaños = [33.3, 17.0, 9.4, 3.5, 3.5, 33.3]
# Configuración de colores, tratar de acercarse a los colores de la imagen original
colores = ["#A4C639", "#8DB328", "#7EA11E", "#668718", "#506D12", "#DCDCDC"]

fig, ax = plt.subplots()
# Dibujar un gráfico circular, configurar autopct para mostrar porcentajes, pctdistance para ajustar la posición del porcentaje y textprops para ajustar el estilo del texto
trozos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.1f%%", 
                                           startangle=90, pctdistance=0.8, textprops={"color": "black"})

# Ajustar el tamaño del texto de la anotación
for texto_automatico in textos_automaticos:
    texto_automatico.set_size(10)
for texto in textos:
    texto.set_size(10)

# Establecer el título
ax.set_title("Distribución de ingresos de creadores de contenido esenciales en China a partir de la creación de contenido")

# Mantener el gráfico circular
ax.axis("equal")

plt.show()