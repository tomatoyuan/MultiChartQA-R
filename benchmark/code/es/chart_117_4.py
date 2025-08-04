import matplotlib.pyplot as plt
import numpy as np

# Funciones de hogar inteligente
funciones = [
    "Sistema de control de iluminación inteligente", "Sistema de control de seguridad inteligente",
    "Sistema de control de cortinas inteligente",
    "Sistema de monitoreo ambiental inteligente", "Sistema de control de audio - video para hogar inteligente",
    "Sistema de control remoto de electrodomésticos",
    "Asistente de voz inteligente", "Modo de escenario de control con un solo botón",
    "Sistema de música de fondo", "Sistema de gestión de energía"
]
# Proporción correspondiente (%)
proporciones = [35.40, 35.24, 31.59, 31.59, 30.79, 29.84, 29.84, 29.52, 22.70, 21.75]

x = np.arange(len(funciones))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas, centradas encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center', va='center', fontsize=9)

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(funciones, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Funciones de hogar inteligente en las que los consumidores chinos están interesados en 2025')

plt.tight_layout()
plt.show()