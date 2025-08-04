import matplotlib.pyplot as plt
import numpy as np

labels_cost = ['建站成本', '产品开发', '流量成本', '仓储物流', '人力成本', '其它成本']
values_cost = [6.1, 25.5, 32.6, 13.0, 18.5, 4.3]
values_cost += values_cost[:1]
angles = np.linspace(0, 2 * np.pi, len(labels_cost), endpoint=False).tolist()
angles += angles[:1]

fig1, ax1 = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})
ax1.plot(angles, values_cost, color='darkorange', linewidth=2)
ax1.fill(angles, values_cost, color='darkorange', alpha=0.6)
ax1.set_thetagrids(np.degrees(angles[:-1]), labels_cost, fontsize=10)
ax1.set_title("独立站主要成本支出", fontsize=14, fontweight='bold', pad=20)

for angle, value in zip(angles, values_cost):
    ax1.text(angle, value + 2, f'{value:.1f}%', color='darkorange',ha='center', va='center', fontsize=10)

plt.figtext(0.5, 0.02, "来源：GoodsFox调研数据，统计时间2023年1月-12月", ha='center', fontsize=10)
plt.tight_layout()
plt.show()