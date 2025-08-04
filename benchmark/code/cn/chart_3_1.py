import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["营销数字化转型非常重要", "数字化时代，运营和数据同等重要", 
          "数字化时代，品牌仍然非常重要", "数字化时代，搭建营销平台非常重要"]
very_agree = np.array([64, 68, 78, 53])  # 非常同意占比
agree = np.array([33, 29, 19, 40])  # 比较同意占比
disagree = np.array([2, 2, 2, 5])  # 不太同意占比
strong_disagree = np.array([1, 1, 1, 2])  # 很不同意占比

# 颜色方案（使用更现代的配色）
colors = ['#E63946', '#F1FAEE', '#A8DADC', '#1D3557']  # 从红色到深蓝色的渐变

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))  # 调整画布大小

# 绘制横向堆积条形图
bottom = np.zeros(len(labels))
for i, (data, label, color) in enumerate(zip(
    [strong_disagree, disagree, agree, very_agree],
    ['很不同意', '不太同意', '比较同意', '非常同意'],
    colors
)):
    bars = ax.barh(labels, data, left=bottom, color=color, label=label, 
                  alpha=0.9, edgecolor='w', linewidth=0.5)
    
    # 在每个条形上标注百分比
    for bar, value in zip(bars, data):
        if value > 2:  # 只显示足够宽的条形上的文本
            ax.text(
                bar.get_x() + bar.get_width()/2, 
                bar.get_y() + bar.get_height()/2,
                f"{value}%", 
                ha='center', 
                va='center',
                color='black' if i < 2 else 'white',  # 根据背景色调整文本颜色
                fontweight='bold',
                fontsize=10
            )
    
    bottom += data

# 设置标题
ax.set_title('2021年广告主数字化营销观点调查结果', fontsize=16, fontweight='bold', pad=20)

# 设置标签
ax.set_xlabel('百分比 (%)', fontsize=12, labelpad=10)
# ax.set_ylabel('观点', fontsize=12, labelpad=10)  # 移除y轴标签

# 设置网格线
ax.grid(axis='x', linestyle='--', alpha=0.7)

# 设置x轴范围
ax.set_xlim(0, 100)

# 美化图例 - 放置在标题下方
fig.legend(loc='upper center', bbox_to_anchor=(0.6, 0.95), ncol=4, frameon=False, fontsize=10)

# 调整边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 调整布局，为图例腾出空间
plt.subplots_adjust(top=0.85)  # 减小顶部边距
plt.tight_layout()

# 显示图表
plt.show()