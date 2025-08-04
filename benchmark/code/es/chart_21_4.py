import matplotlib.pyplot as plt
import numpy as np

# Nombres de las ciudades
ciudades = ["Guangzhou", "Beijing", "Shanghai", "Shenzhen", "Hangzhou", "Fuzhou", "Ningbo", "Wenzhou", "Xiamen", "Wuhan"]
# Datos simulados para el gráfico de barras, generalmente mostrando diferencias de altura, se pueden ajustar según la situación real
datos = [30, 25, 22, 20, 18, 16, 19, 17, 15, 14]

x = np.arange(len(ciudades))  # Coordenadas del eje x
ancho = 0.5  # Ancho de las barras

fig, ax = plt.subplots(figsize=(10, 6))  # Crear un lienzo y un objeto de eje, establecer el tamaño de la figura
# Dibujar el gráfico de barras, establecer los colores en dos tonos cercanos a la imagen original, los valores rgb se pueden ajustar para acercarse más
barras1 = ax.bar(x[::2], datos[::2], ancho, color=(209/255, 78/255, 68/255))  # Barras de la serie roja
barras2 = ax.bar(x[1::2], datos[1::2], ancho, color=(255/255, 235/255, 201/255))  # Barras de color beige claro

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(ciudades, rotation=45, ha='right', fontsize=10)  # Inclinar 45 grados y alinear a la derecha

# Establecer el título del gráfico
ax.set_title("Las 10 ciudades de salida más populares para los viajes de la Fiesta de la Primavera", fontsize=14, fontweight='bold')

# Agregar etiqueta al eje x
ax.set_xlabel("Ciudad", fontsize=12)
# Agregar etiqueta y unidad al eje y
ax.set_ylabel("Índice de popularidad de viajes", fontsize=12)

# Ocultar los ejes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Agregar etiquetas numéricas sobre cada barra
for i, v in enumerate(datos):
    ax.text(i, v + 0.5, str(v), ha='center', fontsize=10)

# Usar métodos de dibujo puros para crear elementos decorativos en lugar de imágenes
from matplotlib.patches import Polygon, Circle

# Crear la forma de un globo aerostático
def crear_globo(ax, x, y, escala=1.0):
    # Cuerpo del globo
    globo = Polygon([
        (x, y+15*escala), (x-5*escala, y+5*escala), (x-3*escala, y), 
        (x+3*escala, y), (x+5*escala, y+5*escala), (x, y+15*escala)
    ], fill=True, color=(209/255, 78/255, 68/255))
    ax.add_patch(globo)
    
    # Canasta
    canasta = Polygon([
        (x-2*escala, y), (x-3*escala, y-3*escala), 
        (x+3*escala, y-3*escala), (x+2*escala, y)
    ], fill=True, color=(139/255, 69/255, 19/255))
    ax.add_patch(canasta)
    
    # Cuerdas
    ax.plot([x-2*escala, x-2.5*escala], [y, y-1.5*escala], 'k-', linewidth=0.5)
    ax.plot([x+2*escala, x+2.5*escala], [y, y-1.5*escala], 'k-', linewidth=0.5)

# Agregar una decoración de globo aerostático en la esquina superior derecha
crear_globo(ax, 8.5, 32, escala=0.3)

plt.tight_layout()  # Ajustar el diseño para garantizar que las etiquetas no se solapen
plt.show()