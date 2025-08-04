import matplotlib.pyplot as plt
import numpy as np

# Top 10 factors affecting sleep
factors = [
    "Can't resist using mobile phones/tablets before sleep", "Habituated to staying up late without motivation to change",
    "High life stress affects rest", "Staying up late to study or work affects rest",
    "Retaliatory staying up late at night due to lack of freedom during the day",
    "Poor bedroom sound insulation and noisy environment", "Roommates/partners affect my sleep",
    "Uncomfortable mattresses, pillows, etc.", "Inappropriate bedroom temperature and humidity",
    "Physical illness affects sleep"
]
# Simulated percentage data (close to the original chart)
percentages = [15.9, 13.6, 12.9, 9.5, 8.1, 7.2, 6.2, 5.6, 4.5, 3.5]
# Free color matching (adjustable, using blue in the example)
bar_color = "#87CEEB"

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a horizontal bar chart
y = np.arange(len(factors))
bar_height = 0.6
bars = ax.barh(y, percentages, height=bar_height, color=bar_color)

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar_height / 2),
                xytext=(5, 0),
                textcoords="offset points",
                ha='left', va='center',
                color='black')

# Set y-axis ticks and labels
ax.set_yticks(y)
ax.set_yticklabels(factors)
# Set x-axis ticks (0 - 17%, suitable for the data)
ax.set_xlim(0, 17)
# Set the title
ax.set_title("Top 10 Factors Affecting Sleep", fontsize=14, fontweight="bold")

# Beautification: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()