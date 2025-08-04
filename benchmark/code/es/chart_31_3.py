import matplotlib.pyplot as plt
import numpy as np

# Datos
grupos_edad = ['Menos de 25', '25 - 40', 'Más de 40']
porcentajes = [18, 37, 45]

# Dibujar un gráfico de barras
x = np.arange(len(grupos_edad))
ancho = 0.5

fig, ax = plt.subplots(figsize=(8, 6))
rectangulos = ax.bar(x, porcentajes, ancho, color=['#FF7F50', '#FFD700', '#4B0082'])

# Agregar título y etiquetas
ax.set_title('Top 5 Esquemas Ponzi en Internet - Distribución por Edad de los Incidentes de Esquemas Ponzi en Internet Representados por "Shanxinhui"', fontsize=14, fontweight='bold')
ax.set_xlabel('Grupo de Edad', fontsize=12)
ax.set_ylabel('Proporción de Búsqueda (%)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(grupos_edad)

# Marcar el porcentaje en las barras
for rectangulo in rectangulos:
    altura = rectangulo.get_height()
    ax.annotate(f'{altura}%',
                xy=(rectangulo.get_x() + rectangulo.get_width() / 2, altura),
                xytext=(0, 3),  # Desplazamiento vertical de 3 puntos
                textcoords="offset points",
                ha='center', va='bottom')

# Mostrar información sobre la cantidad de búsquedas relevantes (puede mostrarse en el título o en un cuadro de texto, aquí se muestra un ejemplo con un cuadro de texto)
info_busqueda = f'Cantidad de Búsquedas Relevantes: 322,000'
props = dict(boxstyle='round', facecolor='white', alpha=0.8)
ax.text(0.02, 0.95, info_busqueda, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()