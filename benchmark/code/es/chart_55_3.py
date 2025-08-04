import matplotlib.pyplot as plt

# -------------------- Definición de Datos --------------------
etiquetas = ["Hombre", "Mujer"]
tamaños = [63.4, 36.6]  # Proporción (%)
colores = ["#a5d6a7", "#4dd0e1"]  # Configuración de colores (similar a la imagen original)

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(6, 6))

# -------------------- Dibujar un gráfico de donut --------------------
# Núcleo: Establecer el ancho del donut a través de wedgeprops
ax.pie(
    tamaños,
    labels=etiquetas,
    autopct="%1.1f%%",  # Mostrar porcentaje
    startangle=90,      # Ángulo de inicio (colocar la parte de "Hombre" a la derecha)
    colors=colores,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "width": 0.3,    # Ancho del donut (parámetro central)
        "edgecolor": "white",
        "linewidth": 2
    }
)

# -------------------- Agregar texto en el centro --------------------
# Agregar "63.4% de los usuarios de deportes electrónicos son hombres" en el centro del donut
ax.text(
    0, 0, 
    "63.4% de los usuarios de deportes electrónicos son hombres",
    ha="center", 
    va="center",
    fontsize=14,
    color="#424242",
    fontweight="bold"
)

# -------------------- Emprolijar el gráfico --------------------
# Establecer el título
ax.set_title(
    "Distribución de género de los usuarios de deportes electrónicos chinos en 2025",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Optimizar el diseño
plt.tight_layout()

plt.show()