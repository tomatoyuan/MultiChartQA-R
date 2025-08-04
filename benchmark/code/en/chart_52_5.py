import matplotlib.pyplot as plt
import numpy as np

# Data definition (corresponding to the original image structure, the values can be fine - tuned)
categories = ["Morning", "Daytime", "Night (including early morning)", "Non - fixed fragmented time"]
values = [3.0, 24.8, 53.2, 19.0]  # Simulated data, can be replaced with real values
special_label = {
    "Night (including early morning)": "Graduate student TGI = 121\nCentral China region TGI = 130"
}

# Color configuration (close to the green color scheme of the original image)
bar_color = "#81c784"
border_color = "#dcedc1"  # Dashed box color

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a horizontal bar chart
y = np.arange(len(categories))
bars = ax.barh(y, values, color=bar_color, height=0.6, edgecolor="white", linewidth=1)

# Add numerical annotations
for bar in bars:
    width = bar.get_width()
    ax.text(
        width + 1,  # Offset 1 unit to the right
        bar.get_y() + bar.get_height()/2,
        f"{width}%",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# Draw a dashed box for the special dimension (Night)
target_idx = categories.index("Night (including early morning)")
target_bar = bars[target_idx]
x0, y0 = target_bar.get_xy()
w, h = target_bar.get_width(), target_bar.get_height()
# Draw a dashed rectangular box
rect = plt.Rectangle(
    (x0 - 0.2, y0 - 0.1),  # Expand the margin outward a bit
    w + 0.4, h + 0.2,
    fill=False,
    linestyle="--",
    color=border_color,
    linewidth=2
)
ax.add_patch(rect)

# Add text annotations for the special dimension (Graduate student TGI, etc.)
if "Night (including early morning)" in special_label:
    ax.text(
        x0 + w + 7,  # Offset to the right
        y0 + h/2,
        special_label["Night (including early morning)"],
        va="center",
        fontsize=9,
        color="#424242",
        linespacing=1.2
    )

# Beautify the chart
ax.set_yticks(y)
ax.set_yticklabels(categories, fontsize=12, color="#424242")
ax.set_xticks([])  # Hide x - axis tick marks
# Hide the border
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(axis="y", left=False)  # Hide y - axis tick lines

# Add a title
ax.set_title(
    "Time when college students most often write papers",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout (center the content)
plt.subplots_adjust(left=0.2, right=0.7, top=0.85, bottom=0.1)

plt.show()