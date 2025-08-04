import matplotlib.pyplot as plt
import numpy as np

# 年份及假期分类
years = ["2020年", "2021年", "2022年"]
holidays_2020 = ["清明", "五一", "端午", "中秋&国庆", "春节"]
holidays_2021 = ["春节", "清明", "五一", "端午", "中秋", "国庆"]
holidays_2022 = ["春节", "清明", "五一", "端午"]  # 4个假期

# 修正数据：补充2022年端午节的数据
revenue_2020 = [19.3, 32.3, 31.2, 69.9, 56.7]
revenue_2021 = [77.0, 74.8, 78.6, 59.9, 56.3, 68.0]
revenue_2022 = [36.2, 44.0, 65.6, 58.0]  # 补充端午节数据

person_times_2020 = [38.6, 47.2, 50.9, 79.0, 94.5]
person_times_2021 = [103.2, 98.7, 87.2, 70.1, 73.9, 85.0]
person_times_2022 = [68.0, 66.8, 86.8, 75.0]  # 补充端午节数据

# 创建画布和子图
fig, axes = plt.subplots(1, 3, figsize=(12, 5), sharey=False)
fig.suptitle("2020-2022年各假期旅游数据恢复情况", fontsize=14, fontweight="bold")

# 绘制2020年子图
ax_2020 = axes[0]
x_2020 = np.arange(len(holidays_2020))
ax_2020.plot(x_2020, revenue_2020, marker='o', color='#A4C639', label='旅游收入恢复至2019年同期（%）', linewidth=2)
ax_2020.plot(x_2020, person_times_2020, marker='o', color='#64B5F6', label='旅游人次恢复至2019年同期（%）', linewidth=2)
ax_2020.set_xticks(x_2020)
ax_2020.set_xticklabels(holidays_2020)
ax_2020.set_title("2020年")
# 添加数据标注
for x, y1, y2 in zip(x_2020, revenue_2020, person_times_2020):
    ax_2020.annotate(f'{y1}%', (x, y1), textcoords="offset points", xytext=(0, 5), ha='center')
    ax_2020.annotate(f'{y2}%', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', color='#64B5F6')

# 绘制2021年子图
ax_2021 = axes[1]
x_2021 = np.arange(len(holidays_2021))
ax_2021.plot(x_2021, revenue_2021, marker='o', color='#A4C639', linewidth=2)
ax_2021.plot(x_2021, person_times_2021, marker='o', color='#64B5F6', linewidth=2)
ax_2021.set_xticks(x_2021)
ax_2021.set_xticklabels(holidays_2021, rotation=45)  # 旋转标签避免重叠
ax_2021.set_title("2021年")
# 添加数据标注
for x, y1, y2 in zip(x_2021, revenue_2021, person_times_2021):
    ax_2021.annotate(f'{y1}%', (x, y1), textcoords="offset points", xytext=(0, 5), ha='center')
    ax_2021.annotate(f'{y2}%', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', color='#64B5F6')

# 绘制2022年子图（修正后）
ax_2022 = axes[2]
x_2022 = np.arange(len(holidays_2022))  # x长度为4
ax_2022.plot(x_2022, revenue_2022, marker='o', color='#A4C639', linewidth=2)  # y长度也为4
ax_2022.plot(x_2022, person_times_2022, marker='o', color='#64B5F6', linewidth=2)  # y长度也为4
ax_2022.set_xticks(x_2022)
ax_2022.set_xticklabels(holidays_2022)
ax_2022.set_title("2022年")
# 添加数据标注
for x, y1, y2 in zip(x_2022, revenue_2022, person_times_2022):
    ax_2022.annotate(f'{y1}%', (x, y1), textcoords="offset points", xytext=(0, 5), ha='center')
    ax_2022.annotate(f'{y2}%', (x, y2), textcoords="offset points", xytext=(0, -15), ha='center', color='#64B5F6')

# 右侧添加额外信息（2022上半年对比）
ax_info = fig.add_axes([0.82, 0.8, 0.15, 0.2])
ax_info.axis('off')
ax_info.text(0, 1, "2022上半年 VS. 2021上半年", fontsize=10, fontweight='bold')
ax_info.text(0, 0.8, "城镇居民国内旅游人次 -16.6%", color='#64B5F6', fontsize=9)
ax_info.text(0, 0.6, "农村居民国内旅游人次 -35.4%", color='#E57373', fontsize=9)

# 合并图例（在第一个子图）
lines, labels = axes[0].get_legend_handles_labels()
fig.legend(lines, labels, loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.1))

# 美化图表，隐藏子图顶部和右侧边框
for ax in axes:
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)

plt.subplots_adjust(top=0.85, bottom=0.2)  # 调整标题和图例位置
plt.show()