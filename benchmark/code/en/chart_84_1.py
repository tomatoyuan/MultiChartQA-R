import matplotlib.pyplot as plt
import numpy as np

# -------------------- Data Definition --------------------
years = ["2019", "2020", "2021"]
x = np.arange(len(years))
consumption_scale = [100, 200, 300]

# Interpolate the data into a smooth curve (preparation for the area chart fitting)
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = np.interp(x_smooth, x, consumption_scale)

# -------------------- Create the Canvas --------------------
fig, ax = plt.subplots(figsize=(7, 5))

# -------------------- Draw the Area Chart --------------------
ax.plot(x, consumption_scale, marker='o', color="#4dd0e1", linewidth=3, label="Consumption Scale")
ax.fill_between(x_smooth, np.interp(x_smooth, x, consumption_scale), color="#b2ebf2", alpha=0.6)

# -------------------- Add Data Annotations --------------------
for i, val in enumerate(consumption_scale):
    ax.text(
        x[i], val + 10,
        f"{val}",
        ha='center', va='bottom',
        fontsize=10,
        fontweight="bold",
        color="#00796b"
    )

# -------------------- Axis Settings --------------------
ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11, color="#424242")

ax.set_yticks([])
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# -------------------- Add Title and Legend --------------------
ax.set_title(
    "Trend of Consumption Scale of 'Functional Snacks' on Tmall Global from 2019 to 2021",
    fontsize=14,
    fontweight="bold",
    pad=20
)

ax.legend(loc="upper left", fontsize=10, frameon=True, facecolor="white", edgecolor="white")

# -------------------- Layout and Display --------------------
plt.tight_layout()
plt.show()