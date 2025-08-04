import matplotlib.pyplot as plt
import numpy as np

# 空间痛点数据
space_pain = {
    "第三排使用时，后备箱空间不足": 30.0,
    "第三排进出不方便": 28.3,
    "空间使用灵活性弱、利用率低": 25.0,
    "第三排空间小": 23.8,
    "储物空间不合理/数量少": 22.9,
    "第三排放倒后，后备箱空间不足": 20.8,
    "前排空间小": 16.3,
    "第二排空间小": 11.7
}
# 驾乘舒适性痛点数据
comfort_pain = {
    "第三排座椅无法开窗": 29.9,
    "音响效果差": 27.7,
    "减震/避震效果差": 26.4,
    "隔热性能差": 25.5,
    "空调效果差": 22.1,
    "车内噪音大": 21.6,
    "上下车不方便": 18.6,
    "座椅舒适性差": 18.2
}

# 提取标签和数值
space_labels = list(space_pain.keys())
space_values = list(space_pain.values())
comfort_labels = list(comfort_pain.keys())
comfort_values = list(comfort_pain.values())

# 配色（自由搭配，可调整）
bar_colors = ["#A4C639", "#87CEEB", "#FFD700", "#FF69B4", 
              "#90EE90", "#B0C4DE", "#FFA07A", "#D8BFD8"]

# 创建双栏布局画布
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=False)

# 绘制空间痛点柱状图
x1 = np.arange(len(space_labels))
ax1.barh(x1, space_values, color=bar_colors, height=0.6)
ax1.set_yticks(x1)
ax1.set_yticklabels(space_labels, fontsize=9)
ax1.set_title("MPV【空间】痛点\n(N=240)", fontsize=12, fontweight="bold")
# 添加空间痛点标注
for i, val in enumerate(space_values):
    ax1.annotate(f'{val}%', (val + 1, i), va='center', fontsize=8)

# 绘制驾乘舒适性痛点柱状图
x2 = np.arange(len(comfort_labels))
ax2.barh(x2, comfort_values, color=bar_colors, height=0.6)
ax2.set_yticks(x2)
ax2.set_yticklabels(comfort_labels, fontsize=9)
ax2.set_title("MPV【驾乘舒适性】痛点\n(N=231)", fontsize=12, fontweight="bold")
# 添加驾乘舒适性痛点标注
for i, val in enumerate(comfort_values):
    ax2.annotate(f'{val}%', (val + 1, i), va='center', fontsize=8)

# 美化：隐藏顶部、右侧边框
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.grid(axis='x', linestyle='--', alpha=0.3)  # 增加辅助网格

plt.tight_layout()
plt.show()