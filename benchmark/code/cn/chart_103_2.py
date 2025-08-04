import matplotlib.pyplot as plt
import numpy as np

# 1. 提取图表数据
years = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
# 各类预制菜市场规模（亿元）
meat = [714, 829, 977, 1224, 1544, 2069, 2668, 3289]        # 肉禽
seafood = [648, 733, 856, 1047, 1237, 1595, 2089, 2576]     # 水产
vegetable = [350, 480, 588, 676, 835, 1186, 1416, 1625]     # 蔬菜
# 总规模（亿元）
total = [1712, 2042, 2421, 2947, 3616, 4850, 6173, 7490]
# 同比增长率（%）
growth = [19.3, 18.6, 21.7, 22.7, 34.2, 27.3, 21.3]

# 2. 绘制组合图表（柱状图+折线图）
x = np.arange(len(years))  # x轴坐标
width = 0.2  # 柱子宽度

fig, ax1 = plt.subplots(figsize=(14, 8))

# 绘制三类预制菜的堆积柱状图
bottom = np.zeros(len(years))
for i, (data, label, color) in enumerate(zip(
    [meat, seafood, vegetable], 
    ['肉禽预制菜', '水产预制菜', '蔬菜类预制菜'], 
    ['#FF5722', '#FF9800', '#FFC107']
)):
    bars = ax1.bar(x, data, width, bottom=bottom, label=label, color=color)
    # 标注各类预制菜的数值
    for j, bar in enumerate(bars):
        height = bar.get_height()
        if height > 50:  # 只标注高度足够的柱子，避免拥挤
            ax1.text(
                bar.get_x() + bar.get_width()/2., 
                bottom[j] + height/2,
                f'{data[j]}',
                ha='center', va='center',
                color='black', fontsize=8
            )
    bottom += data

# 标注总规模数值
for i, val in enumerate(total):
    ax1.text(x[i], total[i] + 80, f'{val}', ha='center', fontsize=10, color='#333')

# 配置左轴（市场规模）
ax1.set_ylabel('市场规模（亿元）', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 新建右轴绘制同比增长率折线
ax2 = ax1.twinx()
ax2.plot(x[:-1], growth, marker='o', color='#FDD835', label='同比增长（%）', linewidth=2)

# 标注增长率数值
for i, val in enumerate(growth):
    ax2.text(x[i], val + 1, f'{val}%', ha='center', fontsize=9, color='#FDD888')

ax2.set_ylabel('同比增长（%）', fontsize=12, color='#FDD888')
ax2.tick_params(axis='y', labelcolor='#FDD888')
ax2.legend(loc='center right')

# 3. 图表整体配置
plt.title('2019-2026年中国预制菜行业市场规模及预测', fontsize=14, pad=20)
plt.tight_layout()
plt.show()