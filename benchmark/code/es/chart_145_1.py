import matplotlib.pyplot as plt
import numpy as np

# --------------------- Datos de distribución de edad ---------------------
etiquetas_edad = ["Menos de 18", "19 - 25", "26 - 30", "31 - 40", "41 - 50", "Más de 51"]
tamaños_edad = [0.0, 13.0, 36.8, 39.9, 8.2, 2.1]
colores_edad = ["#FADBD8", "#F9E79F", "#F5B041", "#F1948A", "#B03A2E", "#8B4513"]

# --------------------- Datos de distribución de área residencial ---------------------
etiquetas_region = ["Ciudades de primer nivel", "Nuevas ciudades de primer nivel", "Ciudades de segundo nivel", "Ciudades de tercer nivel", "Ciudades de cuarto nivel y otras"]
tamaños_region = [27.3, 27.6, 26.9, 12.6, 5.6]
colores_region = ["#FADBD8", "#F9E79F", "#F5B041", "#F1948A", "#8B4513"]

# --------------------- Datos de distribución de género ---------------------
etiquetas_genero = ["Hombre", "Mujer"]
tamaños_genero = [36.8, 63.2]
colores_genero = ["#F9E79F", "#F1948A"]

# Crear un lienzo con un diseño de 1x3
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# --------------------- Dibujar el gráfico circular de distribución de edad (gráfico de la izquierda) ---------------------
wedges1, texts1, autotexts1 = ax1.pie(tamaños_edad, colors=colores_edad, autopct='%1.1f%%', startangle=90)
ax1.set_title('Distribución de edad de los consumidores de productos \nculturales y creativos chinos en 2023')
ax1.legend(wedges1, etiquetas_edad, title="Rango de edad", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de la anotación
for autotext in autotexts1:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el gráfico circular de distribución de área residencial (gráfico del centro) ---------------------
wedges2, texts2, autotexts2 = ax2.pie(tamaños_region, colors=colores_region, autopct='%1.1f%%', startangle=90)
ax2.set_title('Distribución de área residencial de los consumidores de \nproductos culturales y creativos chinos en 2023')
ax2.legend(wedges2, etiquetas_region, title="Tipo de región", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de la anotación
for autotext in autotexts2:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Dibujar el gráfico circular de distribución de género (gráfico de la derecha) ---------------------
wedges3, texts3, autotexts3 = ax3.pie(tamaños_genero, colors=colores_genero, autopct='%1.1f%%', startangle=90)
ax3.set_title('Distribución de género de los consumidores de productos \nculturales y creativos chinos en 2023')
ax3.legend(wedges3, etiquetas_genero, title="Género", loc="center left", bbox_to_anchor=(1, 0.5))
# Ajustar el color del texto de la anotación
for autotext in autotexts3:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()