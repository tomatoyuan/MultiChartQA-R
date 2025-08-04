import matplotlib.pyplot as plt

# Datos
etiquetas = ["Una vez cada seis meses", "Una vez al año", "Una vez cada dos años", 
             "No se hace chequeo sin enfermedad", "Nunca ha realizado un examen físico", "Otro"]
tamaños = [3.94, 35.48, 39.41, 11.49, 9.52, 0.16]
# Colores correspondientes
colores = ['#FF7F27', '#4B53FF', '#32CD32', '#9C27B0', '#E91E63', '#1E90FF']

fig, ax = plt.subplots(figsize=(12, 10))  # 增大画布以容纳外侧标注

# Dibujar gráfico de donut con标注外侧
segmentos, textos, textos_automaticos = ax.pie(
    tamaños, 
    labels=etiquetas, 
    colors=colores, 
    autopct="%1.2f%%",  # 显示百分比
    startangle=90, 
    wedgeprops={"width": 0.4},
    pctdistance=1.15,   # 百分比距离圆心的距离（>1表示外侧）
    labeldistance=1.35  # 标签距离圆心的距离（大于pctdistance避免重叠）
)

# 调整百分比文本格式
for txt in textos_automaticos:
    txt.set_fontsize(10)
    txt.set_color('black')
    # 添加浅色背景框增强可读性
    txt.set_bbox(dict(boxstyle="round,pad=0.3", edgecolor="gray", facecolor="white", alpha=0.8))

# 调整标签格式
for txt in textos:
    txt.set_fontsize(10)
    txt.set_color('black')

# 标题设置
ax.set_title("Situación de exámenes físicos de los consumidores chinos en 2025", 
             fontsize=14, pad=80)

# 保证图形为正圆形
ax.axis('equal')

plt.tight_layout()
plt.show()