import matplotlib.pyplot as plt
import numpy as np

# Organización de datos (agrupados por categoría, cada categoría contiene la proporción de cada nivel de ciudades)
categorias = [
    "Paquetes de alimentos y bebidas", "Ocio y entretenimiento", "Alojamiento en hoteles", "Entradas turísticas",
    "Viajes y transporte", "Servicios de vida", "Belleza y cuidado de la piel", "Capacitación y consultoría"
]
# Proporciones (%) de ciudades de primer nivel, ciudades de nuevo primer nivel, ciudades de segundo y tercer nivel y ciudades de cuarto y quinto nivel en cada categoría
datos = {
    "Paquetes de alimentos y bebidas": [61.8, 59.9, 72.4, 69.2],
    "Ocio y entretenimiento": [56.6, 57.3, 58.6, 43.6],
    "Alojamiento en hoteles": [42.6, 41.4, 30.9, 35.9],
    "Entradas turísticas": [39.7, 49.7, 47.4, 20.5],
    "Viajes y transporte": [39.0, 40.8, 42.1, 48.7],
    "Servicios de vida": [36.8, 42.0, 48.7, 48.7],
    "Belleza y cuidado de la piel": [31.6, 35.7, 33.6, 23.1],
    "Capacitación y consultoría": [22.9, 21.3, 23.0, 15.4]
}
# Colores correspondientes a cada nivel de ciudades (consistentes con la leyenda)
colores = ['coral', 'sandybrown', 'lightpink', 'gold']
# Etiquetas para cada nivel de ciudades
etiquetas_ciudades = ["Ciudades de primer nivel", "Ciudades de nuevo primer nivel", "Ciudades de segundo y tercer nivel", "Ciudades de cuarto y quinto nivel"]

x = np.arange(len(categorias))  # Coordenadas del eje x (una posición para cada categoría)
ancho_barra = 0.2  # Ancho de cada barra de tipo de ciudad

fig, ax = plt.subplots(figsize=(16, 8))

# Bucle para dibujar las barras de cada tipo de ciudad
for i in range(4):
    ax.bar(
        x + i * ancho_barra,  # Controlar la posición en el eje x de las barras para lograr el agrupamiento
        [datos[cat][i] for cat in categorias],  # Tomar la proporción del i - ésimo tipo de ciudad en cada categoría
        width=ancho_barra,
        color=colores[i],
        label=etiquetas_ciudades[i]
    )

ax.set_title('Encuesta de categorías de consumo de usuarios de servicios presenciales en ciudades chinas de diferentes niveles en 2023', fontsize=14)
ax.set_ylabel('Proporción de consumo (%)')
ax.set_xlabel('Categorías de consumo')
ax.set_xticks(x + ancho_barra * 1.5)  # Ajustar la posición de las marcas del eje x para colocar las etiquetas en el centro de los grupos
ax.set_xticklabels(categorias)
ax.legend(title='Tipos de ciudades', loc='upper right')

# Agregar anotaciones numéricas
for i in range(len(categorias)):
    for j in range(4):
        valor = datos[categorias[i]][j]
        ax.text(
            x[i] + j * ancho_barra,
            valor + 1,
            f'{valor}%',
            ha='center',
            va='bottom',
            color='black',
            fontsize=9
        )

plt.tight_layout()
plt.show()