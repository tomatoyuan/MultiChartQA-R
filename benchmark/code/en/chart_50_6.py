import matplotlib.pyplot as plt
import numpy as np

# Types of smart glasses
glasses_types = ["VR Smart Glasses", "AR Smart Glasses", "AI Display Glasses", "AI Audio Glasses", "AI Photography Glasses", "MR Smart Glasses", "Other Smart Glasses"]
# Corresponding percentages (%), the data is roughly simulated and can be adjusted according to actual situation
percentages = [79.4, 69.8, 63.9, 62.0, 55.8, 38.7, 11.9]

x = np.arange(len(glasses_types))  # Positions of x-axis ticks

fig, ax = plt.subplots()

# Draw a horizontal bar chart with a similar green color
bars = ax.barh(x, percentages, color='greenyellow')

# Add a title
ax.set_title('Types of smart glasses heard of by all respondents')

# Set y-axis tick labels
ax.set_yticks(x)
ax.set_yticklabels(glasses_types)

# Add numerical labels to each bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'{width}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),  # Horizontal offset of 3 points, centered vertically
                textcoords="offset points",
                ha='left', va='center')

# Hide x-axis ticks (The original figure has no obvious x-axis tick display, mainly focusing on bar length and labels)
ax.xaxis.set_ticks([])

plt.show()