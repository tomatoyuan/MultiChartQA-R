import matplotlib.pyplot as plt

# 数据
categories = ["生活记录", "颜值", "美食", "幽默搞笑", "游戏", "音乐", "影视", "美妆", "时尚", "情感"]
values = [100, 90, 70, 80, 80, 70, 65, 60, 60, 50]  # 示例值

highlight_indices = [0, 7, 8]  # 高亮显示“生活记录”、“美妆”、“时尚”

# 绘图
fig, ax = plt.subplots(figsize=(10, 4))
bars = ax.bar(categories, values, color="#4da6ff")

# 用虚线框标出重点类目
for idx in highlight_indices:
    bar = bars[idx]
    height = bar.get_height()
    ax.add_patch(plt.Rectangle(
        (bar.get_x() - 0.1, 0), bar.get_width() + 0.2, height + 5,
        fill=False, edgecolor="#b084e9", linewidth=2, linestyle='--'
    ))

# 添加数值标注
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f"{height}",
            ha='center', va='bottom', fontsize=10)

# 图形美化
ax.set_title("抖音腰部达人所属内容类目数量TOP10占比分布", fontsize=12)
ax.set_ylabel("数量（示意）")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()