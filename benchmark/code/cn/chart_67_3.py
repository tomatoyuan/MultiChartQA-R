import matplotlib.pyplot as plt
import numpy as np

# 城市名称
cities = ["北京", "上海", "广州", "深圳"]
# 核心商圈空置率数据
core_vacancy = [9.8, 9.9, 7.6, 18.8]
# 优质写字楼全市空置率数据
city_vacancy = [17.1, 16.6, 11.9, 16.6]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 5))

# 绘制核心商圈空置率折线
core_line, = ax.plot(cities, core_vacancy, marker='o', color='#A4C639', label='核心商圈空置率（%）', linewidth=2)
# 绘制优质写字楼全市空置率折线
city_line, = ax.plot(cities, city_vacancy, marker='o', color='#64B5F6', label='优质写字楼全市空置率（%）', linewidth=2)

# 添加数据标注（核心商圈）
for x, y in zip(cities, core_vacancy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # 标注位置调整
                textcoords='offset points',
                ha='center', va='bottom',
                color='#A4C639')

# 添加数据标注（优质写字楼全市）
for x, y in zip(cities, city_vacancy):
    ax.annotate(f'{y}%',
                xy=(x, y),
                xytext=(0, 5),  # 标注位置调整
                textcoords='offset points',
                ha='center', va='bottom',
                color='#64B5F6')

# 设置标题
ax.set_title('2021年中国一线城市优质写字楼市场空置率', fontsize=14, fontweight='bold')
# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()