import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2023", "2024", "2025e", "2026e", "2027e", "2028e"]
# Global shipments (in ten thousand units)
global_shipments = [34, 234, 585, 1070, 1730, 2600]
# China shipments (in ten thousand units)
china_shipments = [10, 36, 108, 324, 648, 972]

x = np.arange(len(years))  # X-axis tick positions
width = 0.35  # Width of each bar in the group

fig, ax = plt.subplots()

# Draw the global shipments bar chart
rects1 = ax.bar(x - width/2, global_shipments, width, label='Global Shipments (in ten thousand units)', color='greenyellow')
# Draw the China shipments bar chart
rects2 = ax.bar(x + width/2, china_shipments, width, label='China Shipments (in ten thousand units)', color='dodgerblue')

# Add title and axis labels
ax.set_title('AI Glasses Shipment Scale and Forecast from 2023 to 2028')
ax.set_xticks(x)
ax.set_xticklabels(years)

# Add numerical labels to each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3-point vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

# Add legend
ax.legend()

plt.show()