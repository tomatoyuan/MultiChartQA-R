import matplotlib.pyplot as plt
import numpy as np

# 数据准备
elements = [
    "中国传统元素、国潮风格", "生肖元素", "创新创意", 
    "极简主义", "科技元素", "网红时髦", "漫画二次元", "其他"
]
percentages = [62.2, 41.6, 38.7, 37.4, 28.9, 23.8, 19.8, 0.3]

# 计算每个元素对应的方块数量（每个方块代表约3%）
block_counts = [int(p / 3) + (1 if p % 3 > 1.5 else 0) for p in percentages]

# 创建更宽的图表以适应中文文本
fig, ax = plt.subplots(figsize=(16, 7))
ax.set_xlim(0, max(block_counts) + 20)  # 增加x轴范围以容纳长文本
ax.set_ylim(0, len(elements) * 1.5)
ax.set_axis_off()  # 隐藏坐标轴

# 绘制橙色方块和标注
for i, (element, perc, blocks) in enumerate(zip(elements, percentages, block_counts)):
    # 绘制方块
    for j in range(blocks):
        ax.add_patch(plt.Rectangle((j + 1, i * 1.5 + 0.3), 0.8, 0.8, color='orange'))
    
    # 绘制元素名称（右移以避免重叠）
    ax.text(
        blocks + 4,  # 增加x坐标值使文本右移
        i * 1.5 + 0.7, 
        element, 
        fontsize=12, 
        va='center'
    )
    
    # 绘制百分比数值（进一步右移并调整对齐）
    ax.text(
        blocks + 4 + len(element) * 0.6,  # 根据文本长度动态调整位置
        i * 1.5 + 0.7, 
        f'{perc}%', 
        ha='left',  # 左对齐避免与元素名称重叠
        va='center', 
        fontsize=12, 
        color='orange'
    )

# 设置标题
ax.set_title('2023年中国新春礼盒消费者产品元素偏好', fontsize=16, y=1.05)

plt.tight_layout()
plt.show()