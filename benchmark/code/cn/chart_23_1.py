import matplotlib.pyplot as plt
import numpy as np

# 数据
cities = ["深圳", "北京", "广州", "武汉", "长沙"]
ranking = [1, 2, 3, 4, 5]

# 创建水平条形图
plt.figure(figsize=(10, 6))
bars = plt.barh(cities, ranking, color='#6CB4EE')

# 在每个条形上添加排名数字
for i, v in enumerate(ranking):
    plt.text(v + 0.1, i, str(v), va='center', fontsize=12)

# 添加标题和标签
plt.title('赶场相亲城市百行榜', fontsize=16, pad=15)
plt.xlabel('排名', fontsize=12, labelpad=10)
plt.ylabel('城市', fontsize=12, labelpad=10)

# 设置x轴范围
plt.xlim(0, max(ranking) + 1)

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()