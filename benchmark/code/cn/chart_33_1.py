import matplotlib.pyplot as plt
import numpy as np

# 年份数据
years = np.arange(2017, 2030)
# 模拟的市场规模数据（大体趋势贴近，数值可根据实际微调）
market_size = [120, 125, 130, 133, 136, 139, 142, 145, 147, 149, 151, 153, 155]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制柱状图
bars = ax.bar(years, market_size, color='#6699cc', width=0.8)

# 在每个柱子上方添加数值标签
for bar, value in zip(bars, market_size):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
            f'{value}', ha='center', va='bottom')

# 标注两段的复合年增长率（CAGR），这里手动找位置标注，可根据实际微调坐标
ax.text(2019, 140, '2017 - 2023\nCAGR为1.85%', ha='center')
ax.text(2026, 140, '2024 - 2029E\nCAGR为1.31%', ha='center')

# 添加竖线分隔两段
ax.axvline(x=2024, color='gray', linestyle='--')

# 设置x轴刻度标签，2025年及以后的年份添加"E"标识
xtick_labels = [str(year) if year < 2025 else f"{year}E" for year in years]
ax.set_xticks(years)
ax.set_xticklabels(xtick_labels, rotation=45)

# 设置图表标题
ax.set_title('2014 - 2029年中国衣物清洁市场规模')

# 显示图表
plt.tight_layout()  # 调整布局避免标签被遮挡
plt.show()