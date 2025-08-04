import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# Group categories
groups = ["Transaction volume year - on - year growth", "Unit price year - on - year growth"]
# Data categories (corresponding to the legend)
categories = ["Beauty & Haircare (Tmall Global)", "Beauty & Haircare (Tmall + Taobao)"]
# Simulated data (can be adjusted)
data = [[35, 25],  # Transaction volume year - on - year growth: Tmall Global, Tmall + Taobao
        [18, 10]]  # Unit price year - on - year growth: Tmall Global, Tmall + Taobao

# Annotation text
annotation_text = "Tmall Global has obvious advantages in transaction volume year - on - year growth and unit price year - on - year growth"
# Arrow parameters
arrowprops = dict(arrowstyle="->", color="green", connectionstyle="arc3,rad=0.2")

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw grouped bar charts
x = np.arange(len(groups))
bar_width = 0.35
for i in range(len(categories)):
    offset = bar_width * i
    ax.bar(x + offset, data[i], width=bar_width, 
           color="#C63974" if i == 0 else "#87CEEB",
           label=categories[i])

# Add data annotations
for i in range(len(groups)):
    for j in range(len(categories)):
        height = data[j][i]
        ax.annotate(f'{height}%',
                    xy=(x[i] + bar_width * j, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom',
                    color='black')

# Set x - axis ticks and labels
ax.set_xticks(x + bar_width / len(categories))
ax.set_xticklabels(groups)
# Set y - axis ticks
ax.set_ylim(0, 40)
# Set the title
ax.set_title("Growth of Chinese Beauty & Haircare market: \nComparison of the latest one - month data between March 2021 and March 2022", 
             fontsize=14, fontweight="bold", y=1.1)

# Custom legend (to avoid the problem of the automatically generated legend order)
legend_elements = [Patch(facecolor="#C63974", label=categories[0]),
                   Patch(facecolor="#87CEEB", label=categories[1])]
ax.legend(handles=legend_elements, loc="upper right")

# Beautify: Hide the top and right borders
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

# plt.tight_layout()
plt.show()