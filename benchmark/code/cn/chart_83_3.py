import matplotlib.pyplot as plt

# -------------------- 数据定义 --------------------
labels = ['1-50万元（台）', '50-99万元（台）', '100万元及以上（台）']
sizes = [95, 3, 2]  # 占比
absolute_values = [950, 30, 20]  # 假设真实数量（可选）

# 新配色（增强可读性与美感）
colors = ['#ff6f91', '#845ec2', '#88ccf1']

# -------------------- 创建画布 --------------------
fig, ax = plt.subplots(figsize=(7, 6))

# -------------------- 绘制环形图（饼图 + 中心空洞） --------------------
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(width=0.6, edgecolor='white')  # 环形 + 白色边界
)

# -------------------- 调整文字样式 --------------------
for i, autotext in enumerate(autotexts):
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

# -------------------- 添加中心注释 --------------------
total = sum(absolute_values)
ax.text(
    0, 0,
    f"总计\n{total} 台",
    ha='center', va='center',
    fontsize=12,
    fontweight='bold',
    color="#424242"
)

# -------------------- 添加标题 --------------------
ax.set_title(
    "2020年中国康复医院万元以上设备台数分布（环形图）",
    fontsize=14,
    fontweight='bold',
    pad=20
)

# -------------------- 布局优化与展示 --------------------
plt.tight_layout()
plt.show()