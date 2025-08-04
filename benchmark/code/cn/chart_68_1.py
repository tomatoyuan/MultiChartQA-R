import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 设置风格与配色
plt.style.use("ggplot")
sns.set_palette("Set2")

# 数据
categories = ["PaaS厂商收入", "资源成本", "研发成本", "毛利润"]
data = [100, 33, 37, 30]
colors = sns.color_palette("flare", len(data))  # 鲜艳渐变色系

# 极坐标图（雷达图变体）——仅一个维度，用饼图模拟也可以
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# 极坐标角度
angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
# 闭合图形
data += data[:1]
angles += angles[:1]

# 绘图
ax.fill(angles, data, color=colors[0], alpha=0.25)
ax.plot(angles, data, color=colors[0], linewidth=2, linestyle="-", marker='o')

# 添加数据标注
for angle, value, label in zip(angles[:-1], data[:-1], categories):
    ax.text(
        angle,
        value - 5,  # 往外偏移一点防止与图形重合，可调节
        f"{value}%",
        ha='center',
        va='center',
        fontsize=10,
        color='black',
        fontweight='bold'
    )

# 设置类别标签
categories += categories[:1]
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=11)

# 设置标题
plt.title("RTC PaaS厂商盈利能力分布（极坐标视图）", fontsize=14, fontweight="bold", pad=20)

# 配置坐标轴范围
ax.set_rlabel_position(30)
ax.set_yticks([25, 50, 75, 100])
ax.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=10)
ax.grid(color="gray", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()