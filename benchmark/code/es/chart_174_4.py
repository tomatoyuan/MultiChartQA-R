import matplotlib.pyplot as plt

# 数据
etiquetas = ['Descuento de precio', 'Puntos de hotel', 'Otros']
tamaños = [58.7, 36.9, 4]
colores = ['#009C8A', '#A1D4A2', '#F3ECD9']

# 绘图
plt.figure(figsize=(8, 6))
plt.pie(
    tamaños,
    labels=etiquetas,
    colors=colores,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 14}
)

plt.title('Medidas de incentivo esperadas por los consumidores', fontsize=16, pad=20)
plt.axis('equal')  # Hacer que el gráfico circular sea un círculo perfecto
plt.tight_layout()
plt.show()