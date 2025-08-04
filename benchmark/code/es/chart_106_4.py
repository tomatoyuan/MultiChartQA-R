import matplotlib.pyplot as plt
import numpy as np

# Dimensiones de satisfacción
dimensiones = ["Conciencia de la marca", "Endosante/ Promoción publicitaria", "Sabor", "Ingredientes y eficacia de la bebida", 
               "Variedad/diferenciación del producto", "Precio", "Actividades promocionales", "Conveniencia de compra", 
               "Servicio después de la venta", "Diseño de apariencia", "Calidad de higiene", "Métodos de marketing (co - branding de IP/Actividades de consumo experiential)"]
# Proporción de diferentes calificaciones (1 - 5 puntos) en cada dimensión, en el orden de 5 puntos, 4 puntos, 3 puntos, 2 puntos, 1 punto
datos = np.array([
    [41.55, 43.16, 10.04, 5.36, 1.39],
    [32.98, 34.32, 24.13, 7.50, 1.07],
    [40.48, 37.80, 14.48, 4.58, 2.68],
    [33.51, 39.14, 17.43, 6.43, 3.49],
    [32.71, 36.19, 21.98, 7.24, 1.88],
    [26.27, 42.63, 20.64, 7.77, 2.69],
    [32.17, 36.46, 19.64, 8.85, 2.88],
    [28.95, 35.12, 20.65, 10.99, 4.29],
    [28.69, 33.24, 24.93, 9.12, 4.02],
    [32.98, 42.09, 17.43, 5.36, 2.18],
    [38.61, 36.73, 16.89, 4.03, 3.79],
    [29.49, 34.85, 25.21, 8.31, 2.16]
])

# Colores correspondientes a las calificaciones, correspondientes a los colores en el gráfico
colores = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
calificaciones = ["5 Puntos", "4 Puntos", "3 Puntos", "2 Puntos", "1 Punto"]

fig, ax = plt.subplots(figsize=(12, 8))
base = np.zeros(len(dimensiones))

for i in range(datos.shape[1]):
    ax.bar(dimensiones, datos[:, i], bottom=base, color=colores[i], label=calificaciones[i])
    # Agregar anotaciones numéricas
    for j in range(len(dimensiones)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}', ha='center', va='center', fontsize=8)
    base += datos[:, i]

ax.set_ylabel('Proporción (%)')
ax.set_title('Calificaciones de satisfacción de los consumidores chinos para las bebidas embotelladas disponibles en el mercado en 2025')
ax.legend()
plt.xticks(rotation=15, ha='right')
plt.tight_layout()
plt.show()