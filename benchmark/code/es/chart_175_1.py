import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Datos
etiquetas = [
    'Muy confiado, \nespera un '
    'rápido desarrollo',
    'Bastante confiado, \n'
    'espera un aumento estable',
    'Igual que en 2022',
    'Poco confiado, \n'
    'necesita tiempo para recuperarse'
]
valores = [44.4, 43.2, 7.4, 4.9]
colores = ['#0070C0'] * 4

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(10, 6))
barras = ax.barh(etiquetas[::-1], valores[::-1], color=colores)

# Agregar etiquetas
for barra in barras:
    ax.text(
        barra.get_width() + 1,
        barra.get_y() + barra.get_height() / 2,
        f'{barra.get_width():.1f}%',
        va='center',
        fontsize=12
    )

# Agregar un marco discontinuo rojo (encuadra los dos primeros elementos)
# Las coordenadas se miden desde la parte inferior, la altura total de dos barras es la altura de 2 barras + el espacio
y_superior = barras[3].get_y() + barras[3].get_height() + 0.1
y_inferior = barras[2].get_y() - 0.1
rectangulo = patches.Rectangle(
    (0, y_inferior), 50, y_superior - y_inferior,
    linewidth=2, edgecolor='red', linestyle='--', facecolor='none'
)
ax.add_patch(rectangulo)

# Agregar la etiqueta "Actitud positiva"
ax.text(
    52, y_inferior + (y_superior - y_inferior)/2,
    'Actitud positiva 87.6%',
    color='red', fontsize=14, va='center'
)

# Mejorar la apariencia
ax.set_xlim(0, 60)
ax.set_xlabel('Proporción (%)')
ax.set_title('Confianza de las empresas chinas en el mercado internacional en 2023', fontsize=16)
plt.tight_layout()
plt.show()