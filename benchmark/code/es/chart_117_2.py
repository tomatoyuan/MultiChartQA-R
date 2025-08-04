import matplotlib.pyplot as plt
import numpy as np

# Factores de preocupación
factores = [
    "Comodidad", "Textura del material", "Amigabilidad ambiental", "Durabilidad", "Facilidad de limpieza", "Seguridad", 
    "Diseño de estilo", "Ajuste de color", "Decoratividad", "Practicalidad", "Marca", "Servicio posventa", "Descuento"
]
# Proporciones correspondientes (%)
proporciones = [37.69, 36.92, 35.38, 33.85, 33.46, 32.88, 
               32.50, 31.35, 30.38, 30.19, 28.08, 27.12, 25.00]

x = np.arange(len(factores))  # Coordenadas del eje x

fig, ax = plt.subplots(figsize=(12, 7))
# Dibujar un gráfico de barras
barras = ax.bar(x, proporciones, color='orange')

# Agregar anotaciones numéricas, centradas encima de las barras
for i, proporcion in enumerate(proporciones):
    ax.text(i, proporcion + 1, f'{proporcion}', ha='center', va='center', fontsize=9)

# Establecer las marcas y etiquetas del eje x, rotar las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(factores, rotation=45, ha='right')
ax.set_ylabel('Proporción (%)')
ax.set_title('Factores que preocupan a los consumidores chinos al comprar productos de decoración y accesorios para el hogar en 2025')

plt.tight_layout()
plt.show()