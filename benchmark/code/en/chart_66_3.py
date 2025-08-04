import matplotlib.pyplot as plt
import numpy as np

# Data categories
user_types = ["Ointment Users", "Non - Ointment Users"]
# Age group labels
age_labels = ["Post - 95s", "Post - 90s", "Post - 85s", "Pre - 85s"]
# Correct the data structure: each sub - list represents the distribution of a user type across age groups
data = [
    [36.5, 32.5, 18.9, 12.2],  # Ointment users
    [33.1, 29.0, 21.6, 16.4]   # Non - ointment users
]
# Color settings
colors = ["#A4C639", "#8DB328", "#7EA11E", "#668718"]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a stacked bar chart
x = np.arange(len(user_types))
bar_width = 0.6

# Draw stacked bars for each user type separately
for i, user_data in enumerate(data):
    bottom = 0
    for j, value in enumerate(user_data):
        ax.bar(
            x[i], value, bar_width, bottom=bottom, 
            color=colors[j], label=age_labels[j] if i == 0 else "",  # Add legend only on the first draw
            edgecolor="white"
        )
        # Add data labels in the middle of the bars
        ax.text(
            x[i], bottom + value/2, f"{value}%",
            ha='center', va='center', color='white', fontweight='bold'
        )
        bottom += value

# Set the axes and title
ax.set_xticks(x)
ax.set_xticklabels(user_types, fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_title('Pet owner age distribution (by user type)', fontsize=16, pad=15)

# Set the y - axis range
ax.set_ylim(0, 100)

# Add a legend (remove duplicates)
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys(), loc='upper right', bbox_to_anchor=(1.2, 1))

# Beautify the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()