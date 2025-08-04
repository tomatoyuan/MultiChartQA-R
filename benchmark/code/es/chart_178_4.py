import matplotlib.pyplot as plt
import numpy as np

# Categorías
categorias = ['≤1k', '1-2k', '2-3k', '3-4k', '4-5k', '5-8k', '8-10k', '>10k']
# Datos
y_2023 = [5, 18, 19, 27, 17, 8, 4, 2]
y_2024 = [4, 15, 18, 25, 19, 13, 5, 1]

x = np.arange(len(categorias))
ancho = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
barras1 = ax.bar(x - ancho/2, y_2023, ancho, label='Gasto en regalos de Año Nuevo 23', color='#8B0000')
barras2 = ax.bar(x + ancho/2, y_2024, ancho, label='Presupuesto para regalos de Año Nuevo 24', color='#CD5C5C')

# Agregar anotaciones de valores
for barra in barras1 + barras2:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=8)

# Establecer título y etiquetas
ax.set_title('Distribución del presupuesto de las personas para la compra de regalos de Año Nuevo', fontsize=14)
ax.set_ylabel('Porcentaje')
ax.set_xticks(x)
ax.set_xticklabels(categorias)
ax.legend()
ax.set_ylim(0, 35)

plt.tight_layout()
plt.show()