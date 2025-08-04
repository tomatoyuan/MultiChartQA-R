import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ["公园/游乐园", "酒店", "旅行社", "旅游局"]
data_24 = [169.2, 89.2, 895.0, 137.1]
data_25 = [585.6, 70.6, 913.2, 149.1]
growth_rates = ["同比+246.1%", "同比-20.9%", "同比+2.0%", "同比+8.8%"]

# 颜色
color_24 = "#4bb7e6"
color_25 = "#a5d65d"

# 创建画布
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

# ✅ 统一 y 轴最大值（为避免重叠，稍微放大）
y_max = max(max(data_24), max(data_25)) + 80

for i in range(4):
    ax = axes[i]
    x = np.arange(2)
    bars = ax.bar(
        x, 
        [data_24[i], data_25[i]], 
        width=0.6, 
        color=[color_24, color_25], 
        edgecolor='white'
    )
    
    # 添加数据标注（略微靠近柱顶）
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2, 
            height + 5, 
            f'{height:.1f}', 
            ha='center', 
            va='bottom', 
            fontsize=9
        )
    
    # 添加增长率（放在柱顶稍上方）
    peak = max(data_24[i], data_25[i])
    ax.text(
        0.5, 
        peak + 25, 
        growth_rates[i], 
        ha='center', 
        va='bottom', 
        fontsize=10, 
        color="#333333", 
        fontweight='bold'
    )
    
    # 设置x轴标签
    ax.set_xticks(x)
    ax.set_xticklabels(["24年五一假期周", "25年五一假期周"], fontsize=9)
    
    # 隐藏边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # 设置标题
    ax.set_title(categories[i], fontsize=11, fontweight='bold')
    
    # 设置统一y轴上限
    ax.set_ylim(0, y_max)

# 整体标题
fig.suptitle(
    "AdTracker 2024 & 2025 年五一假期（1-5日）旅游相关在线广告投入指数对比",
    fontsize=13,
    fontweight='bold',
    y=1.03
)

# ✅ 调整整体布局，避免 suptitle 被遮挡
plt.tight_layout(rect=[0, 0, 1, 0.96])  # 留出顶部空间给标题
plt.show()