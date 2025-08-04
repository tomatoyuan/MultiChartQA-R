import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2021年Q1", "2022年Q1"]
usage_time = [316.8, 332.9]
growth_rate = 5.1

# 颜色：蓝橙对比
colors = ['#6495ED', '#FFA07A']

# 设置画布
fig, ax = plt.subplots(figsize=(8, 6))

# 对称柱状图的y轴为共享项目（这里设为单项“单机使用时间”）
y = ["单机单日有效时间"]
y_pos = np.arange(len(y))

# 横向柱长（2021为负，2022为正）
bar_2021 = [-usage_time[0]]
bar_2022 = [usage_time[1]]

# 绘制左右两侧的条形图
ax.barh(y_pos, bar_2021, color=colors[0], height=0.4, label=years[0])
ax.barh(y_pos, bar_2022, color=colors[1], height=0.4, label=years[1])

# 添加数据标签
ax.text(bar_2021[0] - 10, y_pos[0], f"{usage_time[0]}", va='center', ha='right', fontsize=10, color=colors[0])
ax.text(bar_2022[0] + 10, y_pos[0], f"{usage_time[1]}", va='center', ha='left', fontsize=10, color=colors[1])

# 增长率标注（中间箭头）
ax.annotate(f'+{growth_rate}%',
            xy=(0, y_pos[0]),
            xytext=(0, y_pos[0] + 0.3),
            ha='center',
            fontsize=11,
            color='green',
            arrowprops=dict(arrowstyle="->", color='green'))

# 设置 x 轴
ax.set_xticks(np.arange(-400, 401, 100))
ax.set_xlim(-400, 400)
ax.axvline(0, color='gray', linewidth=1)  # 中心线

# 设置 y 轴
ax.set_yticks(y_pos)
ax.set_yticklabels(y)
ax.set_title("mUserTracker：2021年Q1与2022年Q1单机单日使用时长对比（对称图）", fontsize=13, fontweight="bold")

# 图例
ax.legend(loc='upper right')

# 美化
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()