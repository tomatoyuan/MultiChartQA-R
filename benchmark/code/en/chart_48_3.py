import matplotlib.pyplot as plt
import numpy as np

# Categories
categories = ['Very well - off', 'Relatively well - off', 'Barely enough', 'Relatively difficult', 'Very difficult']
# Rural data
rural = [2.3, 14.9, 61.3, 17.9, 3.6]
# Urban data
urban = [4.5, 22.0, 61.2, 10.5, 1.8]
# Total data
total = [3.5, 18.7, 61.2, 13.9, 2.7]

x = np.arange(len(categories))  # x-axis position
width = 0.25  # Width of each bar

fig, ax = plt.subplots()
# Draw bars for rural, urban, and total
rects1 = ax.barh(x - width, rural, width, label='Rural', color='green')
rects2 = ax.barh(x, urban, width, label='Urban', color='darkgreen')
rects3 = ax.barh(x + width, total, width, label='Total', color='gray')

# Add labels, title, etc.
ax.set_yticks(x)
ax.set_yticklabels(categories)
ax.set_xlabel('Percentage%')
ax.set_title('Self - rated economic status of elderly people in urban and rural areas in China in 2021')
ax.legend()

# Display values on the bars
def label_bars(rects):
    for rect in rects:
        length = rect.get_width()
        ax.text(length + 0.5, rect.get_y() + rect.get_height() / 2, f'{length}%', va='center')

label_bars(rects1)
label_bars(rects2)
label_bars(rects3)

plt.show()