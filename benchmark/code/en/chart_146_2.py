import matplotlib.pyplot as plt
import numpy as np

# --------------------- Left Pie Chart Data ---------------------
pie_labels = ["Dine-in at the restaurant", "Online food delivery", "Buy offline and take home", "Similar proportion of online and offline"]
pie_sizes = [32.5, 23.3, 23.5, 20.7]
pie_colors = ["#FFD700", "#FF7F50", "#32CD32", "#8B4513"]

# --------------------- Right Grouped Bar Chart Data ---------------------
bar_categories = ["Less than 30% (excluding 30%)", "30 - 40% (excluding 40%)", "40 - 50% (excluding 50%)", "50 - 80% (excluding 80%)", "80 - 100%"]
bar_values = [
    [32.2, 67.8],  # First group: Orange part, Light - colored part
    [43.8, 56.2],
    [19.3, 80.7],
    [3.4, 96.6],
    [1.3, 98.7]
]
bar_colors = ["#FF7F50", "#FAF0E6"]  # Orange, Light beige

# Create a canvas with a 1 - row, 2 - column layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Draw the left pie chart ---------------------
wedges, texts, autotexts = ax1.pie(pie_sizes, colors=pie_colors, autopct='%1.1f%%', startangle=90)
ax1.set_title('Distribution of Types of Night - time Catering Consumption Proportion among Chinese Residents in 2023')
# Adjust the legend
ax1.legend(wedges, pie_labels, title="Consumption Type", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the right grouped bar chart ---------------------
x = np.arange(len(bar_categories))
bottom = np.zeros(len(bar_categories))
for i in range(2):
    ax2.bar(x, [val[i] for val in bar_values], bottom=bottom, color=bar_colors[i], label=pie_labels[i] if i == 0 else '')
    bottom += [val[i] for val in bar_values]

ax2.set_title('Distribution of Night - time Catering Consumption Proportion of the Whole Day among Chinese Residents in 2023')
ax2.set_ylabel('Proportion (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(bar_categories, rotation=45, ha='right')
ax2.legend(title="Consumption Type", loc="upper left")

# Add numerical annotations to the grouped bar chart
for i, (val1, val2) in enumerate(bar_values):
    ax2.text(i, val1 / 2, f'{val1}%', ha='center', va='center', color='white')
    ax2.text(i, val1 + val2 / 2, f'{val2}%', ha='center', va='center', color='black')

# Simulate yellow dashed boxes (first two groups)
ax2.plot([x[0] - 0.3, x[0] + 0.3, x[0] + 0.3, x[0] - 0.3, x[0] - 0.3],
         [0, 0, 100, 100, 0],
         linestyle='--', color='gold', linewidth=2)
ax2.plot([x[1] - 0.3, x[1] + 0.3, x[1] + 0.3, x[1] - 0.3, x[1] - 0.3],
         [0, 0, 100, 100, 0],
         linestyle='--', color='gold', linewidth=2)

plt.suptitle('Proportion of Night - time Catering Consumption to the Whole - day Catering Consumption among Chinese Residents in 2023', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()