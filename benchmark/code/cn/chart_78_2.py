import matplotlib.pyplot as plt
import numpy as np

# 地区名称
regions = ["大洋洲", "欧洲", "亚洲东部", "拉丁美洲及加勒比", "非洲撒哈拉以南"]
# 高中入学率（%），数据大体一致即可
high_school_enrollment = [95.0, 93.6, 86.4, 78.7, 41.9]
# 职业教育参与率（%），数据大体一致即可
vocational_education = [17.5, 18.1, 7.2, 6.9, 1.3]
# 人均 GDP（美金），数据大体一致即可
gdp_per_capita = [49999.0, 34148.9, 13463.6, 7244.7, 1501.2]

# 创建画布和子图
fig, ax = plt.subplots(figsize=(10, 6))

ax.set_ylim(0, 120)

# 绘制分组柱状图
x = np.arange(len(regions))
bar_width = 0.35
# 高中入学率（绿色）
high_school_bars = ax.bar(x - bar_width/2, high_school_enrollment, width=bar_width, color="#A4C639", label="各地区高中入学率（%）")
# 职业教育参与率（蓝色）
vocational_bars = ax.bar(x + bar_width/2, vocational_education, width=bar_width, color="#64B5F6", label="各地区15-24岁职业教育参与率（%）")

# 添加高中入学率数据标注
for bar in high_school_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 添加职业教育参与率数据标注
for bar in vocational_bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 标注位置调整
                textcoords="offset points",
                ha='center', va='bottom')

# 设置x轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(regions)
# 设置y轴标签
ax.set_ylabel("比例（%）")
# 设置标题
ax.set_title("2020年各地区职业教育参与率与高中入学率", fontsize=14, fontweight="bold")

# 添加图例
ax.legend()

# 美化图表，隐藏顶部和右侧边框
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # 自动调整布局
plt.show()