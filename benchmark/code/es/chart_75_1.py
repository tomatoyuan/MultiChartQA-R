import matplotlib.pyplot as plt
import numpy as np

# Nombres de los países
paises = [
    "Unión Europea", "Estados Unidos", "Japón", "Rusia", "Canadá", "Corea del Sur",
    "Argelia", "Australia", "Turquía", "Ucrania", "Arabia Saudita", "Suiza",
    "Brasil", "Indonesia", "Etiopía", "Filipinas", "Vietnam", "México",
    "Colombia", "India", "Tailandia", "Venezuela"
]
# Consumo de café en países importadores de café (miles de sacos), los datos pueden ser aproximadamente iguales
consumo_importacion = [40251, 26982, 7386, 4681, 4011, 2513,
                      2131, 1962, 1754, 1379, 1253, 1074,
                      0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0]
# Consumo de café en países exportadores de café (miles de sacos), los datos pueden ser aproximadamente iguales
consumo_exportacion = [0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0,
                      22400, 5000, 3798, 3312, 2700, 2420,
                      2045, 1485, 1415, 1100]

# Configuración de la posición para los gráficos de barras agrupados
x = np.arange(len(paises))
ancho_barra = 0.35

# Crear un lienzo y subgráficos
fig, ax = plt.subplots(figsize=(10, 8))

# Dibujar el gráfico de barras para el consumo de café en países importadores de café
barras_importacion = ax.barh(x - ancho_barra/2, consumo_importacion, height=ancho_barra, 
                      color="#C6C439", label="Consumo de granos verdes de café en países importadores de café (miles de sacos)")
# Dibujar el gráfico de barras para el consumo de café en países exportadores de café
barras_exportacion = ax.barh(x + ancho_barra/2, consumo_exportacion, height=ancho_barra, 
                      color="#AD64F6", label="Consumo de granos verdes de café en países exportadores de café (miles de sacos)")

# Agregar etiquetas de datos para el consumo en países importadores
for barra in barras_importacion:
    ancho = barra.get_width()
    if ancho > 0:
        ax.annotate(f'{ancho}',
                    xy=(ancho, barra.get_y() + barra.get_height() / 2),
                    xytext=(5, 0),  # Ajustar la posición de la etiqueta
                    textcoords="offset points",
                    ha='left', va='center')

# Agregar etiquetas de datos para el consumo en países exportadores
for barra in barras_exportacion:
    ancho = barra.get_width()
    if ancho > 0:
        ax.annotate(f'{ancho}',
                    xy=(ancho, barra.get_y() + barra.get_height() / 2),
                    xytext=(5, 0),  # Ajustar la posición de la etiqueta
                    textcoords="offset points",
                    ha='left', va='center')

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(x)
ax.set_yticklabels(paises)
# Establecer la etiqueta del eje x
ax.set_xlabel("Consumo (miles de sacos)")
# Establecer el título
ax.set_title("Consumo global de granos verdes de café en los principales países en 2020", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Emprolijar el gráfico, ocultar los bordes superior, derecho e inferior
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()