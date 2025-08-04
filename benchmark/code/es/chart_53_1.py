import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
categorias = [
    "Proteínas en Polvo (General)",
    "Proteínas en Polvo (Con Probiotics)",
    "Calcio, Hierro, Zinc/Calcio, Magnesio/Calcio",
    "Vitaminas/Minerales",
    "Proteínas Enzimáticas",
    "Colágeno",
    "Aceite de Pescado/Aceite de Pescado Omega3",
    "Extracto de Ostra/Mariscos",
    "L - Carnitina",
    "Extracto de Maca",
    "Extracto de Semilla de Uva",
    "DHA/EPA/DPA",
    "Extracto de Natto",
    "Ácido Fólico",
    "Arándano"
]

# Datos simulados (pueden ser reemplazados con valores reales)
valores = [7.4, 5.2, 4.8, 4.5, 4.2, 3.9, 
           3.7, 3.5, 3.2, 3.0, 2.8, 2.6, 
           2.4, 2.2, 2.0]

# Nota especial (correspondiente a "Proteínas en Polvo (General)")
nota_especial = (
    "“Proteínas en Polvo” es uno de los mercados más destacados en la subcategoría de suplementos nutricionales dietéticos\n"
    "bajo la categoría de primer nivel de alimentos saludables/suplementos nutricionales dietéticos."
)

# Configuración de colores (similar al esquema de color verde en la figura original)
color_barra = "#81c784"
color_destacado = "#a5d6a7"  # Color de resaltado (Proteínas en Polvo General)

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 7))

# -------------------- Dibujar un gráfico de barras horizontales --------------------
y = np.arange(len(categorias))

# Resaltar la primera barra (Proteínas en Polvo General)
barras = ax.barh(
    y, 
    valores, 
    color=[color_destacado] + [color_barra]*(len(categorias)-1),
    height=0.6,
    edgecolor="white",
    linewidth=1
)

# Agregar anotaciones numéricas
for barra in barras:
    ancho = barra.get_width()
    ax.text(
        ancho + 0.2,  # Desplazamiento a la derecha
        barra.get_y() + barra.get_height()/2,
        f"{ancho}%",
        va="center",
        fontsize=9,
        fontweight="bold",
        color="#424242"
    )

# Anotación de texto (descripción del lado derecho)
ax.text(
    max(valores) + 1.5,  # Desplazamiento a la derecha
    y[0] - 0.5,  # Desplazamiento hacia arriba
    nota_especial,
    fontsize=9,
    color="#424242",
    linespacing=1.2,
    ha="left",
    bbox=dict(
        facecolor="white", 
        edgecolor=color_barra, 
        boxstyle="round,pad=0.5"
    )
)

# -------------------- Embellir el gráfico --------------------
ax.set_yticks(y)
ax.set_yticklabels(categorias, fontsize=10, color="#424242")
ax.set_xticks([])  # Ocultar las marcas de la escala del eje x

# Ocultar el marco
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Ocultar las marcas de la escala del eje y

# Agregar un título
ax.set_title(
    "Participación del mercado de los submercados en alimentos saludables/suplementos nutricionales dietéticos (Categoría de primer nivel)",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.subplots_adjust(left=0.3, right=0.7, top=0.85, bottom=0.1)

plt.show()