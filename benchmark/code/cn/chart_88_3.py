import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022e", "2023e", "2024e", "2025e", "2026e"]
# 现零糖饮品市场规模（亿元），数据与图表一致
market_size = [32, 42, 67, 97, 118, 143, 168, 195, 231, 269, 301]
# yoy（%），数据与图表一致，添加2016年的0%（因无同比数据）
yoy = [0, 28.8, 61.3, 43.7, 22.1, 21.4, 17.5, 16.2, 17.9, 16.7, 11.7]  # 修正：添加2016年的0%

# 创建画布
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_ylim(0, 600)

# 绘制柱状图（市场规模，绿色）
ax1.bar(years, market_size, color="#A4C639", label="现零糖饮品市场规模（亿元）")
ax1.set_ylabel("市场规模（亿元）", color="#A4C639")
ax1.tick_params(axis='y', labelcolor="#A4C639")

# 创建次坐标轴绘制折线图（yoy，蓝色）
ax2 = ax1.twinx()

ax2.set_ylim(-120,110)

ax2.plot(years, yoy, marker='o', color="#87CEEB", label="yoy(%)", linewidth=2)
ax2.set_ylabel("yoy(%)", color="#87CEEB")
ax2.tick_params(axis='y', labelcolor="#87CEEB")

# 添加数据标注（市场规模）
for x, y in zip(np.arange(len(years)), market_size):
    ax1.text(x, y + 5, f'{y}', ha='center', va='bottom', color='black')

# 添加数据标注（yoy）
for x, y in zip(np.arange(len(years)), yoy):
    ax2.text(x, y + 1, f'{y}%', ha='center', va='bottom', color='black')

# 添加 CAGR 说明文本
cagr_texts = [
    (0.2, 0.85, "CAGR=36.1%"),
    (0.7, 0.85, "CAGR=15.6%")
]
for x, y, text in cagr_texts:
    ax1.text(x, y, text, transform=ax1.transAxes, fontsize=12, ha='center', va='bottom')

# 设置标题
ax1.set_title('2016-2026年中国无糖饮料市场规模', fontsize=14, fontweight='bold')

# 合并图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# 美化：隐藏顶部、右侧边框
for spine in ['top', 'right']:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()