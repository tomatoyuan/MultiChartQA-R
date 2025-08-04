import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = ["2006-2016", "2017", "2018", "2019", "2020", "2021", "Total"]
x = np.arange(len(years))
quantities = [6, 7, 18, 40, 47, 76, 194]

# Prepare step data for the step chart
x_step = np.repeat(x, 2)[1:]
y_step = np.repeat(quantities, 2)[:-1]

# Color scheme (gradient scheme)
fill_color = "#b2dfdb"      # Main color of the filled area
line_color = "#00796b"      # Curve color
point_color = "#009688"     # Marking point color

# -------------------- Create the canvas --------------------
fig, ax = plt.subplots(figsize=(9, 5))

# -------------------- Draw the step area chart --------------------
ax.step(x, quantities, where='mid', color=line_color, linewidth=2.5, label="Annual number of hydrogen refueling stations built")
ax.fill_between(x_step, y_step, step='pre', alpha=0.3, color=fill_color)

# -------------------- Add data points and annotations --------------------
ax.plot(x, quantities, "o", color=point_color)

for i, val in enumerate(quantities):
    ax.text(
        x[i], val + 5,
        str(val),
        ha='center', va='bottom',
        fontsize=10,
        fontweight='bold',
        color=point_color
    )

# -------------------- Axes and labels --------------------
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")
ax.set_ylabel("Number of hydrogen refueling stations in China (units)", fontsize=11)
ax.set_ylim(0, max(quantities) + 30)

# -------------------- Legend and title --------------------
ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="white")
ax.set_title("Number of hydrogen refueling stations built in China from 2006 to 2021", fontsize=14, fontweight='bold', pad=20)

# -------------------- Beautify --------------------
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()