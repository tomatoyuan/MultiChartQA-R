import matplotlib.pyplot as plt

# Tipos de empresas y sus datos de proporción
etiquetas = [
    "Manufactura", "Transmisión de información, servicios informáticos y software", "Minería", "Cultura, deportes y entretenimiento",
    "Agricultura, silvicultura, ganadería y pesca", "Comercio al por mayor y al por menor", "Educación", "Construcción", "Inmobiliaria",
    "Producción y suministro de electricidad, gas y agua", "Transporte, almacenamiento y servicios postales", "Finanzas",
    "Salud, seguridad social y bienestar social", "Otros"
]
tamaños = [14.74, 14.32, 2.14, 8.55, 4.27, 8.55, 3.85, 5.34, 7.26, 9.40, 8.97, 4.49, 7.91, 0.21]
# Colores correspondientes (tratar de coincidir con la imagen original, se pueden ajustar según la situación real)
colores = [
    '#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
    '#1E90FF', '#FFD700', '#00FA9A', '#FF69B4', '#00BFFF',
    '#FFA07A', '#9370DB', '#7FFF00', '#BA55D3'
]

fig, ax = plt.subplots(figsize=(12, 8))
# Dibujar un gráfico de dona, wedgeprops establece el ancho de la dona
trozos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                            startangle=90, wedgeprops={"width": 0.4})

# Ajustar el tamaño y el color del texto de la anotación (opcional) para que la posición de la anotación sea más razonable
for texto in textos:
    texto.set_fontsize(10)
for texto_automatico in textos_automaticos:
    texto_automatico.set_fontsize(9)
    texto_automatico.set_color('black')  # Hacer que los valores sean más claros en los bloques de color

ax.set_title('Tipos de empresas en transformación digital en China en 2025')

plt.tight_layout()
plt.show()