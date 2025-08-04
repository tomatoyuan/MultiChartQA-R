import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Etiquetas de las filas y columnas
grupos_edad = ['Menos de 20 años', '21 - 25 años', '26 - 30 años', '31 - 34 años', '35 - 40 años', '41 - 45 años', 'Más de 45 años']
generaciones = ['Generación 00', 'Generación 95', 'Generación 90', 'Generación 85', 'Antes de 85']

# Matriz de porcentajes
datos_porcentaje = np.array([
    [52, 0, 0, 0, 1],
    [42, 29, 5, 5, 2],
    [2, 70, 60, 24, 5],
    [2, 1, 33, 51, 24],
    [0, 0, 2, 17, 38],
    [1, 0, 0, 0, 22],
    [1, 0, 0, 0, 9],
])

# Calcular la posición del valor máximo de cada columna (para resaltar en amarillo)
mascara_resaltado = (datos_porcentaje == np.max(datos_porcentaje, axis = 0))

# Mapeo de colores
cmap = plt.cm.Purples
norm = mcolors.Normalize(vmin = 0, vmax = np.max(datos_porcentaje))

# Preparación de la gráfica
fig, ax = plt.subplots(figsize=(10, 7))
ax.set_xlim(0, len(generaciones))
ax.set_ylim(0, len(grupos_edad))

# Dibujar las celdas
for i in range(len(grupos_edad)):
    for j in range(len(generaciones)):
        valor = datos_porcentaje[i, j]
        if valor > 0:
            if mascara_resaltado[i, j]:
                color = '#FFD700'  # Amarillo para resaltar el valor máximo
                color_texto = 'black'
            else:
                color = cmap(norm(valor))  # Gradiente de morado
                color_texto = 'white' if valor > 30 else 'black'
            ax.add_patch(plt.Rectangle((j, len(grupos_edad)-1 - i), 1, 1, color = color))
            ax.text(j + 0.5, len(grupos_edad)-1 - i + 0.5, f'{valor}%',
                    ha = 'center', va = 'center', fontsize = 11, color = color_texto)

# Establecer las etiquetas de los ejes
ax.set_xticks(np.arange(len(generaciones)) + 0.5)
ax.set_xticklabels(generaciones, fontsize = 12)
ax.set_yticks(np.arange(len(grupos_edad)) + 0.5)
ax.set_yticklabels(grupos_edad[::-1], fontsize = 12)
ax.invert_yaxis()

# Título y fuente de los datos
plt.title('Distribución de la primera percepción del envejecimiento cutáneo\n'
          ' en diferentes edades por generación', fontsize = 14, weight = 'bold', loc = 'left')
plt.text(0, -1, 'Fuente de datos: Encuesta CBNData de julio de 2024\nQ5. ¿A qué edad comenzó a notar signos de envejecimiento cutáneo?',
         fontsize = 9, color = 'gray')

# Limpiar el estilo
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(left = False, bottom = False)
plt.grid(False)

# Agregar la barra de colores (solo muestra el mapeo de morado)
cbar = plt.colorbar(plt.cm.ScalarMappable(norm = norm, cmap = cmap),
                    ax = ax, orientation = 'vertical', shrink = 0.6, pad = 0.02)
cbar.set_label('Intensidad porcentual (no máximos)', fontsize = 10)

plt.tight_layout()
plt.show()