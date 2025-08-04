# 图表3：重新绘制横向柱状图，优化颜色方案与标签可视化

import matplotlib.pyplot as plt

factores = [
    "Se ajusta bien, \nsin apretar ni abrochar",
    "Modela el trasero y\n mejora el contorno",
    "Tela de alta calidad, \nsuave y delicada con la piel",
    "Alta elasticidad y \ngran capacidad de adaptación",
    "Modelado con presión suave, \nadelgazante y ajustado"
]
porcentajes = [38, 33, 32, 30, 28]

colores = ['#ec407a', '#f06292', '#f48fb1', '#f8bbd0', '#fce4ec']  # Rosa degradado

fig, ax = plt.subplots(figsize=(8, 5))
barras = ax.barh(factores, porcentajes, color=colores, edgecolor='gray')

# Agregar etiquetas de valores
for barra in barras:
    ancho = barra.get_width()
    ax.text(ancho + 1, barra.get_y() + barra.get_height()/2,
            f'{ancho}%', va='center', fontsize=10)

# Título y mejoras visuales
ax.set_title("Los 5 factores más influyentes en la compra de leggings de tiburón", fontsize=14)
ax.invert_yaxis()  # El más alto arriba
ax.set_xlim(0, 45)
ax.set_xlabel("Porcentaje (%)")
plt.tight_layout()
plt.show()