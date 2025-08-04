import matplotlib.pyplot as plt
import numpy as np

# Izquierda: Datos de encuesta sobre la cantidad de APPs de corretaje de autogestión que poseen los usuarios chinos de corretaje
left_labels = ["3 - 4", "1 - 2", "5 o más"]
left_sizes = [54.55, 39.57, 5.88]
left_colors = ["gold", "coral", "green"]

# Derecha: Datos de encuesta sobre la cantidad de veces que los usuarios chinos de corretaje abren las APPs de corretaje de autogestión por día
right_labels = ["Abre varias veces al día en promedio", "Abre varias veces a la semana en promedio", 
                "Abre muchas veces al día en promedio", "Abre varias veces al mes en promedio", 
                "Abre menos de una vez al año en promedio"]
right_sizes = [44.39, 32.09, 14.97, 7.49, 1.06]
right_colors = ["gold", "green", "coral", "brown", "olive"]

# Crea una figura más grande
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# Gráfico circular izquierdo: Cantidad de APPs poseídas
# Ajusta la posición de la etiqueta de porcentaje con pctdistance
wedges, texts, autotexts = ax1.pie(
    left_sizes, 
    labels=left_labels, 
    colors=left_colors, 
    autopct="%1.2f%%",
    startangle=90,
    pctdistance=0.85,  # Distancia de las etiquetas de porcentaje desde el centro
    textprops={'fontsize': 12}  # Tamaño de fuente de las etiquetas
)

# Ajusta los colores de las etiquetas de porcentaje izquierdas
for autotext in autotexts:
    autotext.set_color("black")

# Establece el título izquierdo
ax1.set_title("Encuesta sobre la cantidad de APPs de corretaje de autogestión\nque poseen los usuarios chinos de corretaje", fontsize=14, pad=20)

# Gráfico circular derecho: Cantidad de aperturas diarias
# Utiliza el parámetro explode para separar las rebanadas y evitar la superposición de etiquetas
explode = (0.05, 0.05, 0.05, 0.05, 0.08)  # Separación para cada rebanada
wedges, texts, autotexts = ax2.pie(
    right_sizes, 
    labels=right_labels, 
    colors=right_colors, 
    autopct="%1.2f%%",
    startangle=90,
    explode=explode,  # Separa las rebanadas para evitar la superposición de etiquetas
    pctdistance=0.85,  # Distancia de las etiquetas de porcentaje desde el centro
    labeldistance=1.1,  # Distancia de las etiquetas de categoría desde el centro
    textprops={'fontsize': 11}  # Tamaño de fuente de las etiquetas
)

# Ajusta los colores de las etiquetas de porcentaje derechas
for autotext in autotexts:
    autotext.set_color("black")

# Establece el título derecho
ax2.set_title("Encuesta sobre la cantidad de veces que los usuarios chinos de corretaje abren las APPs de corretaje de autogestión por día", fontsize=14, pad=20)

# Ajusta el diseño
plt.tight_layout(pad=5.0)  # Aumenta el espacio entre los subgráficos

plt.show()