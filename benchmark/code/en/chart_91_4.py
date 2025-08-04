import matplotlib.pyplot as plt
import numpy as np

# Purchase frequency categories
categories = ["Within half a year", "Half a year to one year", "One year to two years", "Over two years"]
# Corresponding proportion data (simulated, can be adjusted according to actual situation)
percentages = [24.4, 49.7, 23.6, 3.3]
# Total proportion (Within half a year + Half a year to one year)
total_percent = sum(percentages[:2])

# Create a canvas and sub - plot
fig, ax = plt.subplots(figsize=(7, 5))

# Draw a bar chart
x = np.arange(len(categories))
bar_width = 0.6
bars = ax.bar(x, percentages, width=bar_width, color="#A4C639")

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Add the total proportion label (simulate a blue dashed box and text)
ax.text(1, total_percent + 3, f'Total {total_percent}%',
        ha='center', va='bottom', color='lightblue', fontweight='bold')
# Draw a blue dashed box (simulate the range)
x_min = x[0] - bar_width/2
x_max = x[1] + bar_width/2
y_min = 0
y_max = total_percent + 5
ax.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min],
        linestyle='--', color='lightblue', linewidth=1)

# Set x - axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(categories)
# Hide y - axis ticks
ax.set_yticks([])
# Set the title
ax.set_title("Average frequency of consumers purchasing high - end cup and kettle products in the past 3 years", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()