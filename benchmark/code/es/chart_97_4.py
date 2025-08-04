import matplotlib.pyplot as plt
import numpy as np

# Razones para ver el partido (datos simulados, siguiendo la lógica de la imagen original)
razones = [
    "Dar apoyo a tu equipo/jugador favorito", "Se ha convertido en un hábito a largo plazo",
    "Disfrutar del alto nivel de trabajo en equipo", "Brindar entretenimiento y emoción",
    "Admirar las excelentes habilidades de fútbol de los jugadores", "Sentir el espíritu de trabajo duro y lucha",
    "Experimentar la sensación de tensión/estimulación", "Aprender habilidades de fútbol",
    "Querer aliviar el estrés", "Tener temas comunes con las personas de alrededor",
    "El presentador/comentarista es muy interesante", "Matar el tiempo",
    "Ver el partido con amigos/familia"
]
# Porcentajes simulados (se pueden ajustar manteniendo la tendencia)
porcentajes = [81.1, 63.5, 58.9, 56.2, 
               55.3, 44.7, 37.1, 24.9, 
               23.5, 19.6, 10.2, 9.5, 3.7]

# Combinación de colores libre (evitar el verde, usar una combinación de azul y naranja)
colores_barras = ["#4169E1", "#1E90FF", "#87CEFA", "#ADD8E6", 
                  "#FFA07A", "#FF8C00", "#FF6347", "#FF4500", 
                  "#FFD700", "#FFC107", "#DAA520", "#B8860B", "#8B4513"]

# Crear un lienzo
fig, ax = plt.subplots(figsize=(8, 7))  # Ajustar la altura para una lista larga

# Dibujar un gráfico de barras horizontales
y = np.arange(len(razones))
barras = ax.barh(y, porcentajes, color=colores_barras, height=0.6)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.annotate(
        f'{ancho}%', 
        xy=(ancho, barra.get_y() + barra.get_height()/2),
        xytext=(5, 0),  # Desplazamiento de 5px hacia la derecha
        textcoords="offset points",
        ha='left', va='center',
        fontsize=8,
        color='black'
    )

# Configurar los ejes y el título
ax.set_yticks(y)
ax.set_yticklabels(razones, fontsize=9)  # Reducir el tamaño de la fuente para evitar sobrecrowding
ax.set_title("Razones por las que los aficionados chinos de fútbol vieron partidos en 2022", fontsize=14, fontweight="bold", y=1.02)

# Embelezar: Ocultar los bordes + Agregar líneas de cuadrícula horizontales
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.grid(axis='x', linestyle='--', alpha=0.3)  # Agregar líneas de cuadrícula auxiliares

plt.tight_layout()  # Optimizar automáticamente el diseño
plt.show()