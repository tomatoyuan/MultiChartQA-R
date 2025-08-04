import matplotlib.pyplot as plt
import numpy as np

# Categorías de bebidas
categorias = ["Bebidas de vinagre (por ejemplo, Tiandi Yihao)", "Bebidas en polvo (por ejemplo, Xiangpiaopiao)", 
              "Bebidas a base de leche (por ejemplo, yogur, leche agria)", "Bebidas de café (por ejemplo, Nescafé)", 
              "Bebidas a base de proteínas vegetales (por ejemplo, leche de soja)", "Bebidas de té (por ejemplo, Té Verde Jasmin de Master Kong)", 
              "Bebidas energéticas (por ejemplo, Bebida Especial Dongpeng)", "Bebidas carbonatadas (por ejemplo, cola)", 
              "Agua con gas (por ejemplo, Yuanqi Forest)", "Bebidas de jugo de frutas o vegetales (por ejemplo, Minute Maid Pulpy Orange)", 
              "Agua embotellada (por ejemplo, Agua Mineral C'estbon)", "Productos lácteos (por ejemplo, yogur, leche)"]
# Proporciones correspondientes (%)
proporciones = [16.10, 16.90, 29.30, 29.40, 31.00, 31.60, 32.80, 49.50, 50.90, 51.00, 51.00, 51.70]

y = np.arange(len(categorias))  # Coordenadas del eje y

fig, ax = plt.subplots(figsize=(10, 7))
# Dibujar un gráfico de barras horizontales
barras = ax.barh(y, proporciones, color='orange')

# Agregar anotaciones numéricas
for i, proporcion in enumerate(proporciones):
    ax.text(proporcion, i, f'{proporcion}', va='center', ha='left', fontsize=9)

# Establecer las marcas y etiquetas del eje y
ax.set_yticks(y)
ax.set_yticklabels(categorias)
ax.set_xlabel('Proporción (%)')
ax.set_title('Conciencia de los consumidores chinos sobre las categorías de bebidas en 2025')

plt.tight_layout()
plt.show()