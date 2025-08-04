import matplotlib.pyplot as plt
import numpy as np

# 年份
years = [2007, 2013, 2017, 2020]
diabetes_rates = [9.7, 10.4, 11.2, 11.9]
cholesterol_rates = [3.1, 6.0, 8.0, 8.2]

# 颜色设定
diabetes_color = "#6ab04c"      # 温和橄榄绿
cholesterol_color = "#45aaf2"   # 浅亮蓝

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 面积图绘制
ax.fill_between(
    years, diabetes_rates, 
    color=diabetes_color, alpha=0.3, label="成人糖尿病患病率（%）"
)
ax.plot(years, diabetes_rates, color=diabetes_color, linewidth=2.5, marker="o")

ax.fill_between(
    years, cholesterol_rates, 
    color=cholesterol_color, alpha=0.3, label="成人高胆固醇血症患病率（%）"
)
ax.plot(years, cholesterol_rates, color=cholesterol_color, linewidth=2.5, marker="o")

# 添加数据标注
for x, y in zip(years, diabetes_rates):
    ax.text(x, y + 0.4, f"{y}%", ha='center', va='bottom', fontsize=10, color=diabetes_color)

for x, y in zip(years, cholesterol_rates):
    ax.text(x, y - 0.8, f"{y}%", ha='center', va='top', fontsize=10, color=cholesterol_color)

# 设置坐标轴
ax.set_xticks(years)
ax.set_ylabel("患病率（%）")
ax.set_title("2007-2020年中国成人糖尿病及高胆固醇血症患病率", fontsize=14, fontweight='bold')

# 图例
ax.legend(loc="upper left", fontsize=10)

# 美化
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
ax.grid(alpha=0.2)

plt.tight_layout()
plt.show()