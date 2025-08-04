import matplotlib.pyplot as plt
import numpy as np

# Data preparation
provinces = ["Hubei", "Zhejiang"]
# Each Olympic Games (Note: The 24th Games appears twice in the original data. Here, we process it according to the column title order.)
games = ["23rd", "24th", "24th", "26th", "27th", "28th", "29th", "30th"]
# Gold medals of Hubei
hubei_golds = [1, 1, 3, 4, 6, 4, 5, 2]
# Gold medals of Zhejiang
zhejiang_golds = [2, 1, 1, 1, 1, 4, 2, 4]

x = np.arange(len(games))  # x-axis tick positions
width = 0.35  # Bar width

fig, ax = plt.subplots()
# Plot Hubei data
rects1 = ax.bar(x - width/2, hubei_golds, width, label='Hubei')
# Plot Zhejiang data
rects2 = ax.bar(x + width/2, zhejiang_golds, width, label='Zhejiang')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(games)
# y-axis title
ax.set_ylabel('Number of Gold Medals')
# Chart title
ax.set_title('Comparison of Gold Medals in Each Olympic Games between Hubei and Zhejiang')
ax.legend()  # Show legend

# Add numerical labels to each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Vertical distance of the label from the bar
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()  # Optimize layout
plt.show()  # Show the chart