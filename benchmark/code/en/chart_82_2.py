import matplotlib.pyplot as plt
import numpy as np

# Pain point categories
pain_points = [
    "High work - life stress, prone to emotional tension/depression",
    "Subjectively dissatisfied with one's own body/physique",
    "Sub - health state, suffering from chronic diseases such as cervical spondylosis",
    "Social media marketing triggers body/lifestyle anxiety",
    "Having bad living habits/addictions such as staying up late and smoking",
    "Difficulty in balancing work and life, with less free time",
    "Narrow social circle, hoping to make more friends",
    "Disposable income is insufficient to meet consumption needs"
]
# Corresponding percentages (%)
percentages = [55.1, 50.7, 47.0, 43.8, 41.6, 39.9, 31.9, 29.7]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(8, 6))

# Draw a bar chart (horizontal bar chart, adjusted to be consistent with the original image)
y = np.arange(len(pain_points))
bar_width = 0.6
bars = ax.barh(y, percentages, height=bar_width, color="#A4C639")

# Add data labels
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # Adjust the label position
                textcoords="offset points",
                ha='left', va='center')

# Set y - axis ticks and labels (adjust the order so that the first pain point is at the top)
ax.set_yticks(y)
ax.set_yticklabels(pain_points)
# Hide x - axis ticks
ax.set_xticks([])
# Set the title
ax.set_title("Main pain points in the daily life and work of Chinese fitness users in 2022", fontsize=14, fontweight="bold")

# Simulate different border styles (according to the original image, some entries have dashed borders. Here is a simplified demonstration and can be expanded as needed)
# For example, add a dashed border to "Sub - health state, suffering from chronic diseases such as cervical spondylosis"
special_index = 2
special_bar = bars[special_index]
x0, y0 = special_bar.get_xy()
width, height = special_bar.get_width(), special_bar.get_height()
# Draw a dashed rectangular border
rect = plt.Rectangle((x0, y0), width, height, fill=False, edgecolor='blue', linestyle='--')
ax.add_patch(rect)

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()  # Automatically adjust the layout
plt.show()