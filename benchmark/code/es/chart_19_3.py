import matplotlib.pyplot as plt

# Extraer datos del gráfico
grupos_edad = ["Menos de 19", "20 - 29", "30 - 39", "40 - 49", "Más de 50"]
porcentajes = [22, 36, 28, 9, 5]

# Esquema de colores personalizado (utilizando tonos suaves de azul - verde)
colores = ['#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

# Resaltar el sector más grande (grupo de edad 20 - 29)
resaltar = (0, 0.1, 0, 0, 0)

# Crear un objeto de trazado
fig, ax = plt.subplots(figsize=(10, 7))

# Dibujar un gráfico circular decorado
wedges, textos, autotextos = ax.pie(
    porcentajes,
    explode=resaltar,
    labels=grupos_edad,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 1},
    textprops={'fontsize': 12}
)

# Establecer el color de las etiquetas de porcentaje para que coincidan con los colores del gráfico circular
for texto, autotexto, color in zip(textos, autotextos, colores):
    texto.set_color('gray')
    autotexto.set_color('black')
    autotexto.set_fontweight('bold')

# Establecer el gráfico circular para que sea un círculo perfecto
ax.axis('equal')

# Agregar un título
ax.set_title('Distribución de edad de los consumidores que "más se arrepienten"', fontsize=16, fontweight='bold', pad=20)

# Agregar una leyenda y ajustar su posición
ax.legend(wedges, grupos_edad, title="Grupos de edad", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Establecer el color de fondo del gráfico
fig.set_facecolor('#f8f9fa')

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()