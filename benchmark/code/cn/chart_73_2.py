import matplotlib.pyplot as plt
import numpy as np

# 数据设置
categories = ["每月5次或以上", "每月3-4次", "每月1-2次", "每季度使用1-2次", "每年使用1-2次"]
data = [8.0, 33.0, 41.5, 14.5, 3.0]
# 要框选的类别索引（“每月3-4次”“每月1-2次”“每季度使用1-2次” 对应索引 1、2、3 ）
boxed_indices = [1, 2, 3]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制水平条形图
y = np.arange(len(categories))
bar_height = 0.6
bars = ax.barh(y, data, height=bar_height, color="#A4C639", edgecolor="white")

# 绘制蓝色虚线框
min_y = min(y[i] - bar_height / 2 for i in boxed_indices)
max_y = max(y[i] + bar_height / 2 for i in boxed_indices)
min_x = 0
max_x = max(data[i] for i in boxed_indices)
rect = plt.Rectangle((min_x, min_y), max_x, max_y - min_y, 
                     fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rect)

# 添加数据标注
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  
                textcoords="offset points",
                ha='left', va='center')

# 设置y轴刻度和标签
ax.set_yticks(y)
ax.set_yticklabels(categories)
# 隐藏x轴刻度
ax.set_xticks([])
# 设置标题
ax.set_title("用户常用即配平台的使用频次", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  
plt.show()