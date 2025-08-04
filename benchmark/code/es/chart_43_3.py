import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# Datos
etiquetas = [
    "Motivada a elegir un estilo de vida más cómodo en el último año",
    "Aprendió más sobre temas relacionados con las mujeres del mundo exterior pero no se expresó públicamente",
    "Participó en discusiones públicas sobre temas de mujeres en el último año",
    "Nunca realmente prestó atención, pensando que está demasiado lejos de mi vida y solo me centro en mi propia vida",
    "Intentó influir en otras mujeres alrededor hablando en voz alta en el último año (chicas ayudan a chicas)",
    "Reducio la atención deliberadamente en el último año debido a que el tema estaba demasiado saturado"
]
porcentajes = [41.9, 18.3, 17.4, 10.1, 8.0, 4.3]

# Crear un gradiente de color personalizado
colores = ["#4a6fe3", "#6a89f0", "#8aa5f7", "#a9bffb", "#c7d8fd", "#e5f0ff"]

# Crear un gráfico
fig, ax = plt.subplots(figsize=(12, 8))
posicion_y = np.arange(len(etiquetas))

# Dibujar un gráfico de barras horizontales con gradiente de color
for i, (valor, etiqueta) in enumerate(zip(porcentajes, etiquetas)):
    barra = ax.barh(i, valor, align='center', color=colores[i], alpha=0.9, edgecolor='none')
    ax.text(valor + 0.5, i, f'{valor}%', va='center', fontsize=11, color='#333333')

# Establecer las etiquetas del eje Y
ax.set_yticks(posicion_y)
ax.set_yticklabels(etiquetas, fontsize=12)
ax.invert_yaxis()  # Ordenar las etiquetas de arriba hacia abajo

# Establecer el rango del eje X
ax.set_xlim(0, max(porcentajes) * 1.15)  # Dejar algo de espacio para mostrar las etiquetas

# Agregar líneas de cuadrícula
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Establecer el título y las etiquetas
ax.set_title('Encuesta sobre el impacto de los temas relacionados con las mujeres en mujeres individuales', fontsize=16, pad=20)
ax.set_xlabel('Porcentaje (%)', fontsize=12, labelpad=10)

# Ajustar los bordes
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()