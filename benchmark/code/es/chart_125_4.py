import matplotlib.pyplot as plt
import numpy as np

# Razones de compra izquierda
razones_izquierda = ["Portabilidad", "Facilidad de operación", "Comodidad de agarre", "Apariencia pequeña y bonita", "Reducir el tiempo frente a la pantalla", "Bajo precio"]
proporciones_izquierda = [73.5, 54.4, 45.2, 38.4, 24.1, 11.0]

# Factores de influencia derecha
factores_derecha = [
    "Cree que la marca tiene alta influencia", "Ha comprado otros teléfonos de la marca antes", "Alta relación calidad - precio", 
    "Buen servicio después de la venta", "El sistema se adapta mejor a los hábitos personales de uso", "La tecnología de pantalla pequeña es líder entre marcas similares", 
    "Fabricante del procesador"
]
proporciones_derecha = [47.2, 46.6, 42.6, 40.2, 33.3, 19.7, 10.0]

fig = plt.figure(figsize=(16, 6))
# Subgráfico izquierdo
ax1 = fig.add_subplot(121)
y1 = np.arange(len(razones_izquierda))
barras1 = ax1.barh(y1, proporciones_izquierda, color='orange')
for i, proporcion in enumerate(proporciones_izquierda):
    ax1.text(proporcion + 1, i, f'{proporcion}%', va='center', ha='left', fontsize=9)
ax1.set_yticks(y1)
ax1.set_yticklabels(razones_izquierda)
ax1.set_xlabel('Proporción (%)')
ax1.set_title('Razones por las que los consumidores chinos compran teléfonos de pantalla pequeña')

# Subgráfico derecho
ax2 = fig.add_subplot(122)
y2 = np.arange(len(factores_derecha))
barras2 = ax2.barh(y2, proporciones_derecha, color='orange')
for i, proporcion in enumerate(proporciones_derecha):
    ax2.text(proporcion + 1, i, f'{proporcion}%', va='center', ha='left', fontsize=9)
ax2.set_yticks(y2)
ax2.set_yticklabels(factores_derecha)
ax2.set_xlabel('Proporción (%)')
ax2.set_title('Factores de influencia para que los consumidores chinos elijan marcas de teléfonos de pantalla pequeña')

plt.tight_layout()
plt.show()