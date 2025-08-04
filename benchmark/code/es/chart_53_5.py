import matplotlib.pyplot as plt

# -------------------- Definición de Datos --------------------
etiquetas = ["Secundaria o inferior", "Licenciatura o superior", "Carrera técnica"]
tamaños = [60.2, 27.1, 12.7]  # Proporción (%)
tgis = [76, 218, 156]       # Valor TGI

# Configuración de colores (similar al esquema de colores de la imagen original)
colores = ["#a5d6a7", "#81d4fa", "#c8e6c9"]

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6))  # Aumentar el ancho de la figura para un mejor diseño

# -------------------- Dibujar un gráfico de pastel --------------------
porciones, etiquetas_texto, textos_automaticos = ax.pie(
    tamaños,
    labels=None,  # Quitar etiquetas del gráfico de pastel (se agregarán a la leyenda en su lugar)
    autopct="%1.1f%%",  # Mostrar porcentaje
    startangle=90,      # Ángulo de inicio (colocar "Secundaria o inferior" a la derecha)
    colors=colores,
    textprops={
        "fontsize": 12, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "linewidth": 2, 
        "edgecolor": "white"
    }
)

# -------------------- Embelezar el gráfico --------------------
# Establecer el título
ax.set_title(
    "Proteínas en polvo en general: Nivel educativo",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar la posición de la leyenda a la izquierda y fuera del gráfico
ax.legend(
    etiquetas,  # Agregar etiquetas a la leyenda
    loc="center left",  # Posicionar la leyenda a la izquierda
    bbox_to_anchor=(-0.35, 0.5),  # Ajustar la posición (mover más a la izquierda)
    fontsize=10, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white",
    framealpha=1.0,  # Hacer el fondo de la leyenda opaco
    handlelength=1.5,  # Ajustar la longitud del marcador de la leyenda
    handleheight=1.5   # Ajustar la altura del marcador de la leyenda
)

# Optimizar el diseño
plt.tight_layout(rect=[0, 0, 0.9, 1])  # Ajustar el diseño para dejar espacio para la leyenda

plt.show()