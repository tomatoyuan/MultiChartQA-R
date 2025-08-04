import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["买后发现不需要", "商品和描述不符", "尺寸型号等不符", "假冒伪劣商品", "客服态度恶劣", "赠品质量恶劣", "售后服务困难", "快递延迟"]
values = [10, 3, 2, 1, 1, 1, 0.5, 0.3]  # 数值为模拟，可根据实际调整

x = np.arange(len(labels))  # x轴刻度位置

# 创建图表
fig, ax = plt.subplots()
rects = ax.bar(x, values, color=['pink', 'pink', 'pink', 'orange', 'orange', 'orange', 'lightblue', 'lightblue'])

# 设置x轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# 添加标题
ax.set_title('双十一后悔原因', fontsize=14, fontweight='bold')

# 给每个柱子添加数值标签
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 像素的偏移
                textcoords="offset points",
                ha='center', va='bottom')

# 显示图表
plt.tight_layout()
plt.show()