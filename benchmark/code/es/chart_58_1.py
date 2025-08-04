import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Parques/Parques de diversiones", "Hoteles", "Agencias de viajes", "Oficinas de turismo"]
datos_24 = [169.2, 89.2, 895.0, 137.1]
datos_25 = [585.6, 70.6, 913.2, 149.1]
tasas_de_crecimiento = ["Año sobre año +246.1%", "Año sobre año -20.9%", "Año sobre año +2.0%", "Año sobre año +8.8%"]

# Colores
color_24 = "#4bb7e6"
color_25 = "#a5d65d"

# Crear un lienzo
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

# ✅ Unificar el valor máximo del eje y (ampliar ligeramente para evitar superposiciones)
y_max = max(max(datos_24), max(datos_25)) + 80

for i in range(4):
    ax = axes[i]
    x = np.arange(2)
    barras = ax.bar(
        x,
        [datos_24[i], datos_25[i]],
        width=0.6,
        color=[color_24, color_25],
        edgecolor='white'
    )

    # Agregar etiquetas de datos (un poco más cerca de la parte superior de la barra)
    for barra in barras:
        altura = barra.get_height()
        ax.text(
            barra.get_x() + barra.get_width()/2,
            altura + 5,
            f'{altura:.1f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    # Agregar tasas de crecimiento (por encima de la parte superior de la barra)
    pico = max(datos_24[i], datos_25[i])
    ax.text(
        0.7,
        pico + 55,
        tasas_de_crecimiento[i],
        ha='center',
        va='bottom',
        fontsize=10,
        color="#333333",
        fontweight='bold'
    )

    # Establecer etiquetas del eje x
    ax.set_xticks(x)
    ax.set_xticklabels(["Semana de las vacaciones del Día del Trabajo en 2024", "Semana de las vacaciones del Día del Trabajo en 2025"], fontsize=9, rotation=15, ha='right')

    # Ocultar los bordes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Establecer el título
    ax.set_title(categorias[i], fontsize=11, fontweight='bold')

    # Establecer el límite superior unificado del eje y
    ax.set_ylim(0, y_max)

# Título general
fig.suptitle(
    "Comparación de AdTracker del índice de inversión en publicidad online para el\n turismo durante las vacaciones del Día del Trabajo (del 1 al 5) en 2024 y 2025",
    fontsize=13,
    fontweight='bold',
    y=1.03
)

# ✅ Ajustar el diseño general para evitar que el título general se vea obscurecido
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Reservar espacio en la parte superior para el título
plt.show()