import matplotlib.pyplot as plt
import numpy as np

# Definición de datos
grupos_edad = ["De 19 - 24 años", "De 25 - 34 años", "Menores de 18 años", "De 35 - 49 años", "Mayores de 50 años"]
porcentajes_edad = [52, 41, 5, 2, 0]
colores_edad = ['#4A7ABC', '#5EB95E', '#F37B1D', '#905CA9', '#E5E5E5']

# Crear un lienzo
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Dibujar un gráfico circular mejorado
wedges, texts = ax.pie(
    porcentajes_edad,
    labels=None,
    autopct=None,
    startangle=90,
    colors=colores_edad,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'antialiased': True},
    pctdistance=0.8,
)

# Agregar un efecto de sombra al gráfico circular
for w in wedges:
    w.set_alpha(0.9)
    w.set_zorder(1)

# Establecer el título
ax.set_title("Proporción de atención de diferentes grupos de edad al 11.11", fontsize=16, pad=25,
              fontweight='bold', color='#333333')
ax.axis('equal')  # Asegurar que el gráfico circular sea circular

# Optimizar el cálculo de la posición de las etiquetas, usando un estilo de línea diagonal + horizontal
posiciones_etiquetas = []

for i, (wedge, grupo, porcentaje) in enumerate(zip(wedges, grupos_edad, porcentajes_edad)):
    if porcentaje == 0:  # Saltar la parte del 0%
        continue

    # Obtener el ángulo del sector
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    rad = np.deg2rad(ang)
    y = np.sin(rad)
    x = np.cos(rad)

    # Ajustar inteligentemente la distancia de la etiqueta
    angulo = wedge.theta2 - wedge.theta1
    radio_base = 1.25
    radio = radio_base + max(0, 0.3 - angulo / 180)

    # Calcular los puntos finales de la línea diagonal y la línea horizontal
    longitud_linea1 = 0.25
    longitud_linea2 = 0.4

    fin_linea1_x = x * (1 + longitud_linea1)
    fin_linea1_y = y * (1 + longitud_linea1)

    if x > 0:  # Etiquetas del lado derecho
        fin_linea2_x = fin_linea1_x + longitud_linea2
        fin_linea2_y = fin_linea1_y
    else:  # Etiquetas del lado izquierdo
        fin_linea2_x = fin_linea1_x - longitud_linea2
        fin_linea2_y = fin_linea1_y

    # Comprobar si hay una superposición con etiquetas existentes
    superposicion = False
    pos_etiqueta = (fin_linea2_x, fin_linea2_y)

    for pos in posiciones_etiquetas:
        dist = np.sqrt((pos_etiqueta[0] - pos[0]) ** 2 + (pos_etiqueta[1] - pos[1]) ** 2)
        if dist < 0.3:
            superposicion = True
            if x > 0:  # Mover la etiqueta del lado derecho hacia arriba
                fin_linea1_y += 0.1
                fin_linea2_y += 0.1
            else:  # Mover la etiqueta del lado izquierdo hacia abajo
                fin_linea1_y -= 0.1
                fin_linea2_y -= 0.1
            break

    posiciones_etiquetas.append(pos_etiqueta)

    # Dibujar la línea de conexión de dos segmentos
    ax.plot([x, fin_linea1_x], [y, fin_linea1_y], color='#999999', linestyle='-', linewidth=1)
    ax.plot([fin_linea1_x, fin_linea2_x], [fin_linea1_y, fin_linea2_y], color='#999999', linestyle='-', linewidth=1)

    # Agregar texto de la etiqueta
    if x > 0:
        ax.text(fin_linea2_x + 0.05, fin_linea2_y, f"{grupo}: {porcentaje}%",
                ha='left', va='center', fontsize=11, backgroundcolor='white')
    else:
        ax.text(fin_linea2_x - 0.05, fin_linea2_y, f"{grupo}: {porcentaje}%",
                ha='right', va='center', fontsize=11, backgroundcolor='white')

# Ajustar el diseño
plt.tight_layout(pad=3)

# Guardar el gráfico (opcional)
# plt.savefig('distribucion_edad.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()