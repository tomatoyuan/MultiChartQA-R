import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
# Meses (simplificado de julio de 2021 a junio de 2022)
meses = [f"2021.{i}" for i in range(7, 13)] + [f"2022.{i}" for i in range(1, 7)]

# Datos simulados (pueden ser reemplazados con valores reales)
indice_proteina = [100, 110, 120, 150, 200, 180, 160, 170, 190, 220, 240, 260]  # Proteína en polvo en general
indice_suero = [90, 95, 100, 130, 160, 140, 130, 140, 160, 180, 200, 220]    # Proteína de suero

# Datos de anotación (correspondientes a puntos de cambio significativos)
anotaciones = {
    "2021.11": "+70.3%",
    "2022.1": "+63.2%",
    "2022.5": "+17.4%",
    "2022.6": "+17.7%"
}

# Configuración de colores (similar al esquema de colores amarillo - verde + azul original)
color_proteina = "#a5d6a7"  # Proteína en polvo en general
color_suero = "#81d4fa"     # Proteína de suero

# -------------------- Crear un lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 5))

# -------------------- Dibujar un gráfico de doble línea --------------------
# Proteína en polvo en general
ax.plot(
    meses, 
    indice_proteina, 
    marker="o", 
    color=color_proteina, 
    label="Índice de Rotación de Proteína en Polvo (General)",
    linewidth=2
)

# Proteína de suero
ax.plot(
    meses, 
    indice_suero, 
    marker="o", 
    color=color_suero, 
    label="Índice de Rotación de Proteína de Suero",
    linewidth=2
)

# -------------------- Agregar Anotaciones y Flechas --------------------
for mes, texto in anotaciones.items():
    idx = meses.index(mes)
    # Anotaciones para proteína en polvo en general (flechas verdes)
    if "2021.11" in mes or "2022.5" in mes:
        ax.annotate(
            texto,
            xy=(idx, indice_proteina[idx]),
            xytext=(idx + 0.5, indice_proteina[idx] + 30),
            arrowprops=dict(
                facecolor=color_proteina,
                shrink=0.05,
                width=1,
                headwidth=6
            ),
            fontsize=9,
            fontweight="bold",
            color=color_proteina
        )
    # Anotaciones para proteína de suero (flechas azules)
    else:
        ax.annotate(
            texto,
            xy=(idx, indice_suero[idx]),
            xytext=(idx + 0.5, indice_suero[idx] + 25),
            arrowprops=dict(
                facecolor=color_suero,
                shrink=0.05,
                width=1,
                headwidth=6
            ),
            fontsize=9,
            fontweight="bold",
            color=color_suero
        )

# -------------------- Embellir el Gráfico --------------------
# Establecer el rango del eje y
ax.set_ylim(0, 300)

# Establecer las etiquetas de las marcas del eje x (inclinar para evitar superposiciones)
plt.xticks(rotation=45, ha="right", fontsize=9)

# Establecer la leyenda
ax.legend(
    loc="upper left", 
    fontsize=9, 
    frameon=True, 
    facecolor="white", 
    edgecolor="white"
)

# Ocultar los bordes superior y derecho
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Agregar un título
ax.set_title(
    "Cambios en la Tendencia Mensual de Rotación de Proteína en Polvo (General) y Proteína de Suero",
    fontsize=12,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()

plt.show()