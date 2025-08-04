import matplotlib.pyplot as plt

# 数据
# Datos
etiquetas = ['Para el/la pareja', 'Para los niños', 'Para los amigos', 'Para los mayores', 'Para sí mismo/a']
tamaños = [60, 14, 10, 8, 8]

# 饼图颜色可自定义，也可使用默认
# Los colores del gráfico circular se pueden personalizar o usar los predeterminados
colores = ['#FF5A7D', '#FF8DA1', '#FFA7B5', '#FFC3CB', '#FFE1E7']

# 绘制饼图
# Dibujar un gráfico circular
fig, ax = plt.subplots()
ax.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.0f%%',
    startangle=90,
    colors=colores,
    textprops={'fontsize': 12}
)

# 保持圆形
# Mantener la forma circular
ax.axis('equal')
plt.title('Distribución de destinatarios de regalos en San Valentín 2023\n (Proporción de UV de transacciones de destinatarios de regalos en la población de regalos)', fontsize=14, pad=20)
plt.tight_layout()
plt.show()