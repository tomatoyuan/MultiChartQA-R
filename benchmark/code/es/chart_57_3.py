import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de datos --------------------
regiones = [
    "Estados Unidos", "Brasil", "India", "Indonesia",
    "Reino Unido", "Japón", "España", "Alemania",
    "Italia", "Francia"
]
porcentajes = [22.7, 14.5, 6.7, 3.7, 3.4, 2.8, 2.4, 2.0, 2.0, 2.0]

# Cerrar los datos
valores = porcentajes + [porcentajes[0]]
angulos = np.linspace(0, 2 * np.pi, len(valores), endpoint=True)

# -------------------- Crear el lienzo --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# -------------------- Dibujar el gráfico de radar --------------------
ax.plot(angulos, valores, color="#ab47bc", linewidth=2)
ax.fill(angulos, valores, color="#ce93d8", alpha=0.4)

# -------------------- Configurar las etiquetas de las coordenadas --------------------
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(regiones, fontsize=10, color="#424242")

# -------------------- Configurar el rango del eje polar --------------------
ax.set_rlabel_position(30)
ax.set_yticks([2.5, 5, 10, 15, 20, 25])
ax.set_yticklabels(["2.5%", "5%", "10%", "15%", "20%", "25%"], color="#757575", fontsize=9)
ax.set_ylim(0, 25)

# -------------------- Agregar anotaciones de valores (Método 3: Ajustar la posición) --------------------
for i, val in enumerate(porcentajes):
    angulo = angulos[i]
    x = angulo
    y = val + 2  # Desplazamiento hacia afuera
    ha = "left" if np.pi/2 < angulo < 3*np.pi/2 else "right"
    ax.text(
        x, y, f"{val}%",
        fontsize=9,
        ha=ha,
        va="center",
        color="#424242",
        fontweight="bold",
        rotation_mode="anchor"
    )

# -------------------- Agregar la leyenda --------------------
import matplotlib.patches as mpatches
patch = mpatches.Patch(color="#ab47bc", label="Porcentaje de cada región")
ax.legend(handles=[patch], loc="center left", bbox_to_anchor=(1.3, 1.1), fontsize=10)

# -------------------- Agregar el título --------------------
ax.set_title(
    "Distribución de la cantidad de publicaciones de marketing \nde influencers en diferentes regiones globales (Gráfico de radar)",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# -------------------- Mostrar el gráfico --------------------
plt.tight_layout()
plt.show()