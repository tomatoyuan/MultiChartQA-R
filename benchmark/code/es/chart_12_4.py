import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
etiquetas = ["Horario", "Resúmenes del Evento de la Copa Europea", "URLs de Transmisión en Vivo", "Puntuación del Último Juego", "Odds de Campeonato", "Otros"]
porcentajes = [30, 24, 17, 14, 8, 7]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#8BC34A')  # Fondo verde

# Dibujar un gráfico de barras horizontales (usando un gradiente amarillo)
posicion_y = np.arange(len(etiquetas))
colores = plt.cm.YlOrBr(np.linspace(0.6, 1, len(etiquetas)))  # Gradiente de amarillo a naranja
barras = ax.barh(posicion_y, porcentajes, color=colores, edgecolor='black', height=0.6)

# Añadir un título y un subtítulo
ax.set_title('Antes de las Cuartas de Final\nTabla de Distribución de Palabras Clave de Búsqueda', fontsize=18, fontweight='bold', pad=20)

# Establecer las etiquetas del eje y (palabras clave)
ax.set_yticks(posicion_y)
ax.set_yticklabels(etiquetas, fontsize=12)
ax.tick_params(axis='y', which='both', length=0)  # Ocultar las marcas de graduación del eje y

# Establecer las etiquetas del eje x (porcentajes)
ax.set_xlabel('Proporción de Búsqueda (%)', fontsize=12, labelpad=15)
ax.set_xlim(0, 35)  # Dejar espacio en el lado derecho
ax.set_xticks(np.arange(0, 36, 5))
ax.set_xticklabels([f'{x}%' for x in np.arange(0, 36, 5)], fontsize=10)

# Añadir etiquetas numéricas a cada barra
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 0.8, barra.get_y() + barra.get_height()/2,
            f'{ancho}%', ha='left', va='center', fontsize=10, fontweight='bold')

# Añadir "Iconos de Persona" (usando formas nativas de matplotlib en su lugar)
for i, (etiqueta, porcentaje) in enumerate(zip(etiquetas, porcentajes)):
    # Dibujar una "persona" simplificada (una cabeza circular + un cuerpo rectangular)
    cabeza = plt.Circle((-2.5, posicion_y[i]), 0.3, color='yellow', ec='black')
    cuerpo = plt.Rectangle((-2.8, posicion_y[i]-0.3), 0.6, 0.6, color='yellow', ec='black')
    ax.add_patch(cabeza)
    ax.add_patch(cuerpo)

    # Añadir una marca de "Corazón" (usando un triángulo en su lugar)
    x_corazon = [-2.6, -2.4, -2.5]
    y_corazon = [posicion_y[i]+0.15, posicion_y[i]+0.15, posicion_y[i]+0.3]
    ax.fill(x_corazon, y_corazon, color='red')

# Añadir marcas de "Lupa" (usando formas nativas de matplotlib)
for i, p in enumerate(porcentajes):
    num_lupas = p // 5
    for j in range(num_lupas):
        # Dibujar una lupa simplificada
        x_lupa = [-5 - j*0.8, -4.5 - j*0.8, -4.7 - j*0.8, -5 - j*0.8]
        y_lupa = [posicion_y[i]+0.1, posicion_y[i]+0.1, posicion_y[i]-0.1, posicion_y[i]-0.1]
        ax.fill(x_lupa, y_lupa, color='black')
        # Mango de la lupa
        ax.plot([-4.5 - j*0.8, -4.3 - j*0.8], [posicion_y[i], posicion_y[i]-0.2], 'k-', linewidth=1.5)

# Ocultar los bordes superior y derecho
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

# Ajustar el diseño
plt.tight_layout(pad=3)
plt.show()