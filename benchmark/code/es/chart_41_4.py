import matplotlib.pyplot as plt

# Datos
etiquetas = ['Comida para mascotas', 'Accesorios para mascotas', 'Salud de mascotas', 'Mascotas vivas', 'Servicios para mascotas']
tamaños = [49.7, 35.5, 8.4, 6.2, 0.2]
# Esquema de colores para una mejor presentación (utilizando tonos degradados más suaves)
colores = ['#6a89cc', '#82ccdd', '#b8e994', '#f8c291', '#d6a2e8']
# Resaltar la parte más grande
explode = (0.1, 0, 0, 0, 0)  

# Crear un lienzo y un sub - gráfico
fig, ax = plt.subplots(figsize=(10, 7), dpi=300)

# Dibujar un gráfico de pastel con sombra y efecto 3D
wedges, texts, autotexts = ax.pie(
    tamaños, 
    explode=explode,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=95,
    colors=colores,
    shadow=True,
    wedgeprops={'edgecolor': 'w', 'linewidth': 2},
    textprops={'fontsize': 10, 'weight': 'bold'}
)

# Ajustar el color de los textos de porcentaje
for text in autotexts:
    text.set_color('black')

# Establecer el título y la leyenda
ax.set_title('Proporción de ventas de subcategorías de comercio electrónico de mascotas en MAT2024', fontsize=16, pad=20)
ax.legend(wedges, etiquetas, title="Categorías", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Asegurarse de que el gráfico de pastel sea circular
plt.axis('equal')
plt.tight_layout()

# Guardar el gráfico (opcional)
# plt.savefig('pet_ecommerce_sales.png', bbox_inches='tight')

plt.show()