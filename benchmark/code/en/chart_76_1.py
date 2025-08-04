import matplotlib.pyplot as plt
import numpy as np

# Data
years = ["Q1 2021", "Q1 2022"]
usage_time = [316.8, 332.9]
growth_rate = 5.1

# Colors: Blue - Orange contrast
colors = ['#6495ED', '#FFA07A']

# Set the canvas
fig, ax = plt.subplots(figsize=(8, 6))

# The y - axis of the symmetric bar chart is the shared item (here set as a single item "Single - machine usage time")
y = ["Single - machine daily effective usage time"]
y_pos = np.arange(len(y))

# Horizontal bar lengths (negative for 2021, positive for 2022)
bar_2021 = [-usage_time[0]]
bar_2022 = [usage_time[1]]

# Draw the bar charts on the left and right sides
ax.barh(y_pos, bar_2021, color=colors[0], height=0.4, label=years[0])
ax.barh(y_pos, bar_2022, color=colors[1], height=0.4, label=years[1])

# Add data labels
ax.text(bar_2021[0] - 10, y_pos[0], f"{usage_time[0]}", va='center', ha='right', fontsize=10, color=colors[0])
ax.text(bar_2022[0] + 10, y_pos[0], f"{usage_time[1]}", va='center', ha='left', fontsize=10, color=colors[1])

# Growth rate annotation (middle arrow)
ax.annotate(f'+{growth_rate}%',
            xy=(0, y_pos[0]),
            xytext=(0, y_pos[0] + 0.3),
            ha='center',
            fontsize=11,
            color='green',
            arrowprops=dict(arrowstyle="->", color='green'))

# Set the x - axis
ax.set_xticks(np.arange(-400, 401, 100))
ax.set_xlim(-400, 400)
ax.axvline(0, color='gray', linewidth=1)  # Center line

# Set the y - axis
ax.set_yticks(y_pos)
ax.set_yticklabels(y)
ax.set_title("mUserTracker: Comparison of single - machine daily usage time between Q1 2021 and Q1 2022 (Symmetric chart)", fontsize=13, fontweight="bold")

# Legend
ax.legend(loc='upper right')

# Beautification
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()