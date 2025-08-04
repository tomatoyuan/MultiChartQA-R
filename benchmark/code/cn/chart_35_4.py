import matplotlib.pyplot as plt

# 数据准备
categories = [
    "易感疲惫", "体重问题", "皮肤问题", "肠胃/消化道",
    "焦虑/抑郁情绪", "三高问题", "呼吸道问题", "以上都没有"
]
percentages = [53, 50, 48, 47, 44, 29, 19, 10]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制横向条形图，添加渐变色
colors = plt.cm.viridis([i/len(categories) for i in range(len(categories))])
bars = ax.barh(categories, percentages, color=colors, edgecolor='gray', alpha=0.8)

# 添加标题和坐标轴标签
ax.set_title("近一年消费者的身体健康问题增多的具体方面", fontsize=16, pad=15)
ax.set_xlabel("比例（%）", fontsize=14, labelpad=10)
ax.set_ylabel("健康问题类型", fontsize=14, labelpad=10)

# 设置x轴范围和刻度
ax.set_xlim(0, max(percentages) * 1.1)  # 稍微扩展x轴范围
ax.set_xticks(range(0, 60, 10))

# 添加网格线
ax.grid(axis='x', linestyle='--', alpha=0.6)

# 添加数据标签
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', fontsize=12)

# 美化图表
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', which='major', labelsize=12)

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()