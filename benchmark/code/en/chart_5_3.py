import matplotlib.pyplot as plt
import numpy as np

# City levels
cities = ['First-tier cities', 'Second-tier cities', 'Third-tier cities', 'Fourth-tier cities']
x = np.arange(len(cities))

# Left Y-axis: Bar chart data (Attention proportion)
bar_values = [33, 17, 22, 15]  # Corresponding to the left axis (0% - 40%)

# Right Y-axis: Line chart data (Attention proportion of another dimension)
line_values = [33, 17, 22, 15]  # Corresponding to the right axis (0% - 40%)

fig, ax1 = plt.subplots(figsize=(10, 6))

# Draw the bar chart, left axis
bars = ax1.bar(x, bar_values, color='#1f77ff', width=0.5)
ax1.set_ylabel('Attention proportion', fontsize=12)
ax1.set_ylim(0, 40)
ax1.set_yticks(np.arange(0, 41, 5))
ax1.set_xticks(x)
ax1.set_xticklabels(cities, fontsize=12)
ax1.set_title('Attention proportion of the milk powder industry by city level in February', fontsize=15)

# Create the right axis to draw the line chart
ax2 = ax1.twinx()
line, = ax2.plot(x, line_values, color='orange', linewidth=3, marker='o', markersize=8)
ax2.set_ylabel('Attention proportion of another dimension', fontsize=12)
ax2.set_ylim(0, 40)
ax2.set_yticks(np.arange(0, 41, 5))

# Add data labels to the line chart
for i, (x_val, y_val) in enumerate(zip(x, line_values)):
    # Adjust the label position according to the value size to avoid overlap
    if i in [0, 2]:  # To avoid overlapping with the bar chart, adjust the position of some labels
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(10, 5),  # Offset to the upper right
                    textcoords="offset points",
                    ha='left', va='bottom',
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))
    else:
        ax2.annotate(f'{y_val}%',
                    xy=(x_val, y_val),
                    xytext=(0, 10),  # Offset upward
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="orange", alpha=0.7))

# Beautify the graph border
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

# Add a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, ['Attention proportion', 'Attention proportion of another dimension'], loc='upper right')

plt.tight_layout()
plt.show()