import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Muy gusta", "Gusta", "Promedio", "No gusta", "Nunca se ha preocupado"]
tamaños = [20.55, 55.78, 17.06, 6.61, 0.00]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']

fig, ax = plt.subplots(figsize=(10, 8))  # Aumentar el ancho del gráfico para dejar espacio para el texto horizontal

# Dibujar un gráfico circular anular, desactivar la rotación automática de las etiquetas
segmentos, textos, textos_porcentaje = ax.pie(
    tamaños, 
    labels=etiquetas, 
    colors=colores, 
    autopct="%1.2f%%",
    startangle=90, 
    wedgeprops={"width": 0.4},
    pctdistance=0.85,  # Distancia del porcentaje de la etiqueta al centro del círculo
    labeldistance=1.15,  # Distancia de la etiqueta de la categoría al centro del círculo (aumentar para evitar superposiciones)
    rotatelabels=False  # Forzar que las etiquetas no se roten
)

# Forzar que todo el texto se muestre horizontalmente (ángulo de rotación de 0)
for texto in textos + textos_porcentaje:
    texto.set_rotation(0)  # Mostrar horizontalmente
    texto.set_fontsize(11)

# Optimizar la posición de las etiquetas de las partes con poca proporción (evitar superposiciones)
for i, (segmento, texto, texto_porcentaje) in enumerate(zip(segmentos, textos, textos_porcentaje)):
    # Calcular el ángulo del punto medio del sector (para ajustar la posición horizontal del texto)
    angulo = (segmento.theta1 + segmento.theta2) / 2
    angulo_rad = np.deg2rad(angulo)
    
    # Ajustar la alineación del texto según el ángulo (alineación izquierda/derecha para garantizar que no se desvíe al mostrarse horizontalmente)
    if angulo < 90 or angulo > 270:
        texto.set_ha('left')  # Alinear a la izquierda el texto del sector derecho
    else:
        texto.set_ha('right')  # Alinear a la derecha el texto del sector izquierdo
    
    # Ocultar la etiqueta del 0% (evitar mostrar algo sin sentido)
    if tamaños[i] == 0:
        texto_porcentaje.set_visible(False)
        texto.set_visible(False)  # Ocultar también la etiqueta "Nunca se ha preocupado"

# Ajustar el estilo de las etiquetas de porcentaje (fuente blanca para mejorar la legibilidad)
for texto_porcentaje in textos_porcentaje:
    texto_porcentaje.set_color('white')
    texto_porcentaje.set_ha('center')  # Centrar la etiqueta de porcentaje

# Establecer el título
ax.set_title("Preferencia de los consumidores chinos por las figuras en 2025", fontsize=14, pad=20)

plt.tight_layout()
plt.show()