import matplotlib.pyplot as plt
import numpy as np

# Date data
dates = ["14th", "15th", "16th", "17th", "18th", "19th"]
# Heat data (unit: ten thousand)
heat_values = [4698, 3708, 3131, 2204, 2325, 2892]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6), facecolor='#f8f9fa')

# Set the grid style
ax.grid(True, linestyle='--', alpha=0.7, color='#dddddd')

# Draw a line chart with a gradient color
x = np.arange(len(dates))
line, = ax.plot(x, heat_values, marker='o', markersize=8, 
                color='#1e88e5', linewidth=3, alpha=0.8)

# Add data labels
for i, (date, value) in enumerate(zip(dates, heat_values)):
    ax.annotate(f'{value}',
                xy=(i, value),
                xytext=(0, 10),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#1e88e5", alpha=0.8))

# Set the x - axis labels
ax.set_xticks(x)
ax.set_xticklabels(dates, fontsize=11)

# Set the y - axis range and label
ax.set_ylim(0, max(heat_values) * 1.1)
ax.set_ylabel('Heat (ten thousand)', fontsize=12, labelpad=10)

# Add a title
ax.set_title('World Cup Heat Trend in the First Round of the Group Stage', fontsize=16, pad=15, fontweight='bold')

# Add a background color
ax.set_facecolor('#f8f9fa')

# Add trend arrows
for i in range(len(x)-1):
    ax.annotate('',
                xy=(x[i+1], heat_values[i+1]),
                xytext=(x[i], heat_values[i]),
                arrowprops=dict(arrowstyle='->', color='#1e88e5', lw=1.5, alpha=0.6))

# Add a legend
ax.legend(['Heat Trend'], loc='upper right', frameon=True, framealpha=0.9)

# Add a bottom note
plt.figtext(0.5, 0.01, 'Data Source: Fictitious Example', ha='center', fontsize=9, color='#666666')

# Optimize the layout
plt.tight_layout(pad=2)

# Save the chart (optional)
# plt.savefig('worldcup_heat_trend.png', dpi=300, bbox_inches='tight')

# Display the chart
plt.show()