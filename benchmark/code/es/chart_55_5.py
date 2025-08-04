import matplotlib.pyplot as plt
import numpy as np

# -------------------- Definición de Datos --------------------
grupos_ingresos = [
    "Por debajo de 4000 yuan", "De 4001 a 6000 yuan", "De 6001 a 8000 yuan",
    "De 8001 a 10000 yuan", "De 10001 a 15000 yuan", "Por encima de 15000 yuan"
]
porcentajes = [4.6, 18.3, 26.5, 21.2, 18.9, 10.4]

# -------------------- Configuración de Coordenadas Polares --------------------
N = len(porcentajes)
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radios = porcentajes
ancho = 2 * np.pi / N * 0.9  # Ancho angular de cada sector

# Esquema de colores degradados (Rojo → Naranja → Amarillo → Verde → Azul → Morado)
colores = ["#e57373", "#ffb74d", "#fff176", "#81c784", "#64b5f6", "#ba68c8"]

# -------------------- Crear el lienzo de coordenadas polares --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
barras = ax.bar(theta, radios, width=ancho, color=colores, edgecolor="white", linewidth=1, align="edge")

# -------------------- Agregar Etiquetas --------------------
for i, (angulo, radio) in enumerate(zip(theta, radios)):
    ax.text(
        angulo + ancho / 2, radio + 2, 
        f"{grupos_ingresos[i]}\n{radio}%", 
        ha="center", va="center",
        fontsize=10, fontweight="bold", color="#424242", rotation_mode='anchor'
    )

# -------------------- Embellir el Gráfico --------------------
ax.set_theta_zero_location('N')   # Establecer el punto de partida en la parte superior
ax.set_theta_direction(-1)        # Dirección en el sentido de las agujas del reloj
ax.set_rticks([])                 # No mostrar la escala radial
ax.set_yticklabels([])            # No mostrar etiquetas radiales
ax.spines["polar"].set_visible(False)  # Quitar el borde de las coordenadas polares

# Agregar título
plt.title(
    "Nivel de ingresos mensuales personales de los usuarios chinos de e - sports en 2025",
    fontsize=14, fontweight="bold", pad=20
)

plt.tight_layout()
plt.show()