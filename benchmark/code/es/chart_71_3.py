import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ["Gasto de consumo deportivo per cápita de los residentes", "Gasto de consumo deportivo per cápita de los adultos", "Gasto de consumo deportivo per cápita de las personas mayores"]
# Datos en 2014 (Yuan), los datos pueden ser aproximadamente los mismos
datos_2014 = [926.0, 968.4, 504.0]
# Datos en 2020 (Yuan), los datos pueden ser aproximadamente los mismos
datos_2020 = [1330.4, 1758.2, 1092.2]

# Ancho de la barra
ancho_barra = 0.35
# Configuración de colores, similares al verde y azul de la figura original
colores = ["#A4C639", "#64B5F6"]

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar el gráfico de barras para los datos de 2014
x = np.arange(len(categorias))
barra_2014 = ax.bar(x - ancho_barra/2, datos_2014, width=ancho_barra, color=colores[0], label="2014 (Yuan)")
# Dibujar el gráfico de barras para los datos de 2020
barra_2020 = ax.bar(x + ancho_barra/2, datos_2020, width=ancho_barra, color=colores[1], label="2020 (Yuan)")

# Agregar etiquetas de datos para 2014
for barra in barra_2014:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar etiquetas de datos para 2020
for barra in barra_2020:
    altura = barra.get_height()
    ax.annotate(f'{altura}',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la anotación
                textcoords="offset points",
                ha='center', va='bottom')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias, rotation=25)
# Establecer la etiqueta del eje y
ax.set_ylabel("Gasto de consumo (Yuan)")
# Establecer el título
ax.set_title("Gasto de consumo deportivo per cápita en China en 2014 y 2020", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico, ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()