import matplotlib.pyplot as plt
import numpy as np

# Datos
expectativas = ["Efecto del producto de larga duración", "Eficacia del producto más refinada", "Diseño de embalaje más bonito y creativo", 
                "Precio asequible", "Alta seguridad del producto", "Lanzamiento de productos con eficacia compuesta"]
porcentajes = [71.4, 47.0, 45.0, 37.1, 32.7, 31.9]

x = np.arange(len(expectativas))

fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar un gráfico de barras
barras = ax.bar(x, porcentajes, color='orange')

# Añadir anotaciones numéricas
for i, porcentaje in enumerate(porcentajes):
    ax.text(i, porcentaje + 1, f'{porcentaje}%', ha='center', va='bottom')

# Configurar los ejes
ax.set_ylabel('Porcentaje (%)')
ax.set_xlabel('Tipo de expectativa')
ax.set_xticks(x)
ax.set_xticklabels(expectativas, rotation=15, ha='right')
ax.set_title('Expectativas de los consumidores chinos para el desarrollo de cosméticos de protección solar')

plt.tight_layout()
plt.show()