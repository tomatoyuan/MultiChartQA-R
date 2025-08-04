import matplotlib.pyplot as plt
import numpy as np

# 时间节点
years = ["2018.12", "2019.6", "2020.3", "2020.6", "2020.12"]
# 网络视听用户规模（亿人）
user_scale = [7.32, 7.8, 8.57, 9.01, 9.44]
# 网民使用率（%）
usage_rate = [88.3, 91.3, 94.8, 95.8, 95.4]

# 创建画布和子图，双y轴
fig, ax1 = plt.subplots(figsize=(8, 5))
ax2 = ax1.twinx()

ax1.set_ylim(0, 20)  # 用户规模Y轴（亿人）
ax2.set_ylim(75, 100)  # 使用率Y轴（%）

# 绘制网络视听用户规模柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax1.bar(x, user_scale, width=bar_width, color="#A4C639", label="网络视听用户规模（亿人）")

# 绘制网民使用率折线图
line, = ax2.plot(x, usage_rate, marker='o', color="#64B5F6", label="网民使用率（%）", linewidth=2)

# 添加用户规模数据标注
for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加使用率数据标注
for x_val, y_val in zip(x, usage_rate):
    ax2.annotate(f'{y_val}%',
                xy=(x_val, y_val),
                xytext=(0, 5),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom',
                color="#64B5F6")

# 设置x轴刻度和标签
ax1.set_xticks(x)
ax1.set_xticklabels(years)
# 设置y轴标签
ax1.set_ylabel("网络视听用户规模（亿人）", color="#A4C639")
ax2.set_ylabel("网民使用率（%）", color="#64B5F6")
# 设置标题
ax1.set_title("2018-2020年中国网络视听用户规模及使用情况", fontsize=14, fontweight="bold")

# 合并图例
handles, labels = ax1.get_legend_handles_labels()
handles.append(line)
labels.append(line.get_label())
ax1.legend(handles, labels, loc='upper left')

# 美化图表，隐藏顶部和右侧边框（针对 ax1 和 ax2 ）
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()