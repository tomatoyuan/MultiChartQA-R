import matplotlib.pyplot as plt
import numpy as np

# 年份
years = ["2016-12", "2017-12", "2018-12", "2019-12", "2020-12", "2021-12", "2022-12", "2023-12"]
# 外卖用户规模（万人）
user_scale = [20856, 34338, 40601, 39780, 41883, 54416, 52118, 54454]
# 占整体网民的比例（渗透率，%）
penetration_rate = [28.5, 44.5, 49.0, 44.0, 42.3, 52.7, 48.8, 49.9]

x = np.arange(len(years))

fig, ax1 = plt.subplots(figsize=(10, 6))

# 绘制外卖用户规模柱状图
ax1.bar(x, user_scale, color='orange', label='外卖用户规模（万人）')
ax1.set_ylabel('外卖用户规模（万人）')
ax1.set_xlabel('年份')
ax1.set_xticks(x)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left')

# 创建双轴，绘制渗透率折线图
ax2 = ax1.twinx()
ax2.plot(x, penetration_rate, marker='o', color='brown', label='占整体网民的比例（%）')
ax2.set_ylabel('渗透率（%）')
ax2.legend(loc='upper right')

# 添加外卖用户规模数值标注
for i, scale in enumerate(user_scale):
    ax1.text(i, scale + 500, f'{scale}', ha='center', va='bottom')

# 添加渗透率数值标注
for i, rate in enumerate(penetration_rate):
    ax2.text(i, rate + 1, f'{rate}%', ha='center', va='bottom')

ax1.set_title('2016-2023年中国网上外卖用户规模及渗透率')

plt.tight_layout()
plt.show()