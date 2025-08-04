import matplotlib.pyplot as plt
import numpy as np

# 数据准备
# 到店业务各城市类型占比（假设从左到右对应一线城市、新一线城市、二线城市、三线及以下城市 ，根据柱状图视觉判断）
store_service = [28.1, 32.4, 31.4, 8.1]
# 到家业务各城市类型占比（同理对应）
home_service = [23.0, 32.9, 35.9, 8.2]

# 城市类型标签（根据柱状图数量推测）
city_types = ["一线城市", "新一线城市", "二线城市", "三线及以下城市"]
x = np.arange(len(city_types))  # x轴坐标

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制到店业务柱状图（黄色系列）
bar_width = 0.35
ax.bar(x - bar_width/2, store_service, width=bar_width, color=['gold', 'peru', 'coral', 'lightpink'], label='到店业务')
# 绘制到家业务柱状图（橙色系列）
ax.bar(x + bar_width/2, home_service, width=bar_width, color=['orange', 'darkorange', 'tomato', 'lightcoral'], label='到家业务')

ax.set_title('2023年中国各线城市网民对本地生活服务产品消费意愿调查', fontsize=14)
ax.set_ylabel('消费意愿占比（%）')
ax.set_xticks(x)
ax.set_xticklabels(city_types)
ax.legend()

# 添加到店业务数值标注
for i, val in enumerate(store_service):
    ax.text(x[i] - bar_width/2, val + 1, f'{val}%', ha='center', va='bottom', color='black')

# 添加到家业务数值标注
for i, val in enumerate(home_service):
    ax.text(x[i] + bar_width/2, val + 1, f'{val}%', ha='center', va='bottom', color='black')

plt.tight_layout()
plt.show()