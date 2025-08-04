import matplotlib.pyplot as plt
import numpy as np

# -------------------- Organización de datos --------------------
# Datos TGI extraídos del gráfico (correspondientes a tres grupos por fila)
datos = {
    "Primaria (7 - 11 años)": [109, 102, 105, 111, 95, 107, 104, 102, 93, 79, 89, 78, 95, 69, 24],
    "Secundaria (12 - 14 años)": [103, 98, 109, 84, 128, 107, 92, 102, 112, 123, 164, 121, 152, 111, 109],
    "Bachillerato (15 - 17 años)": [96, 87, 98, 92, 95, 88, 94, 98, 95, 105, 107, 106, 124, 99, 135, 212]
}

# Asegurarse de que las longitudes de los tres grupos de datos sean iguales (rellenar valores faltantes, debe ajustarse según los datos originales en la práctica)
long_max = max(len(v) for v in datos.values())
for clave in datos:
    if len(datos[clave]) < long_max:
        datos[clave] += [np.nan] * (long_max - len(datos[clave]))

# Etiquetas de grupo (posiciones en el eje x)
x = np.arange(long_max)

# Configuración de colores (verde claro similar a la imagen original)
colores = ["#a5d6a7", "#c8e6c9", "#e8f5e9"]

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(10, 6))

# -------------------- Dibujar el gráfico de barras agrupadas --------------------
ancho_barra = 0.25  # Ancho de cada grupo de barras

for i, (grupo, valores) in enumerate(datos.items()):
    ax.bar(
        x + i * ancho_barra,
        valores,
        width=ancho_barra,
        color=colores[i],
        label=grupo,
        edgecolor="white",
        linewidth=1
    )

# -------------------- Agregar etiquetas de datos --------------------
for i, (grupo, valores) in enumerate(datos.items()):
    for j, val in enumerate(valores):
        if not np.isnan(val):
            ax.text(
                x[j] + i * ancho_barra,
                val + 2,  # Desplazamiento hacia arriba
                f"{val}",
                ha="center",
                fontsize=8,
                color="#424242",
                fontweight="bold"
            )

# -------------------- Embelezar el gráfico --------------------
# Establecer las marcas del eje x (ocultarlas porque es una comparación categórica)
ax.set_xticks([])

# Establecer el rango del eje y
ax.set_ylim(0, 220)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar una leyenda
ax.legend(
    loc="upper left",
    fontsize=9,
    frameon=True,
    facecolor="white",
    edgecolor="white"
)

# Agregar un título
ax.set_title(
    "Comparación de datos TGI para adolescentes de diferentes edades",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()