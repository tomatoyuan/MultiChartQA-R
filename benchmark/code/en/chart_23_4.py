import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ["Ignore marriage urging", "Other attitudes"]
sizes = [50, 50]
colors = ["#FF6B6B", "#4ECDC4"]  # Use a more modern color scheme
explode = (0.05, 0)  # Highlight the first part

# Create the figure and axes
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Draw a donut chart
wedges, texts, autotexts = ax.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct=lambda p: f'{p:.1f}%\n({int(p*sum(sizes)/100)} people)' if p > 0 else '',
    startangle=90,
    colors=colors,
    wedgeprops={"width": 0.4, "edgecolor": "w", "linewidth": 2},
    textprops={"fontsize": 12, "color": "#333333"},
)

# Set the title
ax.set_title("Distribution of respondents' attitudes towards marriage urging", fontsize=16, fontweight="bold", pad=20)

# Adjust the legend
ax.legend(wedges, labels, title="Attitude types", loc="center left", bbox_to_anchor=(1, 0.3, 0.5, 1))

# Add data label styles
for autotext in autotexts:
    autotext.set_fontweight("bold")

# Background and grid settings
fig.patch.set_facecolor('#f8f9fa')
ax.set_facecolor('#f8f9fa')

# Set the axis ratio
plt.axis('equal')

# Add annotation instructions
plt.figtext(0.5, 0.01, "Data source: Fictitious example", ha="center", fontsize=9, bbox={"facecolor": "white", "alpha": 0.5, "pad": 5})

# Adjust the layout
plt.tight_layout()

# Save the chart (optional)
# plt.savefig('marriage_pressure_attitude.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()