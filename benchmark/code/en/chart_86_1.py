import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data definition --------------------
years = ["2019", "2020", "2021"]
quantity = [12, 14, 17]
x = np.arange(len(years))

# Bubble size and color
sizes = np.array(quantity) ** 2.5 * 5  # Adjust the exponent to enlarge the difference
colors = ["#90caf9", "#ce93d8", "#f48fb1"]  # Gradient blue - purple - pink color scheme

# -------------------- Create a canvas --------------------
fig, ax = plt.subplots(figsize=(7, 5))

# -------------------- Draw a bubble chart --------------------
for i in range(len(x)):
    ax.scatter(
        x[i], quantity[i],
        s=sizes[i],
        color=colors[i],
        alpha=0.7,
        edgecolors="white",
        linewidth=2
    )
    # Add data labels
    ax.text(
        x[i], quantity[i] + 0.5,
        f"{quantity[i]}",
        ha='center', va='bottom',
        fontsize=14,
        fontweight='bold',
        color='white'
    )

# -------------------- Set the axes --------------------
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")
ax.set_yticks([])  # Do not display y - axis ticks
ax.set_xlim(-0.5, len(x) - 0.5)
ax.set_ylim(0, max(quantity) + 5)

# -------------------- Title and beautification --------------------
ax.set_title(
    "Trend of the number of variety shows and female - oriented variety shows from 2019 to 2021 in SVC",
    fontsize=14,
    fontweight="bold",
    pad=20
)

# Beautify the border
for spine in ["top", "right", "left", "bottom"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()