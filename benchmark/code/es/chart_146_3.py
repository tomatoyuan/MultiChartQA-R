import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos (Actividades de entretenimiento en línea y fuera de línea y sus proporciones)
datos_online = {
    "Ver programas de televisión y películas": 73.2, "Ver vídeos cortos": 59.0, "Escuchar música": 46.0,
    "Ver transmisiones en vivo": 42.3, "Leer noticias": 39.3, "Navegar por comunidades de contenido": 32.5,
    "Leer libros electrónicos como novelas y cómics": 31.8, "Jugar juegos": 31.5, "Navegar por Weibo": 19.72, "Otros": 0.14
}
datos_offline = {
    "Ver películas en el cine": 51.91, "Hacer ejercicio y mantenerse en forma": 45.53, "Reunirse con amigos": 40.99,
    "Ir a un salón de karaoke (KTV)": 31.63, "Visitar librerías": 30.07, "Ir a bares": 29.50, "Bailar en la plaza": 26.38,
    "Actividades en el mercado nocturno": 25.96, "Festivales de música": 15.32, "Salas de escape": 14.61, "Juegos de misterio con guiones": 11.63,
    "Museos nocturnos": 11.06, "Salas de estudio pagadas": 5.96, "Otros": 0.57
}
# Proporción del anillo
anillo_online = 24.4
anillo_offline = 34.9

# Crear un lienzo con un diseño de una fila y dos columnas
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))

# --------------------- Dibujar el gráfico de barras horizontales de entretenimiento en línea a la izquierda ---------------------
x_online = list(datos_online.values())
y_online = list(datos_online.keys())
ax1.barh(y_online, x_online, color='orange')
ax1.set_title('Preferencias de los residentes chinos para el entretenimiento en línea de noche en 2023', fontsize=12)
# Agregar etiquetas numéricas
for i, val in enumerate(x_online):
    ax1.text(val + 1, i, f'{val}%', ha='left', va='center', color='orange')
# Dibujar la proporción del anillo
anillo_ax1 = plt.Circle((-0.3, -0.3), 0.2, color='white')
ax1.add_artist(anillo_ax1)
ax1.text(-0.3, -0.3, f'{anillo_online}%', ha='center', va='center', fontsize=14, color='orange')
ax1.text(-0.3, -0.5, 'Entretenimiento en línea', ha='center', va='center', fontsize=12)

# --------------------- Dibujar el gráfico de barras horizontales de entretenimiento fuera de línea a la derecha ---------------------
x_offline = list(datos_offline.values())
y_offline = list(datos_offline.keys())
ax2.barh(y_offline, x_offline, color='gold')
ax2.set_title('Preferencias de los residentes chinos para el \nentretenimiento fuera de línea de noche en 2023', fontsize=12)
# Agregar etiquetas numéricas
for i, val in enumerate(x_offline):
    ax2.text(val + 1, i, f'{val}%', ha='left', va='center', color='gold')
# Dibujar la proporción del anillo
anillo_ax2 = plt.Circle((-0.3, -0.3), 0.2, color='white')
ax2.add_artist(anillo_ax2)
ax2.text(-0.3, -0.3, f'{anillo_offline}%', ha='center', va='center', fontsize=14, color='gold')
ax2.text(-0.3, -0.5, 'Entretenimiento fuera de línea', ha='center', va='center', fontsize=12)

# Ajustar el diseño
plt.suptitle('Preferencias de los residentes chinos para el entretenimiento en línea y fuera de línea de noche en 2023', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()