import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 构建数据
data = {
    "category": ["性别（女）", "性别（男）", "19岁及以下", "20-29岁", "30-39岁", "40-49岁", "50岁及以上"],
    "percentage": [33, 67, 11, 26, 29, 23, 11]
}
df = pd.DataFrame(data)

# 分类数据为性别和年龄组
gender_data = df.iloc[:2]
age_data = df.iloc[2:]

# 创建一个包含两个子图的画布
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
fig.patch.set_facecolor('#f8f9fa')  # 设置画布背景色

# 美化柱状图 - 性别分布
sns.barplot(x="category", y="percentage", data=gender_data, palette=["#ff6b6b", "#48dbfb"], ax=ax1)
ax1.set_title("欧洲杯关注者性别分布", fontsize=15, pad=12)
ax1.set_xlabel("性别", fontsize=12)
ax1.set_ylabel("占比（%）", fontsize=12)
ax1.set_ylim(0, 100)  # 设置y轴范围
ax1.grid(axis='y', linestyle='--', alpha=0.7)  # 优化网格线

# 添加性别分布数值标签
for p in ax1.patches:
    height = p.get_height()
    ax1.text(p.get_x() + p.get_width() / 2., height + 1.5,
             f'{height:.1f}%', ha="center", fontsize=11)

# 美化饼图 - 年龄分布
wedges, texts, autotexts = ax2.pie(
    age_data["percentage"],
    labels=age_data["category"],
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("pastel"),
    wedgeprops={'edgecolor': 'w', 'linewidth': 1},
    textprops={'fontsize': 10}
)
ax2.set_title("欧洲杯关注者年龄分布", fontsize=15, pad=12)
ax2.axis('equal')  # 保证饼图是正圆形

# 调整布局
plt.tight_layout(pad=3)  # 增加子图间距
plt.suptitle("欧洲杯关注度基础数据统计", fontsize=18, y=1.02, fontweight='bold')

# 显示图表
plt.show()