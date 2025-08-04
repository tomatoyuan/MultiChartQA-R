import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Preparación de datos
grupos_edad = ['Menos de 18', '18 - 24', '25 - 34', '35 - 44', '45 - 54', '55 - 64', 'Más de 65']
datos = [20, 30, 15, 12, 10, 8, 8]

# Crear colores con gradiente
colores = plt.cm.Blues(np.linspace(0.8, 0.4, len(grupos_edad)))
indice_destacado = 1  # Destacar el segundo grupo de edad
colores[indice_destacado] = plt.cm.Oranges(0.6)  # Usar naranja para destacar

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

# Establecer el estilo de fondo
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Dibujar un gráfico de barras
barras = ax.bar(grupos_edad, datos, color=colores, edgecolor='black', linewidth=0.5, alpha=0.9)

# Agregar etiquetas de datos
for barra in barras:
    altura = barra.get_height()
    ax.text(barra.get_x() + barra.get_width()/2., altura + 0.5,
            f'{altura}', ha='center', va='bottom', fontsize=10)

# Establecer título y etiquetas
ax.set_title('Análisis de los grupos de edad de la población que busca información sobre enfermedades cardíacas coronarias', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Grupo de edad', fontsize=12, labelpad=10)
ax.set_ylabel('Número de buscadores', fontsize=12, labelpad=10)

# Establecer el rango y las divisiones del eje y
ax.set_ylim(0, max(datos) * 1.1)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

# Agregar líneas de cuadrícula
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Agregar una leyenda
etiquetas_leyenda = ['Otros grupos de edad' if i != indice_destacado else '18 - 24 (Más alto)' for i in range(len(grupos_edad))]
manijas = [plt.Rectangle((0, 0), 1, 1, color=colores[i]) for i in range(len(grupos_edad))]
ax.legend(manijas[0:2], etiquetas_leyenda[0:2], loc='upper right')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()