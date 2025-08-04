import matplotlib.pyplot as plt

# 数据
labels = [
    "午餐选择很少，选来选去都是那几家，都吃腻了",
    "担心外卖的健康问题，但没有外卖之外的其他选择",
    "经常由于工作繁忙，没时间吃午餐或者无法按时吃午餐",
    "想吃健康好吃的食物，但没有购买渠道或者价格昂贵"
]
sizes = [53, 44, 41, 40]
colors = ['#7ccf7c', '#7ccf7c', '#7ccf7c', '#7ccf7c']  # 绿色系

# 创建画布
plt.figure(figsize=(12, 8))

# 绘制条形图
bars = plt.barh(labels, sizes, color=colors, alpha=0.8)

# 添加数据标签
for bar in bars:
    width = bar.get_width()
    plt.text(width + 1, bar.get_y() + bar.get_height()/2,
             f'{width}%',
             ha='left', va='center', fontsize=12)

# 设置标题和标签
plt.title("时间短、选择少，费时费力也难保“入口健康”", fontsize=14, fontweight='bold')
plt.xlabel('百分比 (%)', fontsize=12)
plt.ylabel('问题类型', fontsize=12)

# 设置x轴范围
plt.xlim(0, 60)

# 添加网格线
plt.grid(axis='x', linestyle='--', alpha=0.7)

# 优化布局
plt.tight_layout()

# 显示图形
plt.show()