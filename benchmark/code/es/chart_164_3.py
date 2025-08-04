import matplotlib.pyplot as plt

# 数据
etiquetas = ['Tela suave', 'Ajuste cómodo y cercano a la piel', 'Respirante, mantiene seco', 'Ligero, fácil de transportar', 'Elástico, fácil de estirar', 'Abrigo']
valores = [75, 72, 69, 66, 57, 55]
colores = ['#c49e6c', '#b88d59', '#a87d4a', '#98703d', '#88612f', '#7a5325']

# Crear un gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.bar(etiquetas, valores, color=colores)

# Agregar etiquetas de valores
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'{altura}%',
                xy=(barra.get_x() + barra.get_width() / 2, altura),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# Embellir el gráfico
ax.set_title("Requisitos específicos de comodidad de los consumidores (presentados en forma de gráfico de barras)", fontsize=14)
ax.set_ylabel("Proporción (%)")
ax.set_ylim(0, 80)
plt.xticks(rotation=30)
plt.tight_layout()

# Agregar una nota sobre la fuente de los datos
plt.figtext(0.5, -0.05,
            "Fuente de los datos: Encuesta de CBNData sobre las tendencias de moda de la ropa de outdoor de lujo en China en mayo de 2024\nExplicación de los datos: ¿Cuáles de los siguientes requisitos específicos tiene para la comodidad de la ropa de outdoor? N = 571",
            wrap=True, horizontalalignment='center', fontsize=10)

plt.show()