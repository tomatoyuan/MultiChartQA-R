import matplotlib.pyplot as plt
import numpy as np

# Data definition (corresponding to the original image structure, the values can be fine - tuned)
years = ["2018", "2019", "2020", "2021", "2022", "2023"]
incomes = [28228, 30733, 32189, 35128, 36883, 39218]  # Simulated data, can be replaced with real values

# Color configuration (close to the green color scheme of the original image)
bar_color = "#81c784"

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart
x = np.arange(len(years))
bars = ax.bar(x, incomes, color=bar_color, width=0.6, edgecolor="white", linewidth=1)

# Add numerical annotations
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 500,  # Offset upwards to avoid occlusion
        f"{height}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold",
        color="#424242"
    )

# Beautify the chart
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=12, color="#424242")
ax.set_ylabel("Per capita disposable income (yuan)", fontsize=12, color="#424242")

# Hide the top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Add a title
ax.set_title(
    "National per capita disposable income (yuan) from 2018 to 2023",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Adjust the layout
plt.tight_layout()

plt.show()