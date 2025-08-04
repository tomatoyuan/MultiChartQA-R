import matplotlib.pyplot as plt
import numpy as np

# 数据
años = ['Hasta dic. 2022', 'Hasta dic. 2023']
población = [52000, 54800]  # 单位：万（Unidad: diez mil）
tasa_penetración = [48.8, 49.9]  # 单位：%（Unidad: %）

# 设置画布
fig, ax1 = plt.subplots(figsize=(7, 4))

# 绘制柱状图：人数（左轴）
ancho_barra = 0.4
x = np.arange(len(años))
barras = ax1.bar(x, población, ancho_barra, color='#4CAF50', label='Número de personas (diez mil)')
ax1.set_ylabel('Número de personas (diez mil)', fontsize=12)
ax1.set_ylim(50000, 56000)
ax1.set_xticks(x)
ax1.set_xticklabels(años, fontsize=11)
ax1.tick_params(axis='y', labelsize=10)

# 添加柱状图数值标签
for i, v in enumerate(población):
    ax1.text(i, v + 200, f"{v}", ha='center', va='bottom', fontsize=10)

# 设置第二个坐标轴：渗透率（右轴）
ax2 = ax1.twinx()
ax2.plot(x, tasa_penetración, color='blue', marker='o', linewidth=2.5, label='Tasa de penetración (%)')
ax2.set_ylabel('Tasa de penetración en el total de usuarios de Internet (%)', fontsize=12)
ax2.set_ylim(48.25, 50.50)
ax2.tick_params(axis='y', labelsize=10)

# 添加渗透率数值标签
for i, v in enumerate(tasa_penetración):
    ax2.text(i, v - 0.2, f"{v}%", color='blue', ha='center', va='bottom', fontsize=15, fontweight='bold')

# 标题与图例
plt.title('Estadísticas del tamaño de la población de usuarios de \npedidos de comida a domicilio en línea y su tasa de penetración', fontsize=14, pad=15)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=10)

# 数据来源标注

plt.tight_layout()
plt.show()