import matplotlib.pyplot as plt
import numpy as np

# 标签和数据
labels = ['刚需', '愉悦自己', '彰显品味/个性', '焕新', '种草/他人推荐', '猎奇尝鲜', '礼赠亲友', '冲动购买']
values = [55, 42, 36, 36, 30, 21, 15, 11]

# 处理雷达图的角度
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

# 设置画布
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# 绘图
ax.plot(angles, values, color='blue', linewidth=2)
ax.fill(angles, values, color='blue', alpha=0.25)

# 设置标签
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# 添加数值标签
for angle, value in zip(angles, values):
    ax.text(angle, value + 3, f"{value}%", ha='center', va='center', fontsize=10)

# 添加标题和来源
fig.text(0.5, 1.05, '电器行业消费者需求', ha='center', fontsize=16, fontweight='bold')
plt.subplots_adjust(top=1)  # 增加顶部空间
plt.figtext(0.1, 0.01, "数据来源：魔镜洞察", ha="left", fontsize=10)

plt.tight_layout()
plt.show()