import matplotlib.pyplot as plt
import numpy as np

# 标题与内容列表
title = "艾滋病知识及预防关注度"
items = [
    "艾滋病传播途径",
    "艾滋病初期症状",
    "艾滋病活多久",
    "艾滋病疫苗",
    "艾滋病初期症状图片",
    "艾滋病宣传材料",
    "艾滋病图片",
    "艾滋病潜伏期的三大表现"
]
# 根据原图红色长条长度比例设置进度值
progress = np.array([0.95, 0.85, 0.85, 0.85, 0.75, 0.74, 0.70, 0.70])  

# 创建画布与轴
fig, ax = plt.subplots(figsize=(6, 4), facecolor="#F5F5F5")
# 隐藏坐标轴
ax.axis("off")  

# 绘制标题
plt.text(
    0.03, 0.95, title, 
    fontsize=16, fontweight="bold", fontfamily="SimSun"
)

# 逐个绘制条目
for i, (text, p) in enumerate(zip(items, progress), start=1):
    # 绘制进度条背景
    rect_bg = plt.Rectangle(
        (0.03, 0.9 - 0.1 * i), 0.94, 0.07, 
        facecolor="#F8D7DA", edgecolor="white"
    )
    ax.add_patch(rect_bg)
    # 绘制进度条填充（使用不同的进度值）
    rect_fill = plt.Rectangle(
        (0.03, 0.9 - 0.1 * i), 0.94 * p, 0.07, 
        facecolor="#F1C2C6", edgecolor="white"
    )
    ax.add_patch(rect_fill)
    # 绘制进度百分比文本
    plt.text(
        0.03 + 0.94 * p + 0.01, 0.9 - 0.1 * i + 0.035, f"{p*100:.0f}%", 
        fontsize=10, va="center", color="#8B0000"
    )
    # 绘制序号圆圈
    circle = plt.Circle(
        (0.02, 0.9 - 0.1 * i + 0.035), 0.03, 
        facecolor=f"C{i-1}", edgecolor="white"
    )
    ax.add_artist(circle)
    # 绘制序号文本
    plt.text(
        0.02, 0.9 - 0.1 * i + 0.032, f"{i}", 
        fontsize=10, color="white", ha="center", va="center"
    )
    # 绘制条目文本
    plt.text(
        0.07, 0.9 - 0.1 * i + 0.035, text, 
        fontsize=12, va="center"
    )

plt.tight_layout(pad=2)
plt.show()