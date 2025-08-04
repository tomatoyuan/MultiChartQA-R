import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# -------------------- Definición de Datos --------------------
categorias = [
    "Problemas de inmunidad",
    "Problemas de crecimiento y desarrollo",
    "Fortalecer huesos / Promover el desarrollo óseo",
    "Problemas de visión",
    "Promover la digestión gastrointestinal",
    "Concentración"
]
porcentajes = [76.0, 63.8, 63.3, 61.2, 48.0, 39.8]

# -------------------- Mapeo de Ángulos y Colores --------------------
N = len(categorias)
angulos = np.linspace(0, 2 * np.pi, N, endpoint=False)
colores = cm.get_cmap("viridis")(mcolors.Normalize()(porcentajes))  # Puede ser reemplazado con 'coolwarm', 'viridis', etc.

# -------------------- Crear Canvas (Coordenadas Polares) --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))
barras = ax.bar(
    angulos,
    porcentajes,
    width=2*np.pi/N * 0.8,  # Controlar el ancho
    color=colores,
    edgecolor="white",
    linewidth=1
)

# -------------------- Agregar Anotaciones --------------------
for angulo, altura in zip(angulos, porcentajes):
    ax.text(
        angulo,
        altura - 7,  # Desplazamiento fuera del arco
        f"{altura:.1f}%",
        ha='center', va='center',
        fontsize=10,
        color="black",
        fontweight="bold"
    )

# -------------------- Establecer Etiquetas de Categorías (Colocar alrededor del círculo) --------------------
ax.set_xticks(angulos)
ax.set_xticklabels(categorias, fontsize=9, color="#333333")

# Ocultar las líneas de radio y escalas predeterminadas de las coordenadas polares
ax.set_yticklabels([])
ax.set_yticks([])
ax.spines["polar"].set_visible(False)

# Agregar un título
plt.title("Preocupaciones de salud para niños de 4 - 6 años (%)", fontsize=14, fontweight="bold", pad=30)

plt.tight_layout()
plt.show()