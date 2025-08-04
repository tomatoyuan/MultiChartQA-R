import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["Ignorar las presiones para casarse", "Otras actitudes"]
sizes = [50, 50]
colors = ["#FF6B6B", "#4ECDC4"]  # Usar un esquema de colores más moderno
explode = (0.05, 0)  # Resaltar la primera parte

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Dibujar el gráfico circular anular
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)} personas)' if p > 0 else '',
    startangle=90,
    colors=colors,
    wedgeprops={"width": 0.4, "edgecolor": "w", "linewidth": 2},
    textprops={"fontsize": 12, "color": "#333333"},
)

# Establecer el título
ax.set_title("Distribución de actitudes de los encuestados \nfrente a las presiones para casarse", fontsize=16, fontweight="bold", pad=20)

# Ajustar la leyenda
ax.legend(wedges, labels, title="Tipos de actitudes", loc="center left", bbox_to_anchor=(1, 0.3, 0.5, 1))

# Añadir estilo a las etiquetas de datos
for autotext in autotexts:
    autotext.set_fontweight("bold")

# Configuración de fondo y cuadrícula
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Establecer la proporción de los ejes
plt.axis('equal')

# Añadir una nota explicativa
plt.figtext(0.5, 0.01, "Fuente de datos: Ejemplo ficticio", ha="center", fontsize=9, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

# Ajustar el diseño
plt.tight_layout()

# Guardar el gráfico (opcional)
# plt.savefig('marriage_pressure_attitude.png', bbox_inches='tight', dpi=300)

# Mostrar el gráfico
plt.show()