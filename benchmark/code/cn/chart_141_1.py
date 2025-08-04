import matplotlib.pyplot as plt
import numpy as np

# 数据
labels = ["营养补充", "作息调理", "孕产知识", "备孕同房技巧", "孕产产品", "产后恢复", "其他"]
percentages = [88.7, 78.1, 67.9, 66.0, 52.8, 48.3, 2.3]
colors = ["#FF9933"] * len(labels)  # 统一橙色，贴近原图风格

x = np.arange(len(labels))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制条形图
bars = ax.barh(x, percentages, color=colors)
ax.set_ylabel('关注内容')
ax.set_xlabel('关注占比（%）')
ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.invert_yaxis()  # 让“营养补充”在最上方，贴近原图顺序

# 添加数值标注
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height() / 2, 
            f'{width}%', ha='left', va='center')

ax.set_title('2023年中国备孕人群关注内容分布')

plt.tight_layout()
plt.show()