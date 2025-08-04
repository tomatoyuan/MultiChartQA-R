import matplotlib.pyplot as plt
import numpy as np

# Data definition (corresponding to the original image structure, numerical values can be fine - tuned)
age_groups = ["18-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "≥60"]
percentages = [23.3, 17.3, 17.3, 13.3, 10.2, 7.6, 5.3, 2.8, 2.8]  # Percentage data
tgis = [159, 119, 93, 90, 89, 76, 69, 63, 75]  # TGI data

# Color configuration (similar to the green color scheme of the original image)
bar_color = "#81c784"

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a horizontal bar chart
y = np.arange(len(age_groups))
bars = ax.barh(y, percentages, color=bar_color, height=0.6, edgecolor="white", linewidth=1)

# Add percentage value labels
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # Offset 1 unit to the right
        bar.get_y() + bar.get_height() / 2,
        f"{width}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# Add TGI labels (on the left side of the bars, simulating the layout of the original image)
for i, (age, tgi) in enumerate(zip(age_groups, tgis)):
    ax.text(
        -3,  # Offset to the left, can be adjusted according to the actual situation
        y[i] + bar.get_height() / 2,
        f"TGI: {tgi}",
        va="center",
        ha="right",
        fontsize=9,
        color="#424242"
    )

# Beautify the chart
ax.set_yticks(y)
ax.set_yticklabels(age_groups, fontsize=12, color="#424242")
ax.set_xticks([])  # Hide x - axis ticks

# Hide the frame
for spine in ax.spines.values():
    spine.set_visible(False)

ax.tick_params(axis="y", left=False)  # Hide y - axis tick marks

# Add a title
ax.set_title(
    "Protein milk powder: Age groups",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout (center the content and leave space for the left - side TGI labels)
plt.subplots_adjust(left=0.2, right=0.9, top=0.85, bottom=0.1)

plt.show()