import matplotlib.pyplot as plt
import numpy as np

# 数据
age_groups = ["<19岁", "19-24岁", "25-34岁", "35-49岁", ">=50岁"]
male_percents = [13, 37, 41, 8, 1]
female_percents = [20, 47, 27, 5, 1]

x = np.arange(len(age_groups))  # x 轴位置
width = 0.35  # 条形宽度

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制男性、女性分组条形
rects_male = ax.bar(x - width/2, male_percents, width, label="男性群体", color="#4CAF50")
rects_female = ax.bar(x + width/2, female_percents, width, label="女性群体", color="#F44336")

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(age_groups)
# 设置 y 轴标签
ax.set_ylabel("关注占比（%）")
# 设置标题
ax.set_title('关注“情人节礼物”的性别 - 年龄分布')
# 添加图例
ax.legend()

# 在条形上标注数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 数值标签距离条形的垂直距离
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects_male)
autolabel(rects_female)

# 调整布局，显示图表
plt.tight_layout()
plt.show()