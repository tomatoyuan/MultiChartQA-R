import matplotlib.pyplot as plt

# 数据
categorias = ['Normas locales', 'Normas de asociaciones', 'Normas empresariales']
valores = [27, 289, 90]

# Dibujar el gráfico
fig, ax = plt.subplots(figsize=(6, 6))
barras = ax.bar(categorias, valores, color='red')

# Agregar etiquetas de valores
for barra in barras:
    valor_y = barra.get_height()
    ax.text(barra.get_x() + barra.get_width() / 2, valor_y + 5, f'{int(valor_y)}',
            ha='center', va='bottom', fontsize=12)

# Agregar título y etiquetas
ax.set_title('Distribución de normas relacionadas con platos prefabricados en China en 2024', fontsize=14)
ax.set_ylabel('Unidad: ítems', fontsize=12)
ax.set_ylim(0, 320)


plt.tight_layout()
plt.show()