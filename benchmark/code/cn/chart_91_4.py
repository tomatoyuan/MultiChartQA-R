import matplotlib.pyplot as plt
import numpy as np

# 购买频率分类
categories = ["半年以内", "半年至一年", "一年至两年", "两年以上"]
# 对应占比数据（模拟，可根据实际调整）
percentages = [24.4, 49.7, 23.6, 3.3]
# 合计占比（半年以内 + 半年至一年）
total_percent = sum(percentages[:2])

# 创建画布和子图
fig, ax = plt.subplots(figsize=(7, 5))

# 绘制柱状图
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color="#A4C639")

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# 添加合计占比标注（模拟蓝色虚线框及文字 ）
ax.text(1, total_percent + 3, f'合计{total_percent}%',
        ha='center', va='bottom', color='lightblue', fontweight='bold')
# 绘制蓝色虚线框（模拟范围 ）
x_min = x[0] - bar_width/2
x_max = x[1] + bar_width/2
y_min = 0
y_max = total_percent + 5
ax.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min],
        linestyle='--', color='lightblue', linewidth=1)

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 隐藏y轴刻度
ax.set_yticks([])
# 设置标题
ax.set_title("消费者近3年购买高端杯壶产品的平均频率", fontsize=14, fontweight="bold")

# 美化图表，隐藏顶部、右侧和底部边框
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()