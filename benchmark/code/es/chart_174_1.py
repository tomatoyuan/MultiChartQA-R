import matplotlib.pyplot as plt

# 数据
etiquetas = ['Hoteles sin promoción', 'Con carteles de advertencia', 'Con carteles promocionales']
tamaños = [88, 7, 5]
colores = ['#058b83', '#dbe5c4', '#abd7a6']  # Colores personalizados, consistentes con el estilo de la gráfica

# Generar el gráfico circular
plt.figure(figsize=(7, 5))
porciones, textos, textos_automaticos = plt.pie(
    tamaños,
    labels=etiquetas,
    autopct='%1.0f%%',
    startangle=90,
    colors=colores,
    textprops={'fontsize': 14}
)

# Establecer el título
plt.title('Proporción de diferentes promociones del \nnuevo decreto de reducción del uso de plásticos en hoteles', fontsize=16)

# Mostrar la gráfica
plt.tight_layout()
plt.show()