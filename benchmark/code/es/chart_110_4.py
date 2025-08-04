import matplotlib.pyplot as plt
import numpy as np

# 维度定义
dimensiones = [
    "Creer que el uso de aplicaciones de audiolibros ayuda \na desarrollar hábitos de lectura y aumentar el conocimiento",
    "Creer que los audiolibros son fáciles de usar y tienen bajos requisitos \npara la habilidad de lectura (alfabetización y capacidad de comprensión lectora)",
    "Preferir escuchar audiolibros con altos datos \nexistentes (número de reproducciones, favoritos y reseñas)",
    "Preferir escuchar audiolibros completos"
]

# 数据
datos = np.array([
    [32.18, 36.84, 20.48, 9.44, 1.06],
    [30.32, 37.63, 18.88, 7.32, 5.85],
    [39.23, 30.85, 21.02, 6.91, 1.99],
    [35.11, 40.29, 12.63, 9.58, 2.39]
])

# 样式配置
colores = ['#FF5722', '#3F51B5', '#03A9F4', '#9C27B0', '#E91E63']
calificaciones = ["5 estrellas", "4 estrellas", "3 estrellas", "2 estrellas", "1 estrella"]

fig, ax = plt.subplots(figsize=(12, 8))
base = np.zeros(len(dimensiones))

# 绘制堆叠条形图
for i in range(datos.shape[1]):
    ax.bar(dimensiones, datos[:, i], bottom=base, color=colores[i], label=calificaciones[i])
    # 添加数值标注
    for j in range(len(dimensiones)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}', ha='center', va='center', fontsize=8)
    base += datos[:, i]

# 设置图例位置（外部左侧）
ax.legend(loc='center left', bbox_to_anchor=(-0.3, 0.5), fontsize=10)

# 其他样式调整
ax.set_ylabel('Proporción (%)', fontsize=12)
ax.set_title('Evaluación de la experiencia y sensaciones reales de los usuarios chinos de audiolibros en 2025', fontsize=14, pad=20)
plt.xticks(rotation=15, ha='right', fontsize=10)
plt.ylim(0, 110)  # 预留10%空间避免标注溢出
plt.tight_layout()
plt.show()