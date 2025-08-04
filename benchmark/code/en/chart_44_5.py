import matplotlib.pyplot as plt
import numpy as np

# Chart data
status = ["Sedentary, sitting almost all day with little movement", 
          "Get up and walk around only when feeling uncomfortable from sitting too long", 
          "Set up a computer stand at the workstation and often work standing", 
          "Regularly require oneself to get up and move at intervals, such as every hour", 
          "Frequently move around due to work requirements and don't have the problem of sitting for long periods"]
percentage = [34, 44, 8, 13, 2]
tgi = [138, 108, 73, 59, 65]

# Create a canvas and dual Y - axes
fig, ax1 = plt.subplots(figsize=(14, 8))
ax2 = ax1.twinx()

# Set the positions of the bar charts
x = np.arange(len(status))
width = 0.35

# Draw the bar charts
bars1 = ax1.bar(x - width/2, percentage, width, label='Percentage', color='#5DA5DA')
bars2 = ax2.bar(x + width/2, tgi, width, label='TGI', color='#FAA43A')

# Set the axis labels and title
ax1.set_xlabel('Daily office status', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12, color='#5DA5DA')
ax2.set_ylabel('TGI', fontsize=12, color='#FAA43A')
plt.title('Distribution of daily office status and TGI among punk overtime workers', fontsize=16, pad=10)

# Set the x - axis ticks and labels
ax1.set_xticks(x)
ax1.set_xticklabels(status, rotation=45, ha='right', fontsize=10)

# Add a legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

# Add data labels
def add_labels(bars, ax, is_percentage=True):
    for bar in bars:
        height = bar.get_height()
        if is_percentage:
            ax.annotate(f'{height}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')
        else:
            ax.annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

add_labels(bars1, ax1)
add_labels(bars2, ax2, False)

# Set the grid lines
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust the layout
plt.tight_layout()

# Display the chart
plt.show()