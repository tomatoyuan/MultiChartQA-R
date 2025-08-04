import matplotlib.pyplot as plt
import numpy as np

# 类别名称
categories = ["硅水凝胶", "水凝胶", "硬性高透性", "混合材质", "我不了解"]
# 各类别对应不同隐形眼镜类型的占比数据
data = np.array([
    [20, 20, 16],
    [18, 18, 12],
    [12, 10, 12],
    [6, 6, 6],
    [8, 8, 4]
])

# 计算每个类别的总数值
total_values = data.sum(axis=1)

# 根据总数值排序（降序）
sorted_indices = np.argsort(total_values)[::-1]

# 重新排列类别和数据
categories = [categories[i] for i in sorted_indices]
data = data[sorted_indices]

# 转置数据，让每列对应一种隐形眼镜类型
data = data.T

# 不同类型隐形眼镜的标签和对应颜色
labels = ["透明隐形眼镜", "彩色隐形眼镜", "硬性隐形眼镜"]
colors = ["#4CAF50", "#FF9800", "#F44336"]  

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))  # 适当增加宽度以容纳标签

# 绘制堆积条形图
bottom = np.zeros(len(categories))
for i in range(len(labels)):
    bars = ax.barh(categories, data[i], left=bottom, color=colors[i], label=labels[i])
    
    # 为每个条形添加数据标签
    for bar, value in zip(bars, data[i]):
        if value > 0:  # 只显示非零值
            ax.text(
                bar.get_x() + bar.get_width()/2,  # x 位置：条形中心
                bar.get_y() + bar.get_height()/2, # y 位置：条形中心
                f"{value}%",                      # 显示值和百分号
                ha='center', va='center',         # 水平和垂直居中
                color='white', fontweight='bold', # 白色文字，加粗
                fontsize=9                        # 字体大小
            )
    
    bottom += data[i]

# 添加注释文本（调整位置避免遮挡标签）
annotation_text = "硅水凝胶多为需戴镜8-12小时\n的重度使用人群\n(TGI>100)"
ax.text(0.7, 0.85, annotation_text, transform=ax.transAxes,
        bbox=dict(facecolor='orange', alpha=0.8), fontsize=10)

# 设置图表属性
ax.yaxis.set_label_position("right")
ax.set_ylabel("隐形眼镜类型", fontsize=12)
ax.set_xlabel("占比（%）", fontsize=12)
ax.set_title("不同材质隐形眼镜佩戴者的类型分布", fontsize=14, pad=15)
ax.legend(loc='lower right')  # 调整图例位置
plt.tight_layout()
plt.show()