import matplotlib.pyplot as plt
import numpy as np

# Years
years = [2022, 2023, 2024]
# Online channel shares
online_shares = [41, 41, 43]
# Offline channel shares (calculated by 100 - online channel shares, as the total is 100%)
offline_shares = [100 - x for x in online_shares]

x = np.arange(len(years))  # Bar chart x-axis positions
width = 0.35  # Width of each bar

fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size for better layout
# Draw offline channel bars
rects_offline = ax.bar(x - width/2, offline_shares, width, label='Offline Channel', color='#D9C8B1')
# Draw online channel bars
rects_online = ax.bar(x + width/2, online_shares, width, label='Online Channel', color='#F7C8AA')

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set y-axis label
ax.set_ylabel('Share (%)')
# Set the title
ax.set_title('Comparison of Online and Offline Channel Shares of Skincare Products from 2022 - 2024')

# Adjust y-axis limit to create space for legend
ax.set_ylim(0, 110)  # Increase upper limit to 110%

# Label the values on the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}%'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # Offset of the value label position
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects_offline)
autolabel(rects_online)

# Place legend outside the plot to avoid overlapping
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),  # Position legend below the chart
          fancybox=True, shadow=True, ncol=2)  # Use 2 columns for better appearance

plt.tight_layout()  # Adjust layout to ensure everything fits
plt.show()