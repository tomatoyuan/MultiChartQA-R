import matplotlib.pyplot as plt
import numpy as np

# Definir datos estrictamente según el orden del gráfico (mantener el orden original)
datos = [
    {"provincia": "Guangxi", "region": "Occidental", "crecimiento": 145},
    {"provincia": "Ningxia", "region": "Occidental", "crecimiento": 135},
    {"provincia": "Mongolia Interior", "region": "Occidental", "crecimiento": 135},
    {"provincia": "Tianjin", "region": "Oriental", "crecimiento": 120},
    {"provincia": "Jiangxi", "region": "Central", "crecimiento": 105},
    {"provincia": "Liaoning", "region": "Noreste", "crecimiento": 100},
    {"provincia": "Jiangsu", "region": "Oriental", "crecimiento": 100},
    {"provincia": "Hebei", "region": "Oriental", "crecimiento": 90},
    {"provincia": "Zhejiang", "region": "Oriental", "crecimiento": 85},
    {"provincia": "Hainan", "region": "Oriental", "crecimiento": 85},
    {"provincia": "Guizhou", "region": "Occidental", "crecimiento": 80},
    {"provincia": "Shanghai", "region": "Oriental", "crecimiento": 75},
    {"provincia": "Heilongjiang", "region": "Noreste", "crecimiento": 70},
    {"provincia": "Guangdong", "region": "Oriental", "crecimiento": 65},
    {"provincia": "Hubei", "region": "Central", "crecimiento": 60},
    {"provincia": "Sichuan", "region": "Occidental", "crecimiento": 55},
    {"provincia": "Shanxi", "region": "Central", "crecimiento": 45},
    {"provincia": "Shandong", "region": "Oriental", "crecimiento": 40},
    {"provincia": "Chongqing", "region": "Occidental", "crecimiento": 40},
    {"provincia": "Xinjiang", "region": "Occidental", "crecimiento": 35},
    {"provincia": "Beijing", "region": "Oriental", "crecimiento": 30},
    {"provincia": "Henan", "region": "Central", "crecimiento": 25},
    {"provincia": "Hunan", "region": "Central", "crecimiento": 20},
    {"provincia": "Jilin", "region": "Noreste", "crecimiento": 10}
]

# Extraer datos
provincias = [item["provincia"] for item in datos]
regiones = [item["region"] for item in datos]
crecimientos = [item["crecimiento"] for item in datos]

# Mapeo de región - color (coincidir estrictamente con la imagen original)
color_region = {
    "Oriental": "#4CADDF",  # Azul
    "Central": "#8FC31F",  # Verde
    "Occidental": "#FBBE28",  # Naranja
    "Noreste": "#F26522"  # Rojo
}
colores = [color_region[reg] for reg in regiones]

# Crear un lienzo
plt.figure(figsize=(8, 10))  # Ajustar el tamaño del lienzo para ajustarse a los datos

# Crear el eje x principal (eje x inferior)
ax1 = plt.subplot(111)

# Dibujar un gráfico de barras horizontales (el orden de los datos del eje Y se invierte)
pos_y = np.arange(len(provincias))
barras = ax1.barh(pos_y[::-1], crecimientos, color=colores, height=0.7)

# Establecer las etiquetas del eje Y (nombres de las provincias, mantener el orden original)
ax1.set_yticks(pos_y)
ax1.set_yticklabels(provincias[::-1], fontsize=10)

# Establecer las marcas del eje x inferior (formato de porcentaje)
ax1.set_xlim(0, 150)
ax1.set_xticks([0, 30, 60, 90, 120, 150])
ax1.set_xticklabels(["0%", "30%", "60%", "90%", "120%", "150%"], fontsize=9)
ax1.set_xlabel("Tasa de crecimiento", fontsize=10)

# Crear el eje x superior (compartir el eje Y con el eje x inferior)
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())  # Asegurar que los ejes x superior e inferior tengan el mismo rango
ax2.set_xticks([0, 30, 60, 90, 120, 150])
ax2.set_xticklabels(["0%", "30%", "60%", "90%", "120%", "150%"], fontsize=9)

# Agregar un título
plt.title("Tasa de crecimiento año tras año de las búsquedas de nuevos productos domésticos por usuarios en cada provincia en 2020",
          fontsize=12, fontweight="bold", y=1.03)

# Construir manualmente la leyenda (coincidir con la posición y el estilo original)
from matplotlib.patches import Patch
parches_leyenda = [
    Patch(color=color_region["Oriental"], label="Oriental"),
    Patch(color=color_region["Central"], label="Central"),
    Patch(color=color_region["Occidental"], label="Occidental"),
    Patch(color=color_region["Noreste"], label="Noreste")
]
ax1.legend(handles=parches_leyenda, bbox_to_anchor=(1, 0.7),
           fontsize=9, frameon=False)

# Ajustar el diseño (evitar la superposición de la leyenda y el contenido)
plt.subplots_adjust(left=0.3, right=0.8)  # Reservar espacio a la derecha para la leyenda

# Agregar etiquetas de datos (corregir el orden)
for i, barra in enumerate(barras):
    ancho = barra.get_width()
    ax1.text(ancho + 2, barra.get_y() + barra.get_height() / 2,
             f"{crecimientos[i]}%",  # Corregir el índice, usar directamente i
             ha='left', va='center', fontsize=9)

# Agregar una nota (restaurar estrictamente la nota inferior)
plt.figtext(0.55, 0.05, "Nota: La división regional se refiere a las cuatro principales regiones económicas de China.",
            ha="center", fontsize=8, color="gris")

# Mostrar el gráfico
plt.show()