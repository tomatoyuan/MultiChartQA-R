import matplotlib.pyplot as plt
import numpy as np

# Principales tipos de ansiedad durante el embarazo
ansiedades = ["Ansiedad por presión económica", "Ansiedad por conocimiento del embarazo y el parto", "Ansiedad por planificación del futuro", "Ansiedad por asimetría de información", 
             "Ansiedad por relación familiar", "Ansiedad por crecimiento personal/trabajo", "Ansiedad por imagen corporal", "Ansiedad por salud", "Ansiedad por selección y compra de productos"]
# Proporciones correspondientes (%)
proporciones = [31.57, 28.51, 27.90, 27.70, 26.68, 26.48, 25.87, 25.46, 23.42]

x = np.arange(len(ansiedades))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center')

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(ansiedades, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Principales ansiedades de las futuras madres chinas en 2025')

plt.tight_layout()
plt.show()