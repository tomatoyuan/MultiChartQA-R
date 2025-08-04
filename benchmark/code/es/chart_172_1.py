import matplotlib.pyplot as plt

# 定义数据
etiquetas = ['Prefiere bajos niveles de azúcar', 'Prefiere sin azúcar', 'No presta atención', 'Prefiere mucha azúcar']
tamaños = [56, 23, 12, 9]
colores = ['#00a2e8', '#b3ecf7', '#00d2c8', '#4caf50']  # Simula la combinación de colores de la imagen original

# Concatenar etiquetas y mostrar porcentajes
etiquetas_con_porcentaje = [f'{etiqueta}, \n{tamaño}%' for etiqueta, tamaño in zip(etiquetas, tamaños)]

# Crear un gráfico circular
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos = ax.pie(tamaños, labels=etiquetas_con_porcentaje, colors=colores, startangle=110,
                           labeldistance=0.2, textprops={'fontsize': 11, 'color': 'white'})

# Agregar título
plt.title('Opiniones de los consumidores chinos sobre el contenido\n de azúcar en las bebidas carbonatadas en 2022', fontsize=14, fontweight='bold', pad=20)

# Forzar que la figura sea circular
ax.axis('equal')

plt.tight_layout()
plt.show()