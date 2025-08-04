import matplotlib.pyplot as plt
import numpy as np

# 数据
groups = ['Total人群', '男', '女', '18-34岁', '35-64岁', '高线城市', '低线城市']
values = [31.4, 29.8, 33.2, 26.7, 32.6, 28.6, 33.0]
colors = ['#bbbbbb'] + ['#ff2d55'] * 6  # 第一项灰色，其余红色

y = np.arange(len(groups))

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))

# 横向条形图
bars = ax.barh(y, values, color=colors, height=0.6)

# 添加数值标签在右侧
for i, (bar, val) in enumerate(zip(bars, values)):
    ax.text(val + 0.5, bar.get_y() + bar.get_height() / 2, f'{val:.1f}%', va='center', fontsize=10)

# 虚线参考线（最高值对齐）
ax.axvline(x=31.4, linestyle='--', color='gray', linewidth=2)

# 设置标签与标题
ax.set_yticks(y)
ax.set_yticklabels(groups, fontsize=11)
ax.set_xlim(0, 40)
ax.invert_yaxis()  # 让“Total人群”在最上方
ax.set_xlabel('周渗透率（%）', fontsize=12)
ax.set_title('各细分人群中，\n微短剧的周渗透率', fontsize=14, fontweight='bold', pad=20)

# 去除边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# 网格线
ax.xaxis.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()