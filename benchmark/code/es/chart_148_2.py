import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos
tipos_de_bebidas = [
    "Bebidas carbonatadas sin azúcar (por ejemplo, \ncola sin azúcar, serie Yuanqi Forest, agua mineral sin azúcar, etc.)",
    "Bebidas de té sin azúcar (por ejemplo, serie \nDongfang Shuye, té oolong sin azúcar, etc.)",
    "Jugos de frutas y verduras sin azúcar (por \nejemplo, jugos NFC, jugos de verduras sin azúcar, etc.)",
    "Bebidas a base de leche sin azúcar (por \nejemplo, yogur sin azúcar, leche con calcio sin azúcar, etc.)",
    "Otras bebidas sin azúcar (por ejemplo, \nzumo de ciruela sin azúcar, etc.)"
]
proporciones = [76.07, 70.09, 46.16, 45.90, 11.31]  # Proporción (%)

x = np.arange(len(tipos_de_bebidas))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(x, proporciones, color='coral')
ax.set_title('Tipos de bebidas sin azúcar consumidas por los consumidores chinos en 2023', fontsize=14)
ax.set_xlabel('Proporción (%)')
ax.set_ylabel('Tipos de bebidas sin azúcar')
ax.set_yticks(x)
ax.set_yticklabels(tipos_de_bebidas)

# Añadir anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion + 1, i, f'{proporcion}%', ha='left', va='center', color='black')

# Añadir una leyenda y descripción de la fuente de la muestra
ax.legend(barras, ['Proporción'], loc='lower right')
ax.text(0.7, -0.2, 'Fuente de la muestra: Sistema de Encuesta y Cálculo de Datos de Strawberry Pie', 
        fontsize=10, ha='center', transform=ax.transAxes)

plt.tight_layout()
plt.show()