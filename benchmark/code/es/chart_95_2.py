import matplotlib.pyplot as plt
import numpy as np

# Años
years = [2007, 2009, 2011, 2013, 2015, 2017, 2019]
# Salarios iniciales promedio de diferentes niveles educativos (yuan/mes, datos simulados, cercanos a la tendencia)
especialidad = [1410, 1510, 1856, 2285, 2734, 3185, 3548]
licenciatura = [1788, 2276, 2743, 3278, 3961, 4825, 5417]
maestria = [3469, 3637, 4003, 5461, 6334, 8556, 8778]
doctorado = [3252, 3757, 5118, 8800, 6746, 10774, 13849]

# Configuración de colores (cercana a la figura original)
colores = ["#A4C639", "#87CEEB", "#FFD700", "#FF69B4"]
etiquetas = ["Titulares de diplomas técnicos (yuan/mes)", "Titulares de licenciatura (yuan/mes)", "Titulares de maestría (yuan/mes)", "Titulares de doctorado (yuan/mes)"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de líneas y anotar los datos
for i, (datos, color, etiqueta) in enumerate(zip([especialidad, licenciatura, maestria, doctorado], colores, etiquetas)):
    ax.plot(years, datos, marker='o', color=color, label=etiqueta, linewidth=2)
    # Agregar anotaciones de datos
    for x, y in zip(years, datos):
        ax.annotate(f'{y}',
                    xy=(x, y),
                    xytext=(5, 5),  # Desplazamiento de la posición de la anotación
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color=color)

# Establecer las marcas del eje x
ax.set_xticks(years)
# Establecer el título
ax.set_title("Salarios iniciales promedio de graduados universitarios con diferentes niveles educativos de 2007 a 2019", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend(loc='upper left')

# Embelezar: Ocultar los bordes superior y derecho
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()