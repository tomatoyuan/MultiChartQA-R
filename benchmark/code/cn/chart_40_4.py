import matplotlib.pyplot as plt

# 数据
channels = ['线上', '同时选线上线下', '线下']
percentages = [89, 68, 74]

# 创建画布
plt.figure(figsize=(10, 6))

# 绘制条形图
bars = plt.bar(channels, percentages, color=['#ff9999', '#66b3ff', '#99ff99'], alpha=0.8)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}%',
             ha='center', va='bottom', fontsize=12)

# 设置标题和标签
plt.title('消费者会选择列入购物决策的渠道占比', fontsize=15)
plt.xlabel('渠道类型', fontsize=12)
plt.ylabel('占比 (%)', fontsize=12)

# 设置y轴范围
plt.ylim(0, 100)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 优化布局
plt.tight_layout()

# 显示图形
plt.show()