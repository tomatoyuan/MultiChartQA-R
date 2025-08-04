import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2017", "2018", "2019", "2020", "2021"]
# 电池成本数据（元），[锂离子电池成本，铅酸电池成本]
battery_costs = np.array([[1800, 400], [1400, 400], [1300, 400], [1150, 400], [1050, 400]])

# 自由配色（可调整），分别对应锂离子电池和铅酸电池
colors = ["#6839C6", "#87CEEB"]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制分组柱状图，x轴位置
x = np.arange(len(years))  
# 柱状图宽度
width = 0.35  

# 绘制锂离子电池成本柱状图
li_ion_bars = ax.bar(x - width/2, battery_costs[:, 0], width, color=colors[0], label="锂离子电池（元）")
# 绘制铅酸电池成本柱状图
lead_acid_bars = ax.bar(x + width/2, battery_costs[:, 1], width, color=colors[1], label="铅酸电池（元）")

# 添加锂离子电池成本标注
for bar in li_ion_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 添加铅酸电池成本标注
for bar in lead_acid_bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置标题
ax.set_title("2017-2021年中国两轮电动车电池成本", fontsize=14, fontweight="bold")
# 添加图例
ax.legend()

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()