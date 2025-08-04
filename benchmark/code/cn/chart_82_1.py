import matplotlib.pyplot as plt
import numpy as np

# 年份
years = np.arange(2015, 2022)

# 数据（示例，可根据实际微调）
# 居民健康素养水平（%）
health_literacy = [10.4, 11.6, 14.3, 17.1, 19.5, 23.2, 25.4]
# 健康生活方式与行为素养水平（%）
lifestyle_literacy = [10.3, 9.8, 14.2, 17.0, 19.2, 26.4, 28.1]

# 创建画布
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制居民健康素养水平折线（上方标注）
health_line, = ax.plot(years, health_literacy, marker='o', color='#A4C639', label='居民健康素养水平（%）', linewidth=2)
# 绘制健康生活方式与行为素养水平折线（下方标注）
lifestyle_line, = ax.plot(years, lifestyle_literacy, marker='o', color='#64B5F6', label='健康生活方式与行为素养水平（%）', linewidth=2)

# 为居民健康素养水平折线添加上方标注
for x, y in zip(years, health_literacy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # 上方偏移
                textcoords='offset points',
                ha='center',
                va='bottom',
                color='#A4C639')

# 为健康生活方式与行为素养水平折线添加下方标注
for x, y in zip(years, lifestyle_literacy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, -10),  # 下方偏移
                textcoords='offset points',
                ha='center',
                va='top',
                color='#64B5F6')

# 设置坐标轴与标题
ax.set_xlabel('年份')
ax.set_ylabel('素养水平（%）')
ax.set_title('2015-2021年中国居民健康素养水平', fontsize=14, fontweight='bold')
ax.set_xticks(years)
ax.set_xticklabels(years)

# 添加图例
ax.legend(loc='upper left')

# 美化：隐藏顶部、右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()