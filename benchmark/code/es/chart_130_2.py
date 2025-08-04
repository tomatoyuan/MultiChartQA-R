import matplotlib.pyplot as plt
import numpy as np

# Datos
etiquetas = ["Muy Satisfecho", "Relativamente Satisfecho", "Promedio", "Relativamente Insatisfecho", "Muy Insatisfecho"]
porcentajes = [19.1, 46.4, 26.7, 6.7, 1.1]
# Puntuaciones de satisfacción para ordenar (de alta a baja)
puntuacion_satisfaccion = [5, 4, 3, 2, 1]

# Ordenar por puntuación de satisfacción
indices_ordenados = np.argsort(puntuacion_satisfaccion)
etiquetas = [etiquetas[i] for i in indices_ordenados]
porcentajes = [porcentajes[i] for i in indices_ordenados]
puntuacion_satisfaccion = [puntuacion_satisfaccion[i] for i in indices_ordenados]

fig, ax = plt.subplots(figsize=(8, 6))

# Dibujar un gráfico de línea
ax.plot(puntuacion_satisfaccion, porcentajes, marker='o', color='orange', linewidth=2)
ax.fill_between(puntuacion_satisfaccion, porcentajes, color='orange', alpha=0.2)

# Agregar puntos de datos y anotaciones numéricas
for x, y, etiqueta in zip(puntuacion_satisfaccion, porcentajes, etiquetas):
    ax.scatter(x, y, color='orange', s=50)
    ax.text(x, y + 1.5, f'{y}%', ha='center', va='bottom')

# Establecer las etiquetas del eje x a los niveles de satisfacción
ax.set_xticks(puntuacion_satisfaccion)
ax.set_xticklabels(etiquetas, rotation=15)
ax.set_ylabel('Porcentaje (%)')
ax.set_title('Evaluación subjetiva de la calidad del sueño de los residentes chinos')

plt.tight_layout()
plt.show()