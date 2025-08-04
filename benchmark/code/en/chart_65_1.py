import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib import cm

# -------------------- Data Definition --------------------
platforms = ["Douyin", "Bilibili", "WeChat", "Kuaishou", "Weibo", "Overseas Channels", "Xiaohongshu", "Zhihu", "Others"]
data = [53.4, 48.6, 48.0, 24.9, 24.0, 19.5, 15.3, 11.3, 19.8]
x = np.arange(len(platforms))

# -------------------- Color Setting (Gradient Blue - Purple) --------------------
cmap = cm.get_cmap("cool")  # Blue - purple gradient
colors = [cmap(i / len(data)) for i in range(len(data))]

# -------------------- Create Canvas --------------------
fig, ax = plt.subplots(figsize=(9, 6))

# -------------------- Draw Rounded Bar Chart --------------------
bar_height = 0.5
for i, (platform, value) in enumerate(zip(platforms, data)):
    rect = patches.FancyBboxPatch(
        (0, i - bar_height / 2),  # Starting point (x, y)
        value, bar_height,        # Width, height
        boxstyle="round,pad=0.1",
        linewidth=0,
        facecolor=colors[i],
        edgecolor="none",
        alpha=0.9
    )
    ax.add_patch(rect)

    # Add data labels
    ax.text(value + 1, i, f"{value}%", va="center", ha="left",
            fontsize=10, fontweight="bold", color="#424242")

# -------------------- Beautify the Chart --------------------
ax.set_xlim(0, max(data) + 10)
ax.set_ylim(-0.5, len(platforms) - 0.5)
ax.set_yticks(x)
ax.set_yticklabels(platforms, fontsize=11, color="#333333")

ax.set_xticks([])
ax.set_xlabel("")  # Do not display the x - axis
ax.set_title("Platforms Preferred by Chinese Creators for Content Publishing", fontsize=14, fontweight="bold", pad=20)

# Hide the frame
for spine in ["top", "right", "bottom", "left"]:
    ax.spines[spine].set_visible(False)

# Remove ticks
ax.tick_params(axis="both", which="both", length=0)

plt.tight_layout()
plt.show()