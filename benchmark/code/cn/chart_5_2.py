import matplotlib.pyplot as plt
import numpy as np

# 构造横轴日期数据，与原图表的日期对应
dates = ["2.1", "2.3", "2.5", "2.7", "2.9", "2.11", 
         "2.13", "2.15", "2.17", "2.19", "2.21", 
         "2.23", "2.25", "2.27"]
# 构造近似原图表趋势的纵轴搜索关注度数据
values = [150000, 200000, 250000, 380000, 370000, 390000, 
          360000, 430000, 440000, 410000, 560000, 
          430000, 420000, 340000]  

# 创建画布，设置尺寸
fig, ax = plt.subplots(figsize=(10, 6))  

# 绘制折线图，设置蓝色线条，调整线宽让视觉效果更贴近
line, = ax.plot(dates, values, color="#4285F4", linewidth=2.5)  

# 设置图表标题，字体加粗
ax.set_title("2月奶粉行业搜索关注度趋势", fontsize=16, fontweight="bold")  

# 设置纵轴标签和范围、刻度
ax.set_ylabel("关注度", fontsize=12)
ax.set_ylim(100000, 600000)  
ax.set_yticks([100000, 200000, 300000, 400000, 500000, 600000])  
# 格式化纵轴刻度显示，加上逗号分隔
ax.set_yticklabels([f"{tick:,}" for tick in ax.get_yticks()])  

# 设置横轴刻度，使用构造的日期数据
ax.set_xticks(dates)  

# 添加网格线，虚线样式，增加图表可读性
ax.grid(linestyle="--", color="gray", alpha=0.3)  

# 在数据点上添加标注
for x, y in zip(dates, values):
    # 格式化数值，添加千位分隔符
    value_str = f"{y:,}"
    
    # 调整标注位置，避免重叠
    if y > 400000:  # 上方标注
        ax.annotate(value_str, 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, 10), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#4285F4", alpha=0.8))
    else:  # 下方标注
        ax.annotate(value_str, 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, -15), 
                    ha='center',
                    fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#4285F4", alpha=0.8))

# 突出显示最大值和最小值
max_value = max(values)
min_value = min(values)
for x, y in zip(dates, values):
    if y == max_value or y == min_value:
        ax.scatter(x, y, color='red', s=50, zorder=5)
        ax.annotate(f"{y:,}", 
                    (x, y), 
                    textcoords="offset points",
                    xytext=(0, 15), 
                    ha='center',
                    fontsize=10,
                    fontweight='bold',
                    color='red',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", alpha=0.8))

# 添加图例
ax.legend([line], ["搜索关注度"], loc='upper left')

# 添加数据来源说明
plt.figtext(0.1, 0.01, '数据来源：虚构数据，仅作示例', ha="left", fontsize=9, bbox={"facecolor":"white", "alpha":0.5, "pad":5})

# 优化布局，避免元素重叠
plt.tight_layout()  

# 显示图表
plt.show()