import matplotlib.pyplot as plt

# Datos
etiquetas = ["Escuchar a los padres", "Decidir por sí mismo", "Escuchar a expertos u otros"]
tamaños = [36, 58, 6]
colores = ["#99CCFF", "#FFCC99", "#CC99FF"]  # Mantener el esquema de colores original

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)

# Dibujar un gráfico circular, agregar sombra y efecto de explosión para resaltar la parte "Decidir por sí mismo"
explosion = (0, 0.05, 0)  # Solo la parte "Decidir por sí mismo" se resalta
wedges, textos, autotextos = ax.pie(
    tamaños,
    explode=explosion,
    autopct='%1.1f%%',  # Solo mostrar el porcentaje
    startangle=90,
    colors=colores,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 2},  # Agregar un borde blanco
    textprops={'fontsize': 12, 'weight': 'bold'}  # Poner en negrita el texto del porcentaje
)

# Establecer el título
ax.set_title("¿Cuál opción prefieres en cuanto a la solicitud a la universidad?", fontsize=18, pad=20, fontweight='bold')

# Asegurarse de que el gráfico circular sea circular
ax.axis("equal")  

# Optimizar el estilo de la leyenda
leyenda = ax.legend(
    wedges, 
    etiquetas, 
    title="Preferencia en la solicitud a la universidad", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5),
    frameon=True,
    framealpha=0.9,
    edgecolor='lightgray',
    fontsize=12,
    title_fontsize=14,
    labelspacing=1.2,
    handlelength=1.5,
    handleheight=1.5
)

# Agregar color de fondo y esquinas redondeadas a la leyenda
frame = leyenda.get_frame()
frame.set_facecolor('#f8f9fa')
frame.set_boxstyle("round,pad=0.5,rounding_size=4")

# Agregar estilo a las etiquetas de datos
for texto in autotextos:
    texto.set_backgroundcolor('white')
    texto.set_alpha(0.8)
    texto.set_bbox(dict(facecolor='white', alpha=0.8, edgecolor='none', pad=2))

# Ajustar el diseño
plt.tight_layout(pad=2)

# Mostrar el gráfico
plt.show()