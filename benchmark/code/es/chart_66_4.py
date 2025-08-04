import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Nombres de los canales
canales = ["Tmall", "JD", "Tienda de mascotas", "Taobao", "Hospital de mascotas"]
# Datos correspondientes (porcentaje)
datos = [27, 27, 19, 17, 10]
# Rutas de los iconos, aquí se asume que tienes archivos de iconos locales correspondientes, hay que reemplazarlos con las rutas reales
rutas_iconos = ["tmall_icon.png", "jd_icon.png", "pet_shop_icon.png", "taobao_icon.png", "pet_hospital_icon.png"]
# Configuración de colores, similar al verde y gris de la imagen original
colores_barras = ["#A4C639", "#A4C639", "#A4C639", "#A4C639", "#A4C639"]
colores_fondo = ["#D3D3D3"] * len(canales)

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 5))

# Dibujar un gráfico de barras, establecer el ancho general, etc.
x = np.arange(len(canales))
ancho_barra = 0.6
for i in range(len(canales)):
    # Dibujar una barra de fondo gris
    rect_fondo = ax.bar(x[i], 100, ancho_barra, color=colores_fondo[i], edgecolor="white")
    # Dibujar una barra de primer plano de color
    barra = ax.bar(x[i], datos[i], ancho_barra, color=colores_barras[i], edgecolor="white")
    # Agregar etiquetas de datos
    ax.annotate(f'{datos[i]}%',
                xy=(x[i], datos[i]),
                xytext=(5, -15),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom',
                color="black")

    # Procesar iconos, aquí es una demostración simple, para una restauración precisa, se necesitan más ajustes detallados
    try:
        icono = Image.open(rutas_iconos[i])
        icono = icono.resize((20, 20))  # Ajustar el tamaño del icono
        fig.canvas.draw()
        ax_imagen = fig.add_axes([ax.get_xlim()[0] + i * (ax.get_xlim()[1] - ax.get_xlim()[0])/len(canales) - 0.03, 
                                 ax.get_ylim()[0] + 0.01, 0.05, 0.05])  # Posición del icono
        ax_imagen.imshow(icono)
        ax_imagen.axis("off")
    except:
        pass

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(canales)
# Ocultar el eje y
ax.set_yticks([])
ax.set_ylabel("")
# Establecer el título
ax.set_title("Los 5 principales canales de compra de ungüentos", fontsize=14, fontweight="bold")

# Embelezar el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)
    
plt.show()