import matplotlib.pyplot as plt
import numpy as np

# Disposable types
categories = ['Daily Disposable', 'Monthly Disposable', 'Bi - weekly Disposable', 'Quarterly Disposable', 'Semi - annual Disposable', 'Annual Disposable']
# Proportion of transparent contact lenses (simulated data, generally close to the example ratio)
transparent = [25, 20, 15, 10, 5, 2]
# Proportion of colored contact lenses (simulated data, the sum is approximately the corresponding ratio in the example, such as the sum of daily disposables is approximately 41%)
colorful = [16, 19, 12, 10, 10, 2]

x = np.arange(len(categories))  # x-axis positions
width = 0.35  # Width of each bar in the group

fig, ax = plt.subplots()
# Draw bars for transparent contact lenses
rects1 = ax.bar(x - width/2, transparent, width, label='Transparent Contact Lenses', color='#5799C6')
# Draw bars for colored contact lenses
rects2 = ax.bar(x + width/2, colorful, width, label='Colored Contact Lenses', color='#F28A2B')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=30, ha='right')
# Set y-axis label
ax.set_ylabel('Proportion (%)')
# Set the title
ax.set_title('Consumers alternately choose daily and monthly disposable contact lenses in daily use\nDisposable types mainly used in the past year')
ax.legend()

# Annotate the values above each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Vertical offset of the numerical annotation relative to the bar
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.tight_layout()
plt.show()