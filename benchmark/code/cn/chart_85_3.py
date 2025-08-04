import matplotlib.pyplot as plt
import numpy as np

# -------------------- 数据定义 --------------------
years = ["2006-2016", "2017", "2018", "2019", "2020", "2021", "合计"]
x = np.arange(len(years))
quantities = [6, 7, 18, 40, 47, 76, 194]

# 为阶梯图准备 step 数据
x_step = np.repeat(x, 2)[1:]
y_step = np.repeat(quantities, 2)[:-1]

# 配色（渐变方案）
fill_color = "#b2dfdb"      # 填充区域主色
line_color = "#00796b"      # 曲线颜色
point_color = "#009688"     # 标注点颜色

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# -------------------- 绘制阶梯面积图 --------------------
ax.step(x, quantities, where='mid', color=line_color, linewidth=2.5, label="年度建成数量")
ax.fill_between(x_step, y_step, step='pre', alpha=0.3, color=fill_color)

# -------------------- 添加数据点和标注 --------------------
ax.plot(x, quantities, "o", color=point_color)

for i, val in enumerate(quantities):
    ax.text(
        x[i], val + 5,
        str(val),
        ha='center', va='bottom',
        fontsize=10,
        fontweight='bold',
        color=point_color
    )

# -------------------- 坐标轴与标签 --------------------
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")
ax.set_ylabel("中国加氢站数量（座）", fontsize=11)
ax.set_ylim(0, max(quantities) + 30)

# -------------------- 图例与标题 --------------------
ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="white")
ax.set_title("2006-2021年我国每年建成加氢站数量", fontsize=14, fontweight='bold', pad=20)

# -------------------- 美化 --------------------
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()