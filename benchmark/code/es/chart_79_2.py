import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ["Bebo de pescado", "Holoturia", "Patas de cerdo", "Nido de aves"]
# Contenido de colágeno (%); los datos pueden ser aproximadamente iguales
contenido_colageno = [84.0, 54.2, 11.1, 1.5]

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(6, 5))

# Dibujar un gráfico de barras
x = np.arange(len(categorias))
ancho_barra = 0.6
barras = ax.bar(x, contenido_colageno, width=ancho_barra, color="#A4C639", label="Contenido de colágeno (%)")

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),  # Ajustar la posición de la etiqueta
                textcoords="offset points",
                ha='center', va='bottom')

# Agregar texto explicativo en la parte inferior
ax.text(0.5, -0.25, "● El contenido de colágeno es más de 7 veces el de las patas de cerdo", 
        ha='center', va='bottom', fontsize=10, color='green')

# Establecer las marcas y etiquetas del eje x
ax.set_xticks(x)
ax.set_xticklabels(categorias)
# Establecer la etiqueta del eje y
ax.set_ylabel("Contenido de colágeno (%)")
# Establecer el título
ax.set_title("Contenido de colágeno en el bebo de pescado", fontsize=14, fontweight="bold")

# Agregar una leyenda
ax.legend()

# Embelezar el gráfico ocultando los bordes superior y derecho
for espina in ["top", "right"]:
    ax.spines[espina].set_visible(False)

plt.tight_layout()  # Ajustar automáticamente el diseño
plt.show()