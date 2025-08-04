import matplotlib.pyplot as plt

# 饼图数据
labels = ['18-24', '25-29', '30-34', '35-39', '40+']
sizes_uv = [25, 25, 15, 20, 15]  # 年龄占比
sizes_growth = [30, 15, 45, 60, 50]  # 同比增速（%）

# 创建图形和子图
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# 左侧饼图：年龄占比
wedges, texts, autotexts = axs[0].pie(
    sizes_uv,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)
axs[0].axis('equal')
axs[0].set_title('送朋友用户 年龄占比')

# 设置饼图内文本样式
for text in autotexts:
    text.set_fontsize(10)

# 右侧柱状图：同比增速
bars = axs[1].bar(labels, sizes_growth, color='lightcoral')
axs[1].set_title('送朋友用户 同比增速')
axs[1].set_ylabel('同比增长率 (%)')

# 添加数值标签在柱子上方
for bar, growth in zip(bars, sizes_growth):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height + 2,
        f"{growth}%",
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.tight_layout()
plt.show()