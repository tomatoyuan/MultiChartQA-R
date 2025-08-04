import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022e"]
# 模拟销量占比数据（贴近原图）
percentages = [5.4, 7.5, 12.7, 14.7, 20.6, 23.4, 27.3]
# 自由配色（可调整，示例用绿色系+蓝色系）
bar_color = "#87CEEB"  # 可替换为其他颜色如 "#FF8C00"

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制柱状图
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color=bar_color)

# 添加数据标注
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar_width/2, height),
                xytext=(0, 3),  # 标注位置：上方偏移 3
                textcoords="offset points",
                ha='center', va='bottom',
                color='black')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(years)
# 设置y轴刻度（0-30%）
ax.set_ylim(0, 30)
# 设置标题
ax.set_title("2016-2022年中国两轮锂电车销量占比及预测", fontsize=14, fontweight="bold")

# 美化：隐藏顶部、右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()