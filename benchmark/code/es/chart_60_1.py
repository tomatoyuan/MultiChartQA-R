import matplotlib.pyplot as plt

# Definición de datos
etiquetas = [
    "Usar casi todo el día",
    "Usar solo al mirar objetos lejanos",
    "Usar solo cuando se usen los ojos durante mucho tiempo",
    "Sin patrón fijo, usar cuando se sienta la necesidad"
]
tamaños = [54.1, 15.5, 11.6, 18.9]
colores = ["#a5d6a7", "#81c784", "#4dd0e1", "#ffe082"]

# Crear un lienzo más ancho
fig, ax = plt.subplots(figsize=(12, 6))  # Expandir horizontalmente

# Ajustar la posición del gráfico circular: Mover el punto central hacia la izquierda
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct="%1.1f%%",
    startangle=140,
    colors=colores,
    textprops={
        "fontsize": 10,
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    },
    center=(-0.8, 0)  # Controlar el centro del gráfico circular para moverlo hacia la izquierda
)

# Establecer el título
ax.set_title(
    "Hábitos de uso de gafas de montura entre las personas miopes",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Ajustar el diseño
plt.tight_layout()
plt.show()