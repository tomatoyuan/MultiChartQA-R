import matplotlib.pyplot as plt
import numpy as np

# 年龄情况数据
age_categories = ["24岁以下", "25-34岁", "35-44岁", "45岁及以上"]
age_percentages = [29.3, 41.5, 21.6, 7.6]
# 婚姻情况数据
marriage_categories = ["未婚", "已婚有子女", "已婚无子女"]
marriage_percentages = [60.7, 34.1, 5.2]
# 自由配色（可调整）
bar_color = "#A4C639"  # 柱状图颜色
pie_colors = ["#A4C639", "#87CEEB", "#FFD700"]  # 饼图颜色

# 创建双栏布局画布
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# 绘制年龄情况横向柱状图
y = np.arange(len(age_categories))
ax1.barh(y, age_percentages, color=bar_color, height=0.6)
ax1.set_yticks(y)
ax1.set_yticklabels(age_categories)
ax1.set_title("2022年中国足球球迷年龄情况", fontsize=12, fontweight="bold")
# 添加年龄标注
for i, val in enumerate(age_percentages):
    ax1.annotate(f'{val}%', (val + 1, i), va='center', fontsize=9)

# 绘制婚姻情况饼图
wedges, texts, autotexts = ax2.pie(
    marriage_percentages, 
    labels=marriage_categories, 
    colors=pie_colors, 
    autopct='%1.1f%%', 
    startangle=90
)
ax2.set_title("2022年中国足球球迷婚姻情况", fontsize=12, fontweight="bold")
# 美化饼图标注（颜色、大小）
for text, autotext in zip(texts, autotexts):
    text.set_color('black')
    autotext.set_color('black')
    autotext.set_fontsize(9)

# 美化：隐藏边框
for ax in [ax1, ax2]:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()