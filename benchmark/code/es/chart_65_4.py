import matplotlib.pyplot as plt
import numpy as np

# Fuentes de ingresos
etiquetas = ["Compartición de tráfico (por ejemplo, programas de compartición de ingresos publicitarios de la plataforma)", 
             "Pedidos privados (por ejemplo, ofrecer servicios de personalización personalizada)", 
             "Marketing de contenido (por ejemplo, colaboración y promoción de marcas)", 
             "Promoción de productos de comercio electrónico (gráficos/vídeos/transmisiones en vivo)", 
             "Pago por conocimiento (por ejemplo, cursos pagados, contenido premium)", 
             "Otras fuentes"]
# Datos correspondientes
tamaños = [46.2, 44.5, 18.9, 16.5, 13.9, 12.0]
# Configuración de colores, tratando de acercarse al esquema de color verde original
colores = ["#A4C639"] * len(etiquetas)

x = np.arange(len(etiquetas))  # Se utiliza para establecer las posiciones del eje x
ancho_barra = 0.5  # Ancho del gráfico de barras

fig, ax = plt.subplots()
# Dibujar el gráfico de barras
barras = ax.bar(x, tamaños, width=ancho_barra, color=colores, edgecolor="white")  

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Distancia vertical desde la barra
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas para una mejor visualización
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=25, ha="right")
# Establecer la etiqueta del eje y (el gráfico original no muestra la etiqueta del eje y, decidir si agregarla según sea necesario)
# ax.set_ylabel("Porcentaje (%)")
# Establecer el título del gráfico
ax.set_title("Principales fuentes de ingresos de creadores de contenido que monetizan su contenido en China y el extranjero")

# Hacer el gráfico más bonito, ocultar los bordes superior y derecho
for borde in ["top", "right"]:
    ax.spines[borde].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño para evitar que las etiquetas se muestren incompletas
plt.show()