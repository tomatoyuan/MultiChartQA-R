import matplotlib.pyplot as plt



# Datos
etiquetas = ['Modelo de color carne/tono de piel', 'Modelo de color negro', 'Compraré ambos colores']
tamaños = [61, 32, 7]
colores = ['#ffd6d6', '#ff8080', '#ffeaea']  # Combinación de tonos de rosa degradados similar a la imagen original
resaltar = (0, 0.05, 0.1)  # Resaltar los dos últimos elementos

# Crear la gráfica
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=tamaños,
    explode=resaltar,
    colors=colores,
    startangle=90,
    counterclock=False,
    autopct='%1.0f%%',
    textprops={'fontsize': 12, 'color': 'white'},
    wedgeprops=dict(width=0.9, edgecolor='white')
)

# Establecer el título
ax.set_title("Encuesta sobre las preferencias de color de medias de desnudo de los consumidores", fontsize=14, weight='bold')

# Agregar la leyenda
ax.legend(porciones, etiquetas, loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, frameon=False, fontsize=10)

# Agregar la fuente de los datos
texto_fuente = "Fuente de datos: Datos de la encuesta realizada por CBNData en julio de 2024"
plt.figtext(0.5, -0.12, texto_fuente, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()