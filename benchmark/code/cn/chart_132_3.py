import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ["2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"]
quantities = [177, 201, 238, 290, 341, 377, 457, 474, 438]

x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制柱状图，使用类似毕业帽的图案（简化为橙色柱状图，可替换为自定义图案）
bars = ax.bar(x, quantities, color='orange')

# 添加数值标注，在柱子上方
for i, quantity in enumerate(quantities):
    ax.text(i, quantity + 10, f'{quantity}', ha='center', va='bottom')

# 设置坐标轴
ax.set_ylabel('数量（万人）')
ax.set_xlabel('年份')
ax.set_xticks(x)
ax.set_xticklabels(years)

ax.set_title('2016-2024年中国研究生考生规模')

plt.tight_layout()
plt.show()