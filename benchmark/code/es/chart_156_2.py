import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


# Escenarios y sus correspondientes porcentajes
escenarios = ['Cita', 'Mudanza laboral', 'Cena en grupo', 'Tomar fotos', 'Viaje', 'Aburrimiento en casa', 'Clase']
porcentajes = [55, 52, 50, 44, 43, 18, 12]

# Ordenar en orden inverso (para mostrar de arriba hacia abajo)
escenarios = escenarios[::-1]
porcentajes = porcentajes[::-1]
pos_y = np.arange(len(escenarios))

# Crear una paleta de colores degradada
cmap = LinearSegmentedColormap.from_list("rosado_suave", ["#ffe6e6", "#ffb3b3"])

# Crear la gráfica
fig, ax = plt.subplots(figsize=(8, 6))
barras = ax.barh(pos_y, porcentajes, color=cmap(porcentajes / np.max(porcentajes)))

# Agregar etiquetas de texto
for i, (p, etiqueta) in enumerate(zip(porcentajes, escenarios)):
    ax.text(p + 1, i, f"{p}%", va='center', fontsize=11)

# Configurar el título y las etiquetas
ax.set_yticks(pos_y)
ax.set_yticklabels(escenarios, fontsize=12)
ax.invert_yaxis()  # El escenario más popular se muestra en la parte superior
ax.set_xlim(0, 60)
ax.set_title("Encuesta sobre escenarios de uso de medias desnudas por los consumidores", fontsize=15, weight='bold')

# Eliminar los bordes y las marcas de graduación innecesarias
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')
ax.xaxis.set_visible(False)

# Agregar la fuente de los datos
texto_fuente = "Fuente de datos: Datos de la encuesta de CBNData en julio de 2024\nBig Data: Total Insight"
plt.figtext(0.5, -0.05, texto_fuente, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()