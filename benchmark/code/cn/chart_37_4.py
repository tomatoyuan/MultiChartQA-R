import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------- 性别占比饼图数据 --------------------
gender_data = {
    "性别": ["女性", "男性"],
    "占比": [61, 39]
}
gender_df = pd.DataFrame(gender_data)

# -------------------- 年龄分布柱状图数据 --------------------
age_data = {
    "年龄段": ["16-23岁", "24-30岁", "31-35岁", "36-40岁", "41-45岁", "46-50岁", "50岁以上"],
    "占比": [15, 22, 21, 14, 9, 8, 9]
}
age_df = pd.DataFrame(age_data)

# 创建画布，包含 2 个子图（1 行 2 列）
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# -------------------- 绘制性别占比饼图 --------------------
axes[0].pie(
    gender_df["占比"],
    labels=gender_df["性别"],
    autopct="%1.1f%%",  # 显示百分比，保留 1 位小数
    colors=["#ff99cc", "#66b3ff"],  # 自定义颜色
    startangle=90  # 饼图起始角度
)
axes[0].set_title("抖音电商秋冬服饰人群性别占比")

# -------------------- 绘制年龄分布柱状图 --------------------
bar_plot = sns.barplot(
    data=age_df,
    x="年龄段",
    y="占比",
    color="#c9b69f",  # 自定义柱状图颜色
    ax=axes[1]
)
axes[1].set_title("抖音电商秋冬服饰人群年龄分布")
axes[1].set_xlabel("年龄段")
axes[1].set_ylabel("占比")

# 在柱状图上添加数值标签
for p in bar_plot.patches:
    bar_plot.annotate(
        f'{p.get_height()}%',
        (p.get_x() + p.get_width() / 2., p.get_height()),
        ha='center',
        va='center',
        fontsize=10,
        color='black',
        xytext=(0, 5),
        textcoords='offset points'
    )

# 让布局更紧凑（避免标签重叠等问题）
plt.tight_layout()
# 显示图表
plt.show()