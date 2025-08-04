import matplotlib.pyplot as plt
import numpy as np

# Tipos de productos
tipos_de_productos = ["Productos de manualidades", "Ropa, zapatos y sombreros, etc.", "Herramientas de producción agrícola e industrial (por ejemplo, hoz, azada, maquinaria y equipos, etc.)", 
                      "Electrodomésticos (por ejemplo, teléfonos móviles, computadoras, refrigeradores, televisores de color, etc.)", "Artículos de uso diario (por ejemplo, productos de papel para limpieza, \nalmacenamiento doméstico, productos de cuidado de la piel, etc.)", 
                      "Alimentos y productos frescos (por ejemplo, cereales y aceites, frutas, bebidas alcohólicas, aperitivos, etc.)"]
# Proporciones correspondientes (%)
proporciones = [23.94, 27.39, 38.83, 39.10, 41.76, 50.53]

y = np.arange(len(tipos_de_productos))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 6))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(tipos_de_productos)
ax.set_xlabel('Proporción (%)')
ax.set_title('Tipos de productos vendidos por operadores de comercio electrónico rural en China en 2025')

plt.tight_layout()
plt.show()