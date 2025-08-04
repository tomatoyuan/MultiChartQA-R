import matplotlib.pyplot as plt
import numpy as np

# Nombres de las plataformas de comercio electrónico
plataformas = ["Pinduoduo", "Tmall/Taobao", "JD.com", "Suning.com", "Juhuasuan", "Jingxi", "Suning Pinpin",
               "Hema Fresh", "Missfresh", "Douyin", "Kuaishou"]
# Proporción de cada calificación
datos = np.array([
    [24.72, 42.16, 22.62, 7.11, 3.39],
    [38.13, 29.56, 23.26, 7.27, 1.78],
    [32.96, 36.03, 16.31, 12.12, 2.58],
    [25.85, 33.12, 23.75, 13.73, 3.55],
    [25.69, 37.96, 23.10, 9.05, 4.20],
    [28.76, 34.57, 22.77, 10.02, 3.88],
    [25.85, 39.10, 21.00, 11.47, 2.58],
    [29.24, 38.77, 21.65, 7.59, 2.73],
    [28.59, 37.96, 21.82, 9.05, 2.58],
    [27.63, 39.74, 22.78, 6.46, 3.39],
    [29.56, 36.19, 21.81, 9.37, 3.07]
])
# Colores correspondientes a las calificaciones
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
puntuaciones = ["5 Puntos", "4 Puntos", "3 Puntos", "2 Puntos", "1 Punto"]

# 增大画布宽度以容纳外侧图例
fig, ax = plt.subplots(figsize=(16, 8))
base = np.zeros(len(plataformas))

for i in range(datos.shape[1]):
    ax.bar(plataformas, datos[:, i], bottom=base, color=colores[i], label=puntuaciones[i])
    # Agregar anotaciones numéricas
    for j in range(len(plataformas)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}',
                ha='center', va='center', fontsize=7)
    base += datos[:, i]

ax.set_ylabel('Proporción (%)', fontsize=10)
ax.set_title('Satisfacción de los consumidores chinos con la experiencia general al comprar productos agrícolas en varias plataformas de comercio electrónico en 2025',
             fontsize=12, pad=20)

# 将图例放在右侧外侧
ax.legend(
    loc='center left',  # 图例自身锚点为左中部
    bbox_to_anchor=(1.02, 0.5),  # 定位在右侧边界外2%，垂直居中
    fontsize=10,
    title="Puntuaciones",  # 图例标题
    title_fontsize=12
)

plt.xticks(rotation=45, ha='right', fontsize=9)  # 调整x轴标签角度和大小
plt.ylim(0, 110)  # 预留顶部空间避免标注溢出
plt.tight_layout()
plt.subplots_adjust(right=0.85)  # 调整右侧边距为图例留出空间
plt.show()