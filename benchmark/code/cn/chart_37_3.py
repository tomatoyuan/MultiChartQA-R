import matplotlib.pyplot as plt
import numpy as np

# 数据准备（大体模拟，可根据实际微调）
categories = [
    ["冲锋衣裤", "运动羽绒服"],
    ["唐装/中式服装", "非遗/织染服饰"],
    ["二次元衬衫", "二次元连衣裙"]
]
groups = ["户外运动", "国风服饰", "二次元服饰"]
values = [
    [27, 46],
    [123, 78],
    [200, 93]
]

# 颜色配置（接近原图表浅色调）
bar_colors = ["#C9B8A7", "#B8A090"]  # 可根据实际需求微调

# 绘图初始化
fig, axes = plt.subplots(3, 1, figsize=(6, 10), sharex=False)  # 调整高度以容纳标题
plt.subplots_adjust(top=0.85, hspace=0.5)  # 调整顶部间距

# 添加主标题和副标题
plt.suptitle("兴趣圈层相关服饰类目增速", fontsize=16, fontweight="bold", y=0.95)
plt.title("各品类销售额同比增长百分比", fontsize=12, y=1.05)  # 副标题

for i in range(3):
    # 绘制横向条形图
    axes[i].barh(categories[i], values[i], color=bar_colors)
    axes[i].set_title(groups[i], fontsize=12, fontweight="bold")  # 设置分组标题
    
    # 添加数据标签（增长率 +% 格式）
    for j, val in enumerate(values[i]):
        axes[i].text(val + 5, categories[i][j], f"{val}%+", 
                     va="center", fontsize=9, color="black")

# 统一设置坐标轴（隐藏 x 轴刻度，让图表更简洁）
for ax in axes:
    ax.set_xticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

plt.show()