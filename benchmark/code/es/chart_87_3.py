import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# -------------------- Preparación de datos --------------------
razones = [
    "Asesoramiento del médico", "Quieren probar otros métodos primero", 
    "Personalmente piensan que no es necesario usar gafas", "El niño no quiere usar gafas", "Otros"
]
porcentajes = [41.2, 36.5, 14.4, 7.9, 0.1]

# División de ángulos en coordenadas polares (un ángulo por cada categoría)
angulos = np.linspace(0, 2 * np.pi, len(razones), endpoint=False)
# Convertir datos a matriz numpy
datos = np.array(porcentajes)

# Establecer gradiente de colores
cmap = cm.get_cmap("autumn_r")  # Gradiente de naranja a rojo
colores = [cmap(i / len(datos)) for i in range(len(datos))]

# -------------------- Crear gráfico polar --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Establecer ángulo de inicio y dirección de disposición
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Dibujar gráfico de barras polar
barras = ax.bar(angulos, datos, width=0.5, color=colores, edgecolor="white", linewidth=1)

# Agregar etiquetas de datos
for i, (barra, porcentaje) in enumerate(zip(barras, datos)):
    angulo = angulos[i]
    ax.text(
        angulo, barra.get_height(),
        f"{porcentaje}%",
        ha='center', va='bottom',
        fontsize=10, fontweight="bold",
        color="#424242"
    )

# Agregar etiquetas (categorías)
ax.set_xticks(angulos)
ax.set_xticklabels(razones, fontsize=10, color="#333333")

# Quitar eje polar y marcas de graduación
ax.set_yticklabels([])
ax.spines["polar"].set_visible(False)
ax.grid(False)

# Agregar título
ax.set_title("Razones para no obtener gafas inmediatamente o no tenerlas aún", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.show()