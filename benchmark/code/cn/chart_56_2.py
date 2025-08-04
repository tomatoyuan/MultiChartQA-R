import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal')
ax.axis('off')

# ✅ 缩小主圈尺寸
center_circle = plt.Circle((0, 0), 0.6, color='white', ec='black', lw=2.5, zorder=3)
center_circle_inner = plt.Circle((0, 0), 0.45, color='white', ec='black', lw=2.5, zorder=4)
ax.add_artist(center_circle)
ax.add_artist(center_circle_inner)
ax.text(0, 0.06, '11.1 亿人', ha='center', va='center', fontsize=17, fontweight='bold')
ax.text(0, -0.22, '全国网民规模（2024）', ha='center', fontsize=12)

# 子圈参数（已精调）
positions = [(-1.4, 1.0), (1.4, -1.0), (-1.4, -1.0)]
colors = ['#76C7C0', '#58A4B0', '#4C8C9D']
labels = ['短视频用户', '网络直播用户', '网络购物用户']
users = ['10.4 亿人', '8.3 亿人', '9.7 亿人']
rates = ['CAGR¹=4.5%', 'CAGR¹=7.8%', 'CAGR¹=5.6%']
percents = ['× 93.8%', '× 75.2%', '× 87.9%']

r_outer = 0.22
r_inner = 0.18

for i in range(3):
    x, y = positions[i]
    color = colors[i]

    # 子圈绘制
    outer = plt.Circle((x, y), r_outer, color='white', ec=color, lw=2.5, zorder=3)
    inner = plt.Circle((x, y), r_inner, color='white', ec=color, lw=2.5, zorder=4)
    ax.add_artist(outer)
    ax.add_artist(inner)

    # 连接线 + 比例
    ax.plot([0, x], [0, y], color='gray', lw=1, zorder=1)
    ax.text(x * 0.5, y * 0.5, percents[i], ha='center', va='center', fontsize=12, color=color)

    # 子圈说明
    ax.text(x, y - 0.28, users[i], ha='center', va='top', fontsize=12, fontweight='bold')
    ax.text(x, y - 0.42, labels[i], ha='center', va='top', fontsize=12, color=color)
    ax.text(x, y - 0.56, rates[i], ha='center', va='top', fontsize=10)

# ✅ 标题下移，贴近图心
ax.text(0, 1.6, '直播电商行业用户增长空间探析', ha='center', fontsize=18, fontweight='bold')
ax.text(0, -2.2, '¹ CAGR: 复合年增长率', ha='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()