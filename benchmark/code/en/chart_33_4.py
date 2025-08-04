import matplotlib.pyplot as plt
import numpy as np

# E-commerce platform names
platforms = ['Tmall', 'Douyin', 'JD.com']
# Market share data (approximate values are okay)
market_share = [30, 25, 15]

x = np.arange(len(platforms))  # x-axis coordinates
width = 0.5  # Bar width

fig, ax = plt.subplots()
# Draw a bar chart with a similar blue color and black edges
rects = ax.bar(x, market_share, width, color='#4CAF50', edgecolor='black')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(platforms)
# Set y-axis label
ax.set_ylabel('Market Share')
# Set the chart title
ax.set_title('Market Share of E-commerce Platforms in MAT25')

# Add data labels
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects)

plt.show()