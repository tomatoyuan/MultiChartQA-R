import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
marcas = [
    "元气森林", "Coca - Cola", "Nongfu Spring", "Oriental Leaves", 
    "Pepsi", "Wanglaoji", "Vitasoy", "Suntory", 
    "Schweppes", "Watsons", "Yineng", "Mingren", "Lingqi"
]
proporciones = [49.54, 42.52, 42.38, 34.70, 
               34.44, 23.05, 21.19, 20.00, 
               14.83, 14.70, 9.93, 9.93, 9.27]  # Proporción (%)

x = np.arange(len(marcas))

fig, ax = plt.subplots(figsize=(10, 8))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(x, proporciones, color='coral')
ax.set_title('Marcas populares de bebidas sin azúcar entre los consumidores chinos en 2023', fontsize=14)
ax.set_xlabel('Proporción (%)')
ax.set_ylabel('Marcas de bebidas sin azúcar')
ax.set_yticks(x)
ax.set_yticklabels(marcas)
ax.set_xlim(0, 55)  # Ajustar el rango del eje x para ajustarse a la proporción máxima (49.54%)

# Agregar etiquetas numéricas
for i, prop in enumerate(proporciones):
    ax.text(prop + 1, i, f'{prop}%', ha='left', va='center', color='black', fontsize=11)

# Agregar una leyenda y fuente de la muestra (ajustar la posición si es necesario restaurar la imagen original)
ax.legend(barras, ['Proporción'], loc='lower right')
ax.text(0.8, -0.12, 'Fuente de la muestra: Sistema de Encuesta y Cálculo de Datos de Strawberry Pie', 
        fontsize=10, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()