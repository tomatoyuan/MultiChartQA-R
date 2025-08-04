import matplotlib.pyplot as plt
import numpy as np

# Datos
categorias = ["Ropa y Calzado", "Muebles y Electrodomésticos", "Comida y Productos Frescos", "Teléfonos Móviles y Productos Digitales", "Belleza y Cuidado Personal", "Cuidado Médico y Salud"]
rangos = [1, 2, 3, 4, 5, 6]

# Crear una figura y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Establecer los colores del gráfico de barras (gradiente azul)
colores = plt.cm.Blues(np.linspace(0.8, 0.3, len(categorias)))

# Dibujar un gráfico de barras horizontales
barras = ax.barh(categorias, rangos, color=colores)

# Agregar etiquetas de datos
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 0.1, barra.get_y() + barra.get_height()/2,
            f'{int(ancho)}', ha='left', va='center', fontsize=10)

# Establecer el título y las etiquetas de los ejes
ax.set_title("Ranking de Categorías de Productos de Comercio Electrónico que se Lamentó Haber Comprado en el Día 11.11", fontsize=16, pad=15)
ax.set_xlabel("Ranking", fontsize=12, labelpad=10)
ax.set_ylabel("Categorías de Productos", fontsize=12, labelpad=10)

# Establecer las marcas del eje x
ax.set_xticks(range(1, max(rangos) + 1))

# Agregar líneas de cuadrícula para mejorar la legibilidad
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()