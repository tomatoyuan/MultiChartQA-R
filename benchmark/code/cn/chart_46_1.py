import matplotlib.pyplot as plt
import numpy as np

# 类别
categories = ["人体工学椅", "电动升降桌", "护眼灯"]
# 2023 年数据（十亿元）
values_2023 = [3, 2, 9]  
# 2024 年数据（十亿元）
values_2024 = [4.5, 3.5, 12]  
# 同比增速
growth_rates = ["+43%", "+33%", "+26%"]  

x = np.arange(len(categories))  # x 轴位置
width = 0.35  # 柱状图宽度

fig, ax = plt.subplots()
# 绘制 2023 年柱状图
rects2023 = ax.bar(x - width/2, values_2023, width, label='2023', color='lightblue')  
# 绘制 2024 年柱状图
rects2024 = ax.bar(x + width/2, values_2024, width, label='2024', color='steelblue')  

# 添加数值标注函数
def add_labels(rects, values):
    for rect, value in zip(rects, values):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height + 0.2,
                f'{value}', ha='center', va='bottom')

# 为两个年份的柱状图添加数值标注
add_labels(rects2023, values_2023)
add_labels(rects2024, values_2024)

# 添加同比增速文本
for i in range(len(categories)):
    if growth_rates[i].startswith('+'):
        arrow_color = 'red' if growth_rates[i] == '+43%' else 'black'
        ax.text(x[i] + width/2 + 0.1, values_2024[i] - 1, growth_rates[i], 
                color=arrow_color, fontweight='bold')
    else:
        ax.text(x[i] + width/2, values_2024[i] + 0.2, growth_rates[i], ha='center')

# 设置 x 轴刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(categories)
# 设置 y 轴范围，留出标注空间
ax.set_ylim([0, 15])  
# 添加 y 轴刻度
ax.set_yticks(np.arange(0, 16, 5))  
# 添加图例
ax.legend()

# 设置图表标题
ax.set_title('2023年-2024年书房“三大件”线上市场规模（十亿元）及同比增速')
plt.tight_layout()  # 确保布局合理
plt.show()