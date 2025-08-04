import matplotlib.pyplot as plt
import numpy as np

# 日期标签
labels = ["腊月十五", "腊月十六", "腊月十七", "腊月十八", "腊月十九", "腊月廿十",
          "腊月廿一", "腊月廿二", "腊月廿三", "腊月廿四", "腊月廿五", "腊月廿六",
          "腊月廿七", "腊月廿八", "腊月廿九", "除夕"]
# 模拟的数据，大体体现高峰趋势，可根据实际微调
data = [5, 8, 10, 7, 9, 11, 12, 13, 14, 18, 15, 16, 17, 20, 19, 6]
# 标记高峰日期的索引（腊月廿四、腊月廿八 ，对应上面 labels 中的索引 9 和 13 ）
peak_indices = [9, 13]

x = np.arange(len(labels))  # x 轴位置
width = 0.6  # 柱状图宽度

fig, ax = plt.subplots(figsize=(10, 6))  # 创建画布和轴
# 绘制柱状图，大部分为一种颜色，高峰柱子用另一种颜色
bars = []
for i in range(len(x)):
    if i in peak_indices:
        bar = ax.bar(x[i], data[i], width, color='#e65142')  # 高峰颜色，近似原图表红色
    else:
        bar = ax.bar(x[i], data[i], width, color='#80cbc4')  # 其他柱子颜色，近似原图表青绿色
    bars.append(bar)

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right')

# 设置标题
ax.set_title('抢票双高峰：腊月廿八、廿四', fontsize=16, pad=20)

# 隐藏顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 添加一些装饰元素，模拟原图表的小太阳、云朵（简单示意，可根据需求细化）
import matplotlib.patches as patches
# 画小太阳
sun = patches.Circle((1, max(data) + 2), radius=1, color='yellow', alpha=0.8)
ax.add_patch(sun)
# 画云朵（简单矩形模拟，可更精细绘制）
cloud1 = patches.Rectangle((3, max(data) + 1.5), 2, 1, color='white', alpha=0.8)
cloud2 = patches.Rectangle((6, max(data) + 1), 2, 1, color='white', alpha=0.8)
ax.add_patch(cloud1)
ax.add_patch(cloud2)

plt.tight_layout()  # 自动调整布局
plt.show()