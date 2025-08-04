import matplotlib.pyplot as plt
import numpy as np

# AI 眼镜品牌
brands = ["华为", "小米", "谷歌", "雷鸟创新", "Meta", "行者无疆", "雷神科技", "逸文科技", "星际魅族", "百度"]
# 对应品牌占比（%），数据大体模拟，可根据实际调整
percentages = [23.8, 17.3, 15.3, 7.7, 6.5, 5.8, 4.0, 3.0, 2.9, 2.2]

x = np.arange(len(brands))  # x 轴刻度位置

fig, ax = plt.subplots()

# 绘制条形图，颜色设置为接近的绿色
bars = ax.bar(x, percentages, color='greenyellow')

# 添加标题
ax.set_title('整体被访者听说过的AI眼镜品牌 (TOP10)')

# 设置 x 轴刻度标签
ax.set_xticks(x)
ax.set_xticklabels(brands, rotation=45, ha='right')  # 旋转标签，避免重叠

# 为每个条形添加数值标签
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 垂直偏移 3 个点
                textcoords="offset points",
                ha='center', va='bottom')

# 设置 y 轴标签（可根据需要添加）
ax.set_ylabel('品牌占比 (%)')

plt.tight_layout()  # 自动调整布局，避免标签重叠
plt.show()