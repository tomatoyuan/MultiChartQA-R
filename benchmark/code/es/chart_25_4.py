import matplotlib.pyplot as plt
import numpy as np

# Datos y etiquetas
etiquetas = ["Teléfono móvil", "Juegos online", "Recoger sobres rojos", "No querer ir a casa", "Otros"]
valores = [0.6, 0.4, 0.3, 0.2, 0.1]  # Proporción simulada, se puede ajustar según la situación real
colores = ["#F5A623"] * len(etiquetas)  # Color principal del termómetro

# Crear un lienzo
fig, ax = plt.subplots(figsize=(6, 4), facecolor="#D52B1E")  # Fondo rojo

# Dibujar un gráfico de barras horizontales (simulando un termómetro)
pos_y = np.arange(len(etiquetas))
barras = ax.barh(
    pos_y,
    valores,
    color=colores,
    edgecolor="white",
    height=0.6,
    left=0.2  # Reservar espacio en blanco para simular el "tubo de vidrio" del termómetro
)

# Simular las líneas de escala blancas del termómetro (superponer barras en blanco)
ax.barh(
    pos_y,
    [1 - v for v in valores],
    color="white",
    edgecolor="white",
    height=0.6,
    left=0.2 + np.array(valores)
)

# Agregar etiquetas numéricas
for i, (valor, etiqueta) in enumerate(zip(valores, etiquetas)):
    # Calcular la posición de la etiqueta (en el centro de la barra)
    pos_x = 0.2 + valor / 2
    ax.text(
        pos_x, i,
        f"{valor:.1f}",
        ha='center', va='center',
        color='white', fontsize=12,
        fontweight='bold'
    )

# Configuraciones de mejora visual
ax.set_yticks(pos_y)
ax.set_yticklabels(etiquetas, fontsize=12, color="gold")  # Texto dorado
ax.set_xticks([])  # Ocultar las marcas del eje x
ax.spines[:].set_visible(False)  # Ocultar el borde

# Agregar un título y un lema
ax.text(
    0.5, 1.1,
    'Los teléfonos móviles son los principales culpables de "matar" el sentido del ritual de la Fiesta de Primavera',
    ha='center', va='top',
    fontsize=14, color='gold',
    transform=ax.transAxes
)
ax.text(
    0.5, -0.15,
    'Deja de usar tu teléfono y pasa tiempo con tu familia.',
    ha='center', va='bottom',
    fontsize=12, color='white',
    transform=ax.transAxes
)

plt.tight_layout()
plt.show()