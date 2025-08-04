import matplotlib.pyplot as plt
import numpy as np

# --------------------- Left Pie Chart Data ---------------------
labels_pie = ["$501 - $1000", "$1001 - $3000", "$500 and below", "$3001 and above"]
sizes_pie = [49.5, 41.4, 6.5, 2.6]
colors_pie = ["#D2691E", "#F4A460", "#CD853F", "#FFDEAD"]

# --------------------- Right Grouped Bar Chart Data ---------------------
labels_bar = ["3 times a week or more", "1 - 2 times a week", "1 - 2 times a month", "Once every few months", "Almost no consumption in the university town"]
sizes_bar = [
    [13.5, 86.5],  # First group: Orange below, light - colored above
    [51.8, 48.2],
    [29.5, 70.5],
    [3.6, 96.4],
    [1.6, 98.4]
]
colors_bar = ["#D2691E", "#FAF0E6"]  # Orange, light beige

# Create a canvas with a 1 - row, 2 - column layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# --------------------- Draw the Left Pie Chart ---------------------
wedges, texts, autotexts = ax1.pie(sizes_pie, colors=colors_pie, autopct='%1.1f%%', startangle=90)
ax1.set_title('Monthly average consumption of the main consumer groups in Chinese university towns since 2023')
# Adjust the legend
ax1.legend(wedges, labels_pie, title="Consumption range", loc="center left", bbox_to_anchor=(1, 0.5))
# Adjust the color of the annotation text
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

# --------------------- Draw the Right Grouped Bar Chart ---------------------
# Draw the grouped bar chart (stacked form)
x = np.arange(len(labels_bar))
bottom = np.zeros(len(labels_bar))
for i in range(2):
    ax2.bar(x, [size[i] for size in sizes_bar], bottom=bottom, color=colors_bar[i], label=labels_pie[i] if i == 0 else '')
    bottom += [size[i] for size in sizes_bar]

ax2.set_title('Consumption frequency of the main consumer groups in Chinese university towns in 2023')
ax2.set_ylabel('Proportion (%)')
ax2.set_xticks(x)
ax2.set_xticklabels(labels_bar)
ax2.legend(title="Consumption range", loc="upper left")

# Add numerical annotations to the grouped bar chart
for i, (size1, size2) in enumerate(sizes_bar):
    ax2.text(i, size1 / 2, f'{size1}%', ha='center', va='center', color='white')
    ax2.text(i, size1 + size2 / 2, f'{size2}%', ha='center', va='center', color='black')

# Simulate a yellow dashed box (second group)
ax2.plot([x[1] - 0.3, x[1] + 0.3, x[1] + 0.3, x[1] - 0.3, x[1] - 0.3],
         [0, 0, 100, 100, 0],
         linestyle='--', color='gold', linewidth=2)

plt.suptitle('Behavior analysis of the main consumer groups in Chinese university towns: Consumption range and frequency', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()