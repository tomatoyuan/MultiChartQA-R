import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
# Datos del gráfico de pastel
etiquetas_pastel = ["Un par", "Otros"]
tamaños_pastel = [53.2, 46.8]
colores_pastel = ["#dcdcdc", "#a5d6a7"]  # Gris, verde claro

# Datos del gráfico de barras anidadas (división de la categoría "Otros")
etiquetas_barras = ["Dos pares", "Tres pares o más"]
tamaños_barras = [42.7, 4.1]  # Nota: 42.7 + 4.1 = 46.8, coincide con la proporción de "Otros" en el gráfico de pastel
colores_barras = ["#a5d6a7", "#81c784"]  # Verde claro, verde oscuro

# -------------------- Crear el lienzo --------------------
fig, (ax_pastel, ax_barras) = plt.subplots(1, 2, figsize=(8, 5), gridspec_kw={"width_ratios": [1, 2]})

# -------------------- Dibujar el gráfico de pastel --------------------
wedges, textos, textos_automaticos = ax_pastel.pie(
    tamaños_pastel,
    labels=etiquetas_pastel,
    autopct="%1.1f%%",  # Mostrar porcentajes
    startangle=90,      # Ángulo de inicio (colocar la parte de "Un par" a la izquierda)
    colors=colores_pastel,
    textprops={
        "fontsize": 10, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    }
)

# Ajustar la posición del texto del gráfico de pastel (evitar superposición)
for texto, auto in zip(textos, textos_automaticos):
    texto.set_fontsize(10)
    auto.set_fontsize(10)

# -------------------- Dibujar el gráfico de barras anidadas --------------------
x = np.arange(len(etiquetas_barras))
ancho_barra = 0.6

ax_barras.bar(
    x, 
    tamaños_barras, 
    width=ancho_barra, 
    color=colores_barras,
    edgecolor="white",
    linewidth=1
)

# Agregar etiquetas de datos
for i, valor in enumerate(tamaños_barras):
    ax_barras.text(
        i, valor + 1, 
        f"{valor}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Embelezar el gráfico --------------------
# Optimización del gráfico de pastel
ax_pastel.set_aspect("equal")  # Asegurar que el gráfico de pastel sea un círculo perfecto
ax_pastel.spines["top"].set_visible(False)
ax_pastel.spines["right"].set_visible(False)

# Optimización del gráfico de barras
ax_barras.set_xticks(x)
ax_barras.set_xticklabels(etiquetas_barras, fontsize=10, color="#424242")
ax_barras.set_ylim(0, 50)  # El rango del eje y coincide con los datos
ax_barras.spines["top"].set_visible(False)
ax_barras.spines["right"].set_visible(False)

# Agregar un título
fig.suptitle(
    "Distribución del número de gafas de marco que poseen las personas miopes",
    fontsize=14,
    fontweight="bold",
    y=1.05  # Posición del título
)

# Ajustar el diseño
plt.tight_layout()

plt.show()