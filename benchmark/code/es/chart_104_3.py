import matplotlib.pyplot as plt
import numpy as np

# Principales razones para aprender música
razones = ["Cultivar el interés de los niños", "Mejorar la auto - cultura", "Adquirir una habilidad adicional",
           "Cultivar el espíritu de los niños", "Aliviar la presión académica", "Amor propio por la música",
           "Obtener puntos adicionales en la prueba de ingreso a la universidad", "Otros niños están aprendiendo",
           "Perseguir carreras relacionadas", "Acercarse a celebridades"]
# Proporciones correspondientes (%)
proporciones = [30.09, 28.88, 27.26, 26.18, 25.37, 25.37, 21.46, 21.46, 21.05, 20.78]

x = np.arange(len(razones))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 6))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 0.5, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(razones, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Principales razones por las que los usuarios chinos aprenden música en 2025')

plt.tight_layout()
plt.show()