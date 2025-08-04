import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Population categories
groups = ["Female Population", "Population with Postgraduate Education", "Population under 30", "Population in Tier 1 and 2 Cities", "High - Income Population", "High - Consumption Population"]
# Data categories (corresponding to the legend)
categories = ["(Tmall Global) Proportion of Overall Hair and Beauty Population", "(Tmall + Taobao) Proportion of Overall Hair and Beauty Population"]
# Correct the data structure: transpose to match the population categories (6 categories)
data = np.array([
    [85, 55, 60, 65, 50, 40],  # Tmall Global: Proportion of each population
    [70, 35, 50, 55, 38, 20]   # Tmall + Taobao: Proportion of each population
]).T  # After transposing, the shape is (6, 2), matching the number of population categories

# Annotation text
annotation_text = "Tmall Global has more people with high education and high consumption."
# Arrow parameters
arrowprops = dict(arrowstyle="->", color="green", connectionstyle="arc3,rad=0.2")

# Create a canvas
fig, ax = plt.subplots(figsize=(10, 7))

# Draw a grouped horizontal bar chart
y = np.arange(len(groups))
bar_height = 0.35
for i in range(len(categories)):
    offset = bar_height * i
    ax.barh(y + offset, data[:, i], height=bar_height, 
            color="#A4C639" if i==0 else "#EBD487",
            label=categories[i])

# Add data annotations
for i in range(len(groups)):
    for j in range(len(categories)):
        width = data[i, j]
        ax.annotate(f'{width}%',
                    xy=(width, y[i] + bar_height*j),
                    xytext=(5, 0),  # Annotation position: offset 5 to the right
                    textcoords="offset points",
                    ha='left', va='center',
                    color='black')

# Set the y - axis ticks and labels (center the grouped display)
ax.set_yticks(y + bar_height/2)
ax.set_yticklabels(groups)
# Set the x - axis ticks (0 - 100%)
ax.set_xlim(0, 100)
ax.set_xticks([0, 50, 100])
# Set the title
ax.set_title("Hair and Beauty Population Portrait: Tmall Global vs Tmall + Taobao", 
             fontsize=16, fontweight="bold", y=1.03)

# Custom legend
legend_elements = [Patch(facecolor="#A4C639", label=categories[0]),
                   Patch(facecolor="#EBD487", label=categories[1])]
ax.legend(handles=legend_elements, loc="right")

# Beautification: hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()