import matplotlib.pyplot as plt
import numpy as np

# 年龄段
age_groups = ['≤18岁', '19-24岁', '25-34岁', '35-49岁', '50岁']
# 女性占比数据（模拟，根据图表趋势及已知数据合理补充）
female_percents = [60, 71, 57, 55, 52]  
# 男性占比数据（模拟，根据图表趋势及已知数据合理补充）
male_percents = [40, 29, 43, 45, 48]  

x = np.arange(len(age_groups))  # x 轴位置
width = 0.35  # 柱子宽度

fig, ax = plt.subplots()
# 绘制女性柱子
rects1 = ax.bar(x - width/2, female_percents, width, label='女', color='pink')
# 绘制男性柱子
rects2 = ax.bar(x + width/2, male_percents, width, label='男', color='blue')

# 添加标题和标签
ax.set_ylabel('占比 (%)')
ax.set_title('不同年龄段搜索“教师资格证”男女占比')
ax.set_xticks(x)
ax.set_xticklabels(age_groups)
ax.legend()

# 在柱子上标注数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 数值标签距离柱子的垂直距离
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()