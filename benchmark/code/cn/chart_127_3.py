import matplotlib.pyplot as plt
import numpy as np

# 公司名称
companies = [
    "上汽集团", "比亚迪", "长城汽车", "长安汽车", 
    "广汽集团", "一汽解放", "福田汽车", "江淮汽车", 
    "中国重汽", "赛力斯"
]
# 2022 年营收（百亿元）
revenue_2022 = [74.41, 42.41, 13.73, 12.13, 11.03, 3.83, 4.64, 3.66, 2.88, 3.41]
# 2023 年营收（百亿元）
revenue_2023 = [74.47, 60.23, 17.32, 15.13, 12.97, 6.39, 5.61, 4.50, 4.21, 3.58]
# 增长率（%）
growth_rates = [0.09, 42.04, 26.12, 24.78, 17.62, 66.71, 20.78, 23.07, 45.96, 5.09]

x = np.arange(len(companies))

fig, ax = plt.subplots(figsize=(14, 8))

# 绘制 2022 年营收柱状图（橙色）
ax.bar(x - 0.2, revenue_2022, width=0.4, color='orange', label='2022年营收（百亿元）')
# 绘制 2023 年营收柱状图（蓝色）
ax.bar(x + 0.2, revenue_2023, width=0.4, color='blue', label='2023年营收（百亿元）')

# 添加 2022 年营收数值标注
for i, rev in enumerate(revenue_2022):
    ax.text(x[i] - 0.2, rev + 0.5, f'{rev}', ha='center', va='bottom')

# 添加 2023 年营收数值标注
for i, rev in enumerate(revenue_2023):
    ax.text(x[i] + 0.2, rev + 0.5, f'{rev}', ha='center', va='bottom')

# 添加增长率数值标注（右侧）
for i, rate in enumerate(growth_rates):
    ax.text(len(companies) + 0.5, x[i], f'{rate}%', ha='center', va='center', color='black')
    # 绘制向上箭头（简化为文本箭头，或用 matplotlib.patches 绘制图形箭头）
    ax.text(len(companies) + 0.2, x[i], '↑', ha='center', va='center', color='orange', fontsize=16)

ax.set_ylabel('营收（百亿元）')
ax.set_xlabel('公司名称')
ax.set_xticks(x)
ax.set_xticklabels(companies)
ax.legend()
ax.set_title('2023年中国A股新能源汽车整车制造上市公司营业收入前十')

# 调整 x 轴范围，给增长率标注留出空间
ax.set_xlim(-0.5, len(companies) + 1)

plt.tight_layout()
plt.show()