import matplotlib.pyplot as plt
import numpy as np

# Dimensiones de evaluación
dimensiones = ["Nuevo formato", "Actualización en tiempo real", "Contenido rico", "Fuerte interacción", "Profesional y autorizado", 
               "Reporte exclusivo", "Soporte de datos", "Perspectiva internacional", "Análisis profundo"]
# Proporciones de diferentes puntuaciones (1 - 5 puntos) en cada dimensión, en el orden de 5 puntos, 4 puntos, 3 puntos, 2 puntos, 1 punto
datos = np.array([
    [29.82, 46.05, 14.04, 7.02, 3.07],
    [43.53, 32.89, 18.64, 3.51, 1.43],
    [36.62, 36.51, 16.89, 7.13, 2.85],
    [28.07, 35.20, 27.30, 7.46, 1.97],
    [35.64, 33.44, 21.60, 6.03, 3.29],
    [29.39, 38.93, 18.53, 11.61, 1.54],
    [38.05, 34.43, 18.53, 5.70, 3.29],
    [35.96, 37.39, 17.98, 6.92, 1.75],
    [35.96, 34.76, 20.18, 6.47, 2.63]
])

# Colores correspondientes a las puntuaciones, correspondientes a los colores en el gráfico
colores = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
puntuaciones = ["5 Puntos", "4 Puntos", "3 Puntos", "2 Puntos", "1 Punto"]

fig, ax = plt.subplots(figsize=(14, 8))  # Aumentar el ancho de la gráfica para acomodar la leyenda exterior
base = np.zeros(len(dimensiones))

for i in range(datos.shape[1]):
    ax.bar(dimensiones, datos[:, i], bottom=base, color=colores[i], label=puntuaciones[i])
    # Agregar anotaciones numéricas
    for j in range(len(dimensiones)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}', ha='center', va='center', fontsize=8)
    base += datos[:, i]

ax.set_ylabel('Proporción (%)')
ax.set_title('Puntuaciones de importancia de las noticias de medios financieros en 2025 dadas por los usuarios de noticias financieras chinos')

# Mover la leyenda a la derecha exterior de la gráfica
ax.legend(bbox_to_anchor=(1.01, 1), loc='upper left')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()