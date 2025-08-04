import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
# Pie chart data
pie_labels = ["One pair", "Others"]
pie_sizes = [53.2, 46.8]
pie_colors = ["#dcdcdc", "#a5d6a7"]  # Gray, light green

# Nested bar chart data (split of "Others" category)
bar_labels = ["Two pairs", "Three pairs and above"]
bar_sizes = [42.7, 4.1]  # Note: 42.7 + 4.1 = 46.8, matching the "Others" proportion in the pie chart
bar_colors = ["#a5d6a7", "#81c784"]  # Light green, dark green

# -------------------- Create the canvas --------------------
fig, (ax_pie, ax_bar) = plt.subplots(1, 2, figsize=(8, 5), gridspec_kw={"width_ratios": [1, 2]})

# -------------------- Draw the pie chart --------------------
wedges, texts, autotexts = ax_pie.pie(
    pie_sizes,
    labels=pie_labels,
    autopct="%1.1f%%",  # Display percentages
    startangle=90,      # Starting angle (place the "One pair" part on the left)
    colors=pie_colors,
    textprops={
        "fontsize": 10, 
        "color": "#424242",
        "fontweight": "bold"
    },
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 1
    }
)

# Adjust the position of pie chart text (avoid overlap)
for text, auto in zip(texts, autotexts):
    text.set_fontsize(10)
    auto.set_fontsize(10)

# -------------------- Draw the nested bar chart --------------------
x = np.arange(len(bar_labels))
bar_width = 0.6

ax_bar.bar(
    x, 
    bar_sizes, 
    width=bar_width, 
    color=bar_colors,
    edgecolor="white",
    linewidth=1
)

# Add data labels
for i, val in enumerate(bar_sizes):
    ax_bar.text(
        i, val + 1, 
        f"{val}%",
        ha="center", va="bottom",
        fontsize=9,
        color="#424242",
        fontweight="bold"
    )

# -------------------- Beautify the chart --------------------
# Pie chart optimization
ax_pie.set_aspect("equal")  # Ensure the pie chart is a perfect circle
ax_pie.spines["top"].set_visible(False)
ax_pie.spines["right"].set_visible(False)

# Bar chart optimization
ax_bar.set_xticks(x)
ax_bar.set_xticklabels(bar_labels, fontsize=10, color="#424242")
ax_bar.set_ylim(0, 50)  # The y - axis range matches the data
ax_bar.spines["top"].set_visible(False)
ax_bar.spines["right"].set_visible(False)

# Add a title
fig.suptitle(
    "Distribution of the number of frame glasses owned by myopic people",
    fontsize=14,
    fontweight="bold",
    y=1.05  # Title position
)

# Adjust the layout
plt.tight_layout()

plt.show()