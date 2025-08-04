import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
months = ["Jan", "Feb", "Mar"]
years = ["2023", "2024", "2025"]

# Data: [2023, 2024, 2025] (minutes)
data = np.array([
    [286.5, 267.9, 265.5],  # Jan
    [288.3, 272.6, 267.9],  # Feb
    [300.6, 278.9, 268.0],  # Mar
])

# Color style upgrade
colors = ["#7CB342", "#66BB6A", "#00ACC1"]  # Corresponding to 2023/2024/2025
markers = ["o", "s", "D"]

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(9, 5.5))

# -------------------- Draw Multiple Lines --------------------
x = np.arange(len(months))
for i in range(len(years)):
    y = data[:, i]
    ax.plot(
        x, y, marker=markers[i], linewidth=2.5, 
        label=years[i], color=colors[i]
    )
    # Add data labels
    for j, val in enumerate(y):
        ax.text(
            x[j], val + 3,
            f"{val}", ha='center', fontsize=9,
            color=colors[i], fontweight='bold'
        )

# -------------------- Year-on-Year Growth Rate Labels (2024→2025) --------------------
for i in range(len(months)):
    rate = data[i][2] - data[i][1]
    rate_pct = round((rate / data[i][1]) * 100, 1)
    color = "red" if rate_pct < 0 else "green"
    ax.text(
        x[i] + 0.05, data[i][2] + 10,
        f"{rate_pct:+}%", color=color,
        fontsize=9, ha="left", va="center", fontweight="bold"
    )

# -------------------- Beautify the Chart --------------------
ax.set_xticks(x)
ax.set_xticklabels(months, fontsize=11)
ax.set_ylabel("Single-machine Daily Effective Time (minutes)", fontsize=11)
ax.set_title("mUserTracker-2023-2025Q1 Single-machine Daily Effective Time", fontsize=14, fontweight="bold", pad=15)

# Grid lines
ax.grid(alpha=0.2)

# Legend
ax.legend(loc="upper right", fontsize=9, frameon=True)

# Remove redundant borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()