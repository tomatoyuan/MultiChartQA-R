import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# -------------------- Data Preparation --------------------
reasons = [
    "Doctor's advice", "Want to try other methods first", 
    "Personally think it's unnecessary to wear glasses", "Child is unwilling to wear glasses", "Other"
]
percentages = [41.2, 36.5, 14.4, 7.9, 0.1]

# Polar coordinate angle division (one angle for each category)
angles = np.linspace(0, 2 * np.pi, len(reasons), endpoint=False)
# Convert data to numpy array
data = np.array(percentages)

# Set color gradient
cmap = cm.get_cmap("autumn_r")  # Orange - red gradient
colors = [cmap(i / len(data)) for i in range(len(data))]

# -------------------- Create Polar Plot --------------------
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Set starting angle & arrangement direction
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Draw polar bar chart
bars = ax.bar(angles, data, width=0.5, color=colors, edgecolor="white", linewidth=1)

# Add data labels
for i, (bar, percentage) in enumerate(zip(bars, data)):
    angle = angles[i]
    ax.text(
        angle, bar.get_height(),
        f"{percentage}%",
        ha='center', va='bottom',
        fontsize=10, fontweight="bold",
        color="#424242"
    )

# Add labels (categories)
ax.set_xticks(angles)
ax.set_xticklabels(reasons, fontsize=10, color="#333333")

# Remove polar axis and tick marks
ax.set_yticklabels([])
ax.spines["polar"].set_visible(False)
ax.grid(False)

# Add title
ax.set_title("Reasons for not getting glasses immediately or not getting glasses yet", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.show()