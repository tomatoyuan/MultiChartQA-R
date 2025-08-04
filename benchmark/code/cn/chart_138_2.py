import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]
# 各类产量数据（单位：万吨），顺序：蔬菜、肉类、水产品
vegetable = [67434.2, 69192.7, 70346.7, 72102.6, 74912.9, 77549.0, 80000.0]
meat = [8628.3, 8654.4, 8624.6, 7758.8, 7748.4, 8990.0, 9328.4]
aquatic = [6379.5, 6445.3, 6457.7, 6480.4, 6549.0, 6690.0, 6549.0]

x = np.arange(len(years))  # x 轴坐标
bar_width = 0.3  # 每个类别柱状图宽度

fig, ax = plt.subplots(figsize=(12, 8))

# 绘制蔬菜产量柱状图（最底部）
ax.bar(x, vegetable, width=bar_width, label='蔬菜产量（万吨）', color='#CD5C5C')
# 绘制肉类产量柱状图（在蔬菜产量之上）
ax.bar(x, meat, width=bar_width, bottom=vegetable, label='肉类产量（万吨）', color='#FFA07A')
# 绘制水产品产量柱状图（在肉类产量之上）
ax.bar(x, aquatic, width=bar_width, bottom=np.array(vegetable) + np.array(meat), 
       label='水产品总产量（万吨）', color='#FFDAB9')

# 添加各类产量数值标注
# 标注蔬菜产量
for i, v in enumerate(vegetable):
    ax.text(i, v / 2, f'{v}', ha='center', va='center', color='white', fontweight='bold')
# 标注肉类产量
for i, (v, m) in enumerate(zip(vegetable, meat)):
    ax.text(i, v + m / 2, f'{m}', ha='center', va='center', color='white', fontweight='bold')
# 标注水产品产量
for i, (v, m, a) in enumerate(zip(vegetable, meat, aquatic)):
    bottom_sum = v + m
    ax.text(i, bottom_sum + a / 2, f'{a}', ha='center', va='center', color='white', fontweight='bold')

ax.set_ylabel('产量（万吨）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
ax.set_title('2016-2022年中国火锅食材原料产量')

plt.tight_layout()
plt.show()