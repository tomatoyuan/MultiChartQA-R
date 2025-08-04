import matplotlib.pyplot as plt
import numpy as np

# 数据定义（与原图结构对应，可微调数值）
years = ["2018", "2019", "2020", "2021", "2022", "2023"]
incomes = [28228, 30733, 32189, 35128, 36883, 39218]  # 模拟数据，可替换为真实值

# 颜色配置（贴近原图绿色系）
bar_color = "#81c784"

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制柱状图
x = np.arange(len(years))
bars = ax.bar(x, incomes, color=bar_color, width=0.6, edgecolor="white", linewidth=1)

# 添加数值标注
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 500,  # 向上偏移，避免遮挡
        f"{height}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# 美化图表
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12, color="#424242")
ax.set_ylabel("人均可支配收入（元）", fontsize=12, color="#424242")

# 隐藏顶部和右侧边框
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 添加标题
ax.set_title(
    "2018年-2023年全国居民人均可支配收入（元）",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# 调整布局
plt.tight_layout()

plt.show()