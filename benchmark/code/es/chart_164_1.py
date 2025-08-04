import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# Preparación de datos
categorias = [
    "Viajes en \nnieve/esquí", "Camping de lujo", "Deportes acuáticos", "Golf", "Ecuestre", "Globos \naerostáticos",
    "Escalada", "Deportes submarinos", "Deportes extremos", "Tiro",
    "Montañismo\nsenderismo\ncamping", "Ciclismo", "Pesca", "Paseo por la ciudad"
]
valores = [38, 38, 35, 17, 6, 1, 26, 22, 9, 8, 57, 54, 35, 29]

# Colores de las categorías
colores = [
    "#EECFA1"] * 6 + ["#F4A259"] * 4 + ["#B1D8B7"] * 4  # Colores de deportes al aire libre de lujo/deportes al aire libre profesionales/deportes al aire libre populares

fig, ax = plt.subplots(figsize=(12, 8))
barras = ax.barh(categorias, valores, color=colores)

# Agregar etiquetas de valores
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1.5, barra.get_y() + barra.get_height()/2,
            f'{int(ancho)}%', va='center', fontsize=10)

# Título del gráfico
ax.set_title("Distribución de deportes al aire libre que los consumidores han probado y les gustan", fontsize=14, fontweight='bold', loc='center', pad=20)

# Eliminar elementos adicionales
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', length=0)
ax.set_xlim(0, 65)

# Etiquetas de las regiones de categoría (a la derecha)
ax.text(65.5, 2.5, "Deportes al aire libre de lujo", fontsize=12, weight='bold', color='#D4A55A', va='center')
ax.text(65.5, 8.5, "Deportes al aire libre profesionales", fontsize=12, weight='bold', color='#D98C3A', va='center')
ax.text(65.5, 12.5, "Deportes al aire libre populares", fontsize=12, weight='bold', color='#568259', va='center')

# Agregar texto explicativo
plt.figtext(0.01, -0.03,
            "Fuente de datos: Encuesta de tendencias de moda de ropa de lujo para deportes al aire libre en China realizada por CBNData en mayo de 2024\n"
            "Explicación de los datos: ¿Qué deportes o actividades al aire libre ha probado y le gustan? N = 1000",
            ha='left', fontsize=9, linespacing=1.5)

plt.tight_layout()
plt.show()