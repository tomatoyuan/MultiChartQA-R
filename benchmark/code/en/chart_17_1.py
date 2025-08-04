import matplotlib.pyplot as plt
import numpy as np

# Date data
dates = ['8-21', '8-23', '8-25', '8-27', '8-29', '8-31', '9-02', '9-04', '9-06']
# Search heat data. You can adjust it according to the actual values in the chart. Here it is for demonstration.
search_heat = [32000, 26000, 19000, 14000, 17500, 31000, 11500, 9000, 19500]

x = np.arange(len(dates))  # x-axis coordinates

fig, ax = plt.subplots()
# Draw a bar chart
rects = ax.bar(x, search_heat, color=['r', 'r', 'gold', 'b', 'orange', 'r', 'lightgreen', 'b', 'r'])

# Set x-axis tick labels
ax.set_xticks(x)
ax.set_xticklabels(dates)
# Set the y-axis range
ax.set_ylim(0, 35000)
# Set the title and axis labels
ax.set_title('Search Heat of Telecom Fraud')
ax.set_ylabel('Search Heat')

# Annotate the values on the bars (Optional. You can omit this if you want it to be closer to the original chart)
for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

plt.show()