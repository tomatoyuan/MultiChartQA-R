import matplotlib.pyplot as plt
import numpy as np

# Years
years = ["2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022e", "2023e"]
# Market size (trillion yuan)
market_size = [3, 3, 4, 4, 4, 5, 4, 5, 5, 6]
# Year-on-year growth rate (%)
growth_rate = [11.7, 10.8, 10.7, 7.7, 9.4, -15.4, 18.9, 14.2, 12.4]
# Stage division
stages = ["Steady Growth Period"] * 5 + ["Trough Period"] + ["Recovery Period"] + ["New Vitality Period"] * 2
stage_x = [0, 4, 5, 6, 7, 9]  # X-coordinate boundaries for drawing stage backgrounds, need to match the number of years. Here is a simple example and can be refined.
stage_y = [-0.5] * len(stage_x)
stage_height = [1] * len(stage_x)
stage_colors = ["#BDDEB3", "#BDDEB3", "#BDDEB3", "#BDDEB3", "#BDDEB3", "#A6CADD", "#A6CADD", "#A6CADD", "#A6CADD", "#A6CADD"]  # Simulate stage colors

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 6))

# Draw a bar chart (market size)
x = np.arange(len(years))
bar_width = 0.6
bars = ax.bar(x, market_size, width=bar_width, color="#A4C639", label="China's catering market size (trillion yuan)")

# Draw a line chart (year-on-year growth rate)
ax2 = ax.twinx()
ax2.plot(x[:-1], growth_rate, marker='o', color="#87CEEB", label="Year-on-year growth rate (%)", linewidth=2)  # The growth rate data is one less than the years, pay attention to slicing.

# Add market size annotations
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom',
                color="#A4C639")

# Add growth rate annotations
for i, rate in enumerate(growth_rate):
    ax2.annotate(f'{rate}%',
                 xy=(x[i], rate),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 color="#87CEEB")

# Draw stage backgrounds (simple simulation. If precise positions are needed, the coordinates need to be refined.)
for i in range(len(stages)):
    ax.axvspan(i, i + 1, facecolor=stage_colors[i], alpha=0.3)

# Manually add stage texts (because the automatic layout is complex, here it is simply placed and can be adjusted according to the actual situation.)
stage_texts = ["Steady Growth Period", "Trough Period", "Recovery Period", "New Vitality Period"]
ax.text(1, -0.5, stage_texts[0], ha='center', va='top', fontweight='bold')
ax.text(4.5, -0.5, stage_texts[1], ha='center', va='top', fontweight='bold')
ax.text(6.5, -0.5, stage_texts[2], ha='center', va='top', fontweight='bold')
ax.text(8.3, -0.5, stage_texts[3], ha='center', va='top', fontweight='bold')

# Set x-axis ticks
ax.set_xticks(x)
ax.set_xticklabels(years)
# Set the y-axis (market size) range
ax.set_ylim(0, 7)
# Set the title
ax.set_title("China's catering market size from 2014 to 2023", fontsize=14, fontweight="bold")

# Combine legends
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()