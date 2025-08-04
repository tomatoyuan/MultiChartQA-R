import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Presión frecuente para casarse", "Ocho citas a ciegas en un día durante la Fiesta de Primavera", "A menudo apurarse a citas a ciegas"]
tamaños = [70, 54.7, 30]
x = np.arange(len(etiquetas))  # Posiciones en el eje x

# Crear una figura y un subgráfico, establecer el tamaño
fig, ax = plt.subplots(figsize=(10, 6))

# Crear una lista de colores degradados
colores = plt.cm.RdPu(np.linspace(0.6, 0.9, len(tamaños)))  # Usar los colores degradados de la paleta de colores RdPu

# Dibujar un gráfico de barras con sombra y bordes
rectangulos = ax.bar(
    x, 
    tamaños, 
    width=0.6, 
    color=colores, 
    edgecolor='black', 
    linewidth=1.2,
    alpha=0.8,
    zorder=3  # Asegurarse de que el gráfico de barras se muestre por encima de las líneas de la cuadrícula
)

# Establecer las marcas y etiquetas del eje x, aumentar el ángulo de rotación y el tamaño de fuente
ax.set_xticks(x)
ax.set_xticklabels(etiquetas, rotation=30, ha='right', fontsize=12)

# Agregar etiquetas numéricas, aumentar el tamaño de fuente y agregar un cuadro de fondo
for rectangulo in rectangulos:
    altura = rectangulo.get_height()
    ax.annotate(
        f"{altura}%", 
        xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
        xytext=(0, 5),  # Desplazamiento de 5 puntos hacia arriba
        textcoords="offset points",
        ha="center", 
        va="bottom",
        fontsize=12,
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.7)
    )

# Agregar un título y una etiqueta para el eje y, aumentar el tamaño de fuente y el estilo
ax.set_ylabel("Porcentaje (%)", fontsize=14)
ax.set_title("Datos de encuesta sobre la presión en el matrimonio y el amor de hombres y mujeres solteros entrevistados", fontsize=16, fontweight='bold', pad=20)

# Agregar líneas de cuadrícula, establecer la transparencia
ax.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)  # Establecer las líneas de la cuadrícula en la capa inferior

# Establecer el rango del eje y
ax.set_ylim(0, max(tamaños) * 1.1)  # Expandir ligeramente el rango del eje y

# Agregar una leyenda
ax.legend([rectangulos[0]], ["Datos de porcentaje"], loc='upper right')

# Agregar un color de fondo
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f1f3f5')

# Ajustar el diseño
plt.tight_layout()

# Guardar el gráfico (opcional)
# plt.savefig('dating_pressure_chart.png', dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()