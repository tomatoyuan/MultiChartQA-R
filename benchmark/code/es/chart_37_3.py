import matplotlib.pyplot as plt
import numpy as np

# Preparación de datos (simulación aproximada, se puede ajustar según la situación real)
categorias = [
    ["Chubasqueros y Pantalones Impermeables", "Chaquetas de Plumas Deportivas"],
    ["Ropa Estilo Tang/Ropa Estilo Chino", "Patrimonio Cultural Inmaterial/Ropa de Tejido y Tinte"],
    ["Camisas de Anime", "Vestidos de Anime"]
]
grupos = ["Ropa de Deportes al Aire Libre", "Ropa Estilo Chino", "Ropa de Anime"]
valores = [
    [27, 46],
    [123, 78],
    [200, 93]
]

# Configuración de colores (similar al esquema de colores claros del gráfico original)
colores_barras = ["#C9B8A7", "#B8A090"]  # Se puede ajustar según sea necesario

# Inicializar el gráfico
fig, axes = plt.subplots(3, 1, figsize=(6, 10), sharex=False)  # Ajustar la altura para acomodar el título
plt.subplots_adjust(top=0.85, hspace=0.5)  # Ajustar el espacio superior

# Agregar el título principal y el subtítulo
plt.suptitle("Tasa de Crecimiento de Categorías de Ropa Relacionadas con Círculos de Interés", fontsize=16, fontweight="bold", y=0.95)
plt.title("Porcentaje de Crecimiento Anual de las Ventas de Cada Categoría", fontsize=12, y=1.05)  # Subtítulo

for i in range(3):
    # Dibujar gráficos de barras horizontales
    axes[i].barh(categorias[i], valores[i], color=colores_barras)
    axes[i].set_title(grupos[i], fontsize=12, fontweight="bold")  # Establecer el título del grupo

    # Agregar etiquetas de datos (tasa de crecimiento en formato +%)
    for j, val in enumerate(valores[i]):
        axes[i].text(val + 5, categorias[i][j], f"{val}%+", 
                     va="center", fontsize=9, color="black")

# Establecer uniformemente los ejes (ocultar las marcas del eje x para que el gráfico sea más limpio)
for ax in axes:
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

plt.show()