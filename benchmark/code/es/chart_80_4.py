import matplotlib.pyplot as plt
import numpy as np

# Categorías
etiquetas = ["Tanto en línea como fuera de línea", "Canales en línea", "Canales fuera de línea"]
# Proporción de cada categoría (%), los datos pueden ser aproximadamente iguales
tamaños = [75.8, 15.5, 8.7]
# Colores de cada parte del gráfico circular, tratar de acercarse a la imagen original
colores = ["#A4C639", "#87D3F2", "#64B5F6"]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(6, 6))

# Dibujar un gráfico circular
porciones, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.1f%%', 
    startangle=140, colors=colores, 
    textprops={'color': 'black'}
)

# Embelezar el texto de la anotación (ajustar el tamaño, etc.)
for texto in textos + textos_automaticos:
    texto.set_fontsize(12)

# Simular la anotación de la flecha TGI (apuntando a los canales fuera de línea)
# Encontrar la porción correspondiente a los canales fuera de línea
porcion_fuera_de_linea = porciones[2]
# Calcular la posición de la anotación
anotacion = ax.annotate(
    'Consumidores en ciudades de bajo nivel\nTGI = 208',
    xy=porcion_fuera_de_linea.center,  # Centro de la porción
    xytext=(1.2, 0.8),  # Posición del texto
    arrowprops=dict(
        facecolor='blue', 
        shrink=0.1, 
        width=1, 
        headwidth=5,
        connectionstyle="arc3,rad=0.3"  # Flecha curva
    ),
    ha='center', 
    va='bottom',
    color='blue', 
    fontsize=10
)

# Establecer el título
ax.set_title("Proporción de canales de compra de productos de pañales para bebés chinos en 2022", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()