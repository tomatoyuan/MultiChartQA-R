import matplotlib.pyplot as plt

# 数据
etiquetas = ['Relacionado con \n'
             'materias primas', 'Relacionado con\n la marca', 'Relacionado con\n estética médica', 'Otros']
tamaños = [46.6, 24.7, 16.4, 12.3]

# 更粉嫩的淡色系（使用柔和的粉红色调）
colores = ['#FADADD', '#F9C6D0', '#F7B0C4', '#F59EB7']

# 绘制饼图
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=90,
    colors=colores,
    textprops={'fontsize': 12, 'color': 'black'}
)

# 添加标题和数据来源
plt.title('Proporción de eventos de inversión en diferentes campos en 2023', fontsize=14, pad=20)
plt.figtext(0.1, -0.01,
            '*Rango de extracción de datos: Eventos de inversión y financiación\n'
            ' relacionados con la industria de cosméticos locales de China', ha='left', fontsize=10)

# 保证饼图为圆形
ax.axis('equal')

plt.tight_layout()
plt.show()