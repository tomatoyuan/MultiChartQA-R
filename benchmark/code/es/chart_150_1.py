import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
# Proporción de cada tipo de ciudad en el servicio presencial en tienda (suponiendo que de izquierda a derecha corresponden a ciudades de primer nivel, ciudades de nuevo primer nivel, ciudades de segundo nivel y ciudades de tercer nivel y por debajo, juiciado visualmente desde el gráfico de barras)
servicio_en_tienda = [28.1, 32.4, 31.4, 8.1]
# Proporción de cada tipo de ciudad en el servicio de entrega a domicilio (de manera similar correspondiente)
servicio_entrega_domicilio = [23.0, 32.9, 35.9, 8.2]

# Etiquetas de los tipos de ciudad (inferidas del número de barras en el gráfico de barras)
tipos_ciudad = ["Ciudades de primer nivel", "Ciudades de nuevo primer nivel", "Ciudades de segundo nivel", "Ciudades de tercer nivel y por debajo"]
x = np.arange(len(tipos_ciudad))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))

# Dibujar el gráfico de barras para el servicio presencial en tienda (serie amarilla)
ancho_barra = 0.35
ax.bar(x - ancho_barra/2, servicio_en_tienda, width=ancho_barra, color=['gold', 'peru', 'coral', 'lightpink'], label='Servicio presencial en tienda')
# Dibujar el gráfico de barras para el servicio de entrega a domicilio (serie naranja)
ax.bar(x + ancho_barra/2, servicio_entrega_domicilio, width=ancho_barra, color=['orange', 'darkorange', 'tomato', 'lightcoral'], label='Servicio de entrega a domicilio')

ax.set_title('Encuesta sobre la voluntad de consumo de usuarios de Internet en ciudades chinas de diferentes niveles para productos de servicios de vida local en 2023', fontsize=14)
ax.set_ylabel('Proporción de voluntad de consumo (%)')
ax.set_xticks(x)
ax.set_xticklabels(tipos_ciudad)
ax.legend()

# Agregar etiquetas de valor para el servicio presencial en tienda
for i, val in enumerate(servicio_en_tienda):
    ax.text(x[i] - ancho_barra/2, val + 1, f'{val}%', ha='center', va='bottom', color='black')

# Agregar etiquetas de valor para el servicio de entrega a domicilio
for i, val in enumerate(servicio_entrega_domicilio):
    ax.text(x[i] + ancho_barra/2, val + 1, f'{val}%', ha='center', va='bottom', color='black')

plt.tight_layout()
plt.show()