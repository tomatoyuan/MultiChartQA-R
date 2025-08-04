import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Population categories
groups = ["New - generation white - collar", "Gen Z", "Small - town youth", "Small - town middle - aged and elderly", "Senior middle - class", "Exquisite moms", "Urban blue - collar", "Urban senior citizens"]
# Data categories (corresponding to the legend)
categories = ["(Tmall Global) Proportion of the overall hair and beauty population", "(Taobao Tmall) Proportion of the overall hair and beauty population"]
# Simulated data (adjustable), range 0 - 25 (example values)
data = np.array([
    [22, 12],  # New - generation white - collar
    [20, 16],  # Gen Z
    [18, 17],  # Small - town youth
    [15, 24],  # Small - town middle - aged and elderly
    [12, 8],   # Senior middle - class
    [10, 5],   # Exquisite moms
    [8, 15],   # Urban blue - collar
    [3, 4]     # Urban senior citizens
]).T  # Transposed shape (2, 8) to match the platform - population structure

# Create a canvas
fig, ax = plt.subplots(figsize=(12, 6))

# Draw a grouped bar chart
x = np.arange(len(groups))
bar_width = 0.35
for i in range(len(categories)):
    offset = bar_width * i
    ax.bar(x + offset, data[i], width=bar_width, 
           color="#A4C639" if i == 0 else "#87CEEB",
           label=categories[i])

# Add data labels
for i in range(len(groups)):
    for j in range(len(categories)):
        height = data[j][i]
        ax.annotate(f'{height}%',
                    xy=(x[i] + bar_width * j, height),
                    xytext=(0, 3),  # Label position: offset 3 above
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# Set x - axis ticks and labels
ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(groups, rotation=45, ha='right')  # Rotate labels to avoid overlap
# Set y - axis ticks (0 - 40%)
ax.set_ylim(0, 40)
ax.set_yticks([0, 20, 40])
# Set the title
ax.set_title("Tmall Global: Proportion of the eight major Taobao FMCG populations in hair and beauty", 
             fontsize=16, fontweight="bold", y=1.05)

# Custom legend
legend_elements = [Patch(facecolor="#A4C639", label=categories[0]),
                   Patch(facecolor="#87CEEB", label=categories[1])]
ax.legend(handles=legend_elements, loc="upper right")

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()