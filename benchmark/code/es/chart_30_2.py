import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Datos
etiquetas = ['19 - 24 años', '25 - 34 años', '18 años o menos', '35 - 49 años', '50 años']
tamaños = [41, 33, 15, 10, 1]
# Colores personalizados, utilizando un esquema de combinación de colores más profesional
colores = ['#3498db', '#2ecc71', '#f39c12', '#e74c3c', '#9b59b6']
# Resaltar el sector más grande
resaltar = (0.1, 0, 0, 0, 0)  

# Crear un lienzo y un subgráfico
fig, ax = plt.subplots(figsize=(10, 7))

# Dibujar un gráfico de pastel, agregar sombra y estilo de porcentaje personalizado
wedges, textos, autotextos = ax.pie(
    tamaños, 
    explode=resaltar,
    labels=etiquetas,
    colors=colores,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(tamaños)/100)})',  # Mostrar tanto el porcentaje como el número real de personas
    shadow=True,
    startangle=90,
    textprops={'fontsize': 12}
)

# Establecer el título
ax.set_title('El perfil de la población relacionada con el SIDA tiende a ser joven', fontsize=16, pad=20)

# Hacer que el gráfico de pastel sea un círculo perfecto
ax.axis('equal')  

# Agregar una leyenda
plt.legend(wedges, etiquetas, title="Grupos de edad", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Agregar una nota
plt.figtext(0.5, 0.01, f"Datos totales: {sum(tamaños)} personas", ha="center", fontsize=12)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()