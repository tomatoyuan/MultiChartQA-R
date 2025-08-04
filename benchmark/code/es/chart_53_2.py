import matplotlib.pyplot as plt

# -------------------- Definición de Datos --------------------
etiquetas = ["Proteína de suero", "Proteína vegetal y mixta"]
tamaños = [70.4, 29.6]  # Datos de proporción

# -------------------- Esquema de Colores: Tonos Cálidos --------------------
colores = ["#ffb74d", "#e57373"]  # Naranja + Rojo

# -------------------- Crear un Canvas --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- Dibujar un Gráfico de Dona --------------------
segmentos, etiquetas_texto, textos_porcentaje = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct="%1.1f%%",
    startangle=90,
    colors=colores,
    textprops={"fontsize": 12, "color": "#424242"},
    wedgeprops={"linewidth": 2, "edgecolor": "white"}
)

# Agregar un círculo central para crear un efecto "hueco"
circulo_central = plt.Circle((0, 0), 0.4, fc="white")
fig.gca().add_artist(circulo_central)

# Embelezar el texto de los porcentajes
for texto in textos_porcentaje:
    texto.set_color("white")
    texto.set_fontweight("bold")

# -------------------- Agregar un Título --------------------
ax.set_title(
    "Proporción de proteína de suero en el volumen total de ventas de polvos de proteína",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# -------------------- Optimizar el Diseño --------------------
plt.tight_layout()
plt.show()