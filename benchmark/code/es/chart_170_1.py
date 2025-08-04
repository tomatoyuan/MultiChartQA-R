import matplotlib.pyplot as plt

# 数据
etiquetas = ['Leve', 'Moderado', 'Moderadamente grave', 'Grave', 'Ninguno']
tamaños = [29.3, 25.3, 17.7, 11.9, 15.8]
colores = ['#65D1DD', '#6449A6', '#FF7B9C', '#FFA01B', '#F5C447']
separacion = (0.05, 0.05, 0.05, 0.05, 0.05)  # Hacer que cada parte se resalte ligeramente

# 绘图
fig, ax = plt.subplots(figsize=(8, 6))
porciones, textos, textos_automaticos = ax.pie(
    tamaños, labels=etiquetas, autopct='%1.1f%%',
    startangle=90, counterclock=False, colors=colores,
    explode=separacion, textprops={'fontsize': 12}, wedgeprops={'width': 0.3}
)

ax.set_title('Evaluación del estado de depresión de los usuarios en la evaluación psicológica', fontsize=16, pad=20)
ax.axis('equal')  # Mantener el gráfico circular
plt.tight_layout()
plt.show()