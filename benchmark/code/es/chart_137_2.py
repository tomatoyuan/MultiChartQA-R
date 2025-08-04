import matplotlib.pyplot as plt
import numpy as np

# Datos
funciones = ["Conveniencia de compra", "Servicio personalizado", "Interacción y social", "Servicio y posventa",
             "Protección de la seguridad y privacidad de los datos", "Reconocimiento de imágenes", "Otros"]
porcentajes = [67.2, 63.5, 48.8, 40.0, 31.6, 24.4, 0.0]

x = np.arange(len(funciones))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange')

# Agregar anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Porcentaje (%)')
ax.set_xlabel('Tipos de funciones ventajosas')
ax.set_xticks(x)
ax.set_xticklabels(funciones, rotation=15, ha='right')
ax.set_title('Principales funciones ventajosas del comercio electrónico basado en IA chino que atraen a los consumidores en 2024')

plt.tight_layout()
plt.show()