import matplotlib.pyplot as plt

# Datos
etiquetas = [
    "Comercio electrónico", "Educación", "Transporte", "Medios de comunicación", "Finanzas", "Cine y televisión", 
    "Servicios inmobiliarios", "Juegos", "Salud, seguridad social y bienestar social", "Cultura y turismo", "Otros"
]
tamaños = [16.49, 11.97, 8.24, 8.24, 10.51, 7.31, 7.85, 6.78, 12.91, 8.64, 1.06]
# Colores correspondientes (trata de coincidir con la imagen original y ajusta según la situación real)
colores = [
    '#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63',
    '#1E90FF', '#FFD700', '#00FA9A', '#FF69B4', '#00BFFF', '#BA55D3'
]

fig, ax = plt.subplots(figsize=(12, 8))
# Dibuja un gráfico de donut, wedgeprops establece el ancho del donut
segmentos, textos, textos_automaticos = ax.pie(tamaños, labels=etiquetas, colors=colores, autopct="%1.2f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Ajusta el tamaño y el color del texto de la anotación (opcional) para que la anotación sea más clara
for texto in textos:
    texto.set_fontsize(10)
for texto_automatico in textos_automaticos:
    texto_automatico.set_fontsize(9)
    texto_automatico.set_color('black')  # Hace que los valores sean más claros en los bloques de color

ax.set_title('Distribución industrial de las empresas chinas que utilizan humanos digitales AI en 2025')

plt.tight_layout()
plt.show()