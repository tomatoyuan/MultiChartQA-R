import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2020年", "2022年", "2023年", "2025年预估"]
# 对应年份的人均咖啡年饮用杯数
data = [9.1, 11.3, 16.74, 20]
# 为2025年预估设置不同颜色，这里用橙色近似，可根据实际需求微调RGB值
colors = ["#1f77b4", "#1f77b4", "#1f77b4", "#ff7f0e"]  

x = np.arange(len(years))  # 横坐标位置

fig, ax = plt.subplots()
# 绘制柱状图
bars = ax.bar(x, data, color=colors)  

# 设置横坐标刻度标签
ax.set_xticks(x)
ax.set_xticklabels(years)

# 添加标题
ax.set_title("中国人均咖啡年饮用量（杯数）")

# 为每个柱子添加数据标签
for bar, value in zip(bars, data):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f"{value}",
            ha='center', va='bottom')

# 显示图表
plt.show()