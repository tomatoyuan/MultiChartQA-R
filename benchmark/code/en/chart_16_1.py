import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2011, 2012, 2013, 2014, 2015]
# Number of provincial top - scorers admitted by Tsinghua University
qinghua = [35, 43, 50, 42, 43]
# Number of provincial top - scorers admitted by Peking University
beida = [23, 27, 24, 48, 38]

# Set the bar width
bar_width = 0.35
# Generate x - axis positions for the two groups of bars
x = np.arange(len(years))

# Create a figure and axes
fig, ax = plt.subplots()

# Draw the bars for Tsinghua University
rects1 = ax.bar(x - bar_width/2, qinghua, bar_width, label='Tsinghua', color='#6699CC')
# Draw the bars for Peking University
rects2 = ax.bar(x + bar_width/2, beida, bar_width, label='Peking', color='#CC6666')

# Set the x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set the y - axis label
ax.set_ylabel('Number of provincial top - scorers admitted')
# Set the title
ax.set_title('Comparison of the number of provincial top - scorers admitted by Tsinghua and Peking Universities from 2011 to 2015')
# Add a legend
ax.legend()

# Label the values on the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 - point vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Adjust the layout to avoid label overlap
fig.tight_layout()
# Display the chart
plt.show()