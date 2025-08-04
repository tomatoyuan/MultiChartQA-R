import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ["Ergonomic chairs", "Electric standing desks", "Eye - care lamps"]
# Data in 2023 (billions of yuan)
values_2023 = [3, 2, 9]
# Data in 2024 (billions of yuan)
values_2024 = [4.5, 3.5, 12]
# Year - on - year growth rates
growth_rates = ["+43%", "+33%", "+26%"]

x = np.arange(len(categories))  # x-axis positions
width = 0.35  # Bar width

fig, ax = plt.subplots()
# Draw the bar chart for 2023
rects2023 = ax.bar(x - width/2, values_2023, width, label='2023', color='lightblue')
# Draw the bar chart for 2024
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

# Add year - on - year growth rate text
for i in range(len(categories)):
    if growth_rates[i].startswith('+'):
        arrow_color = 'red' if growth_rates[i] == '+43%' else 'black'
        ax.text(x[i] + width/2 + 0.1, values_2024[i] - 1, growth_rates[i], 
                color=arrow_color, fontweight='bold')
    else:
        ax.text(x[i] + width/2, values_2024[i] + 0.2, growth_rates[i], ha='center')

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Set y - axis range
ax.set_ylim([0, 15])
# Add y - axis ticks
ax.set_yticks(np.arange(0, 16, 5))
# Add legend
ax.legend()

# Set chart title
ax.set_title('Online market scale (billions of yuan) and year - on - year growth rate of the "Big Three" in the study from 2023 to 2024')
plt.tight_layout()  # 确保布局合理
plt.show()