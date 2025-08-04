import matplotlib.pyplot as plt
import numpy as np

# Indicadores de servicios de exámenes físicos
indicadores = ["Conveniencia de la cita para el examen físico", "Profesionalismo y completitud del contenido del informe de examen físico", "Tiempo para obtener el informe de examen físico", 
              "Tiempo de espera para el examen físico", "Entorno del lugar del examen físico", "Equipamiento del centro de exámenes físicos", "Velocidad de respuesta y resolución de problemas durante el examen físico"]
# Proporciones de cada puntuación (5 puntos, 4 puntos, 3 puntos, 2 puntos, 1 punto), en el orden de los indicadores, cada indicador corresponde a una sublista
datos = np.array([
    [33.39, 38.66, 19.60, 7.08, 1.27],
    [32.85, 38.66, 18.15, 8.53, 1.81],
    [31.58, 31.94, 21.78, 13.07, 1.63],
    [26.50, 35.93, 25.59, 9.98, 2.00],
    [32.49, 41.38, 17.06, 7.44, 1.63],
    [41.74, 38.11, 15.98, 3.60, 0.54],
    [28.31, 45.01, 14.34, 9.44, 2.90]
])
# Colores correspondientes a las puntuaciones
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63']
puntuaciones = ["5 puntos", "4 puntos", "3 puntos", "2 puntos", "1 punto"]

fig, ax = plt.subplots(figsize=(14, 8))  # 适当增大宽度以容纳外侧图例
base = np.zeros(len(indicadores))

for i in range(datos.shape[1]):
    ax.bar(indicadores, datos[:, i], bottom=base, color=colores[i], label=puntuaciones[i])
    # Agregar anotaciones numéricas en el centro de cada bloque apilado
    for j in range(len(indicadores)):
        ax.text(j, base[j] + datos[j, i] / 2, f'{datos[j, i]:.2f}', 
                ha='center', va='center', fontsize=8)
    base += datos[:, i]

ax.set_ylabel('Proporción (%)', fontsize=10)
ax.set_title('Puntuaciones de satisfacción de los consumidores chinos para varios indicadores de servicios de exámenes físicos en 2025', fontsize=12, pad=20)

# 将图例放在右侧外侧
ax.legend(
    loc='center left',  # 图例自身的锚点为左中部
    bbox_to_anchor=(1.02, 0.5),  # 锚点位置：右侧边界外2%宽度，垂直居中
    fontsize=10,
    title="Puntuaciones",  # 图例标题
    title_fontsize=12
)

plt.xticks(rotation=15, ha='right', fontsize=9)  # 适当减小x轴标签字体
plt.ylim(0, 110)  # 预留顶部空间避免标注溢出
plt.tight_layout()
plt.subplots_adjust(right=0.82)  # 调整右侧边距，为图例留出空间
plt.show()