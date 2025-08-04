import matplotlib.pyplot as plt

# 数据定义（更贴近原图精确位置）
labels = ['肤感', '通真', '隐形', '自然', '裸感']
x_sales_ratio = [0.05, 0.03, 0.04, 0.55, 0.75]  # 销售额占比
y_growth_rate = [2.8, 0.05, -0.02, 0.1, 0.12]   # 同比增速
sizes = [500, 320, 300, 350, 360]  # 气泡大小人为设置以接近原图视觉权重

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制气泡图
ax.scatter(
    x_sales_ratio,
    y_growth_rate,
    s=sizes,
    c='#FF8888',
    alpha=0.75,
    edgecolors='white',
    linewidth=1.5
)

# 添加文本标签
for i in range(len(labels)):
    ax.text(x_sales_ratio[i], y_growth_rate[i] + 0.03, labels[i],
            ha='center', va='bottom', fontsize=12)

# 坐标轴设置
ax.set_title('MAT2024线上淘系“光腿神器”功能卖点细分\n颜色自然度相关', fontsize=15, weight='bold')
ax.set_xlabel('销售额占比', fontsize=12)
ax.set_ylabel('同比', fontsize=12)

# 设置刻度格式与范围
ax.set_xlim(0, 0.9)
ax.set_ylim(-0.3, 3.2)
ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
ax.set_xticklabels(['0%', '20%', '40%', '60%', '80%'])
ax.set_yticks([-1, 0, 1, 2, 3])
ax.set_yticklabels(['-100%', '0%', '100%', '200%', '300%'])

# 添加网格与背景
ax.grid(True, linestyle='--', alpha=0.4)
ax.set_facecolor('#fcfcfc')

# 数据来源说明
source_text = "数据来源：魔镜市场情报数据；MAT2024：2023.07-2024.06"
plt.figtext(0.5, -0.05, source_text, wrap=True, horizontalalignment='center', fontsize=9, color='gray')

plt.tight_layout()
plt.show()