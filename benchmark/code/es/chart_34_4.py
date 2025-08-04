import matplotlib.pyplot as plt
import numpy as np

# Datos
data = [1, 1, 1, 1, 0.4]  # Simular la proporción de cada intervalo, la suma corresponde al promedio de 2.4 escenarios, se puede ajustar según la situación real
labels = ["1 escenario", "2 escenarios", "3 escenarios", "4 escenarios", "5 escenarios"]
colors = ["#4CAF50", "#FFC107", "#F44336", "#9C27B0", "#607D8B"]  # Simular colores similares

# Dibujar un gráfico de donut
fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    data,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",  # Mostrar porcentajes
    startangle=90,
    pctdistance=0.85,  # La distancia de la etiqueta de porcentaje desde el centro del círculo
    wedgeprops={"width": 0.3, "edgecolor": "white"}  # Establecer el ancho y el color del borde del anillo
)

# Agregar texto en el centro para mostrar el número promedio de escenarios
ax.text(
    0,
    0,
    "Promedio\n2.4 escenarios",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold"
)

# Agregar una leyenda codificada por colores a la derecha
text_descriptions = [
    "Desplazamiento Diario",
    "Ropa de Moda",
    "Entrenamiento de Alta Energía",
    "Actividades al Aire Libre en la Montaña",
    "Relajación en Casa"
]

# Calcular las coordenadas verticales para la visualización del texto para distribuir el texto de manera uniforme
y_positions = np.linspace(0.8, -0.8, len(text_descriptions))
for i, (desc, color) in enumerate(zip(text_descriptions, colors)):
    # Agregar marcadores de color
    ax.scatter(
        1.2,  # Posición en el eje x (ligeramente desplazada a la izquierda para dejar espacio para el marcador)
        y_positions[i],
        s=50,  # Tamaño del marcador
        color=color,  # Usar el color correspondiente
        zorder=3  # Asegurarse de que el marcador se muestre en la parte superior
    )
    # Agregar descripciones de texto
    ax.text(
        1.35,  # Posición de inicio del texto (desplazada a la derecha para evitar superposiciones)
        y_positions[i],
        desc,
        fontsize=12,
        ha="left",
        va="center"
    )

# Agregar un título
plt.title("Distribución de Uso de Escenarios de Usuario", fontsize=16, fontweight="bold", pad=20)

# Ajustar el diseño para evitar la superposición de elementos (ampliar ligeramente el espacio a la derecha)
plt.subplots_adjust(right=0.75, top=0.85)

# Mostrar el gráfico
plt.show()