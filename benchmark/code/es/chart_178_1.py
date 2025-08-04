import matplotlib.pyplot as plt

# 数据
categorias = [
    "Fiesta de la Primavera, \nFestival del Medio Otoño,\n Festival del Barco Dragón",
    "Cumpleaños, Bodas, Anniversarios",
    "Día de San Valentín, Qixi Festival",
    "Día del Padre, Día de la Madre",
    "Navidad, Año Nuevo",
    "Festival de compras 11.11, 6.18"
]
valores = [96, 92, 81, 76, 53, 48]

# Dibujo
fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.barh(categorias, valores, color="#8B0000")
ax.invert_yaxis()
ax.set_xlim(0, 100)
ax.set_xlabel("Proporción (%)")
ax.set_title("Distribución de las fechas festivas para dar regalos en la economía de regalos de China", fontsize=14)

# Agregar etiquetas de valores
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height() / 2, f'{ancho}%', va='center')

plt.tight_layout()
plt.show()