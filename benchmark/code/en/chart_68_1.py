import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set the style and color palette
plt.style.use("ggplot")
sns.set_palette("Set2")

# Data
categories = ["PaaS Vendor Revenue", "Resource Cost", "R&D Cost", "Gross Profit"]
data = [100, 33, 37, 30]
colors = sns.color_palette("flare", len(data))  # Bright gradient color scheme

# Polar plot (a variant of radar chart) - only one dimension, can also be simulated with a pie chart
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# Polar angles
angles = np.linspace(0, 2 * np.pi, len(data), endpoint=False).tolist()
# Close the shape
data += data[:1]
angles += angles[:1]

# Plotting
ax.fill(angles, data, color=colors[0], alpha=0.25)
ax.plot(angles, data, color=colors[0], linewidth=2, linestyle="-", marker='o')

# Add data labels
for angle, value, label in zip(angles[:-1], data[:-1], categories):
    ax.text(
        angle,
        value - 5,  # Offset outward a bit to prevent overlapping with the graph, adjustable
        f"{value}%",
        ha='center',
        va='top',
        fontsize=10,
        color='black',
        fontweight='bold'
    )

# Set category labels
categories += categories[:1]
ax.set_xticks(angles)
ax.set_xticklabels(categories, fontsize=11)

# Set the title
plt.title("RTC PaaS Vendor Profitability Distribution (Polar View)", fontsize=14, fontweight="bold", pad=20)

# Configure the axis range
ax.set_rlabel_position(30)
ax.set_yticks([25, 50, 75, 100])
ax.set_yticklabels(["25%", "50%", "75%", "100%"], fontsize=10)
ax.grid(color="gray", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()