import matplotlib.pyplot as plt

# Definición de datos
etiquetas = ['Control de azúcar en sangre', 'Regulación de la presión arterial', 'Reducción de colesterol', 'Salud cardíaca', 'Otros']
tamaños = [25, 25, 25, 17, 8]
colores = ['#00d2c8', '#66cdaa', '#00a2e8', '#3399ff', '#ccecf9']  # Seguir la paleta de colores del gráfico

# Construir contenido de etiquetas (con porcentaje)
etiquetas_con_pct = [f'{etiqueta}, \n{tamaño}%' for etiqueta, tamaño in zip(etiquetas, tamaños)]

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos = ax.pie(tamaños, labels=etiquetas_con_pct, colors=colores,
                           startangle=90, labeldistance=0.3,
                           textprops={'fontsize': 11, 'color': 'white'})

# Título
plt.title('Direcciones de innovación de materias primas \nrelacionadas con enfermedades crónicas en 2024', fontsize=14, fontweight='bold', pad=20)

# Mantener el gráfico en forma circular
ax.axis('equal')

plt.tight_layout()
plt.show()