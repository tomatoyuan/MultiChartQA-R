import matplotlib.pyplot as plt

# Data preparation
categories = [
    "Fatigue susceptibility", "Weight issues", "Skin problems", "Gastrointestinal/digestive tract",
    "Anxiety/depressive mood", "High blood pressure, blood sugar and blood lipid", "Respiratory problems", "None of the above"
]
percentages = [53, 50, 48, 47, 44, 29, 19, 10]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a horizontal bar chart with gradient colors
colors = plt.cm.viridis([i/len(categories) for i in range(len(categories))])
bars = ax.barh(categories, percentages, color=colors, edgecolor='gray', alpha=0.8)

# Add a title and axis labels
ax.set_title("Specific aspects of the increase in consumers' physical health problems in the past year", fontsize=16, pad=15)
ax.set_xlabel("Percentage (%)", fontsize=14, labelpad=10)
ax.set_ylabel("Health problem types", fontsize=14, labelpad=10)

# Set the x - axis range and ticks
ax.set_xlim(0, max(percentages) * 1.1)  # Slightly expand the x - axis range
ax.set_xticks(range(0, 60, 10))

# Add grid lines
ax.grid(axis='x', linestyle='--', alpha=0.6)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2,
            f'{width}%', ha='left', va='center', fontsize=12)

# Beautify the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='both', which='major', labelsize=12)

# Adjust the layout
plt.tight_layout()

# Display the graph
plt.show()