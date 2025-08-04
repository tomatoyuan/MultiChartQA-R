import matplotlib.pyplot as plt
import numpy as np

# Factores
factores = ["Apariencia", "Servicio post - venta", "Calidad", "Marca y reputación", "Rareza", "Precio"]
# Proporción de cada calificación (1 - 5 puntos), en el orden de 5 puntos, 4 puntos, 3 puntos, 2 puntos, 1 punto
datos = np.array([
    [30.79, 21.06, 17.59, 16.67, 13.89],
    [28.94, 24.31, 21.05, 15.28, 10.42],
    [27.08, 26.85, 18.06, 15.51, 12.50],
    [25.93, 28.70, 18.29, 14.81, 12.27],
    [23.61, 30.56, 18.52, 14.58, 12.73],
    [17.59, 29.40, 21.30, 16.20, 15.51]
])

# Colores correspondientes a las puntuaciones
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
puntuaciones = ["5 puntos", "4 puntos", "3 puntos", "2 puntos", "1 punto"]

fig, ax = plt.subplots(figsize=(12, 8))
base = np.zeros(len(factores))

for i in range(datos.shape[1]):
    ax.bar(factores, datos[:, i], bottom=base, color=colores[i], label=puntuaciones[i])
    # Agregar anotaciones numéricas
    for j in range(len(factores)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}', ha='center', va='center', fontsize=8)
    base += datos[:, i]

# Configurar图例位置（右侧外侧）
ax.legend(
    loc='center left',  # 图例自身的锚点为左侧中心
    bbox_to_anchor=(1.02, 0.5),  # 锚点位置：右侧边界外2%宽度，垂直居中
    fontsize=10,
    title="Puntuaciones",  # 图例标题
    title_fontsize=12
)

# 其他样式调整
ax.set_ylabel('Proporción (%)', fontsize=12)
ax.set_title('Calificación de varios factores de los consumidores de figuritas chinas para las figuritas en 2025', fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylim(0, 110)  # 预留10%空间避免标注溢出顶部
plt.tight_layout()  # 自动调整布局，避免元素重叠
plt.subplots_adjust(right=0.85)  # 调整右侧边距，为图例留出空间
plt.show()