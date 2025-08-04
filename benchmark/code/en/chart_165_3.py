import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Compound Prepared\n Dishes/Recipe - Style Seasonings', 'Basic Seasonings', 'Compound Non - Prepared\n Dishes Seasonings', 'Regional Specialty Seasonings']
inner_data = [38, 35, 27, 0]  # 2023 Q1
outer_data = [38, 33, 29, 0]  # 2024 Q1

colors = ['#1f4e79', '#2ca197', '#f6a965', '#d1d1e0']

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal', adjustable='box')

# Inner circle: 2023 Q1
inner_wedges, _ = ax.pie(
    inner_data,
    radius=0.7,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Outer circle: 2024 Q1
outer_wedges, _ = ax.pie(
    outer_data,
    radius=1.0,
    colors=colors,
    startangle=90,
    wedgeprops=dict(width=0.3, edgecolor='white')
)

# Add percentage labels
def add_labels(wedges, data, radius):
    angle = 90
    total = sum(data)
    for i, (wedge, value) in enumerate(zip(wedges, data)):
        if value == 0:
            continue
        theta = (angle - value / total * 360 / 2) * np.pi / 180
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        ax.text(x, y, f'{value}%', ha='center', va='center', fontsize=10)
        angle -= value / total * 360

add_labels(inner_wedges, inner_data, radius=0.55)
add_labels(outer_wedges, outer_data, radius=1.15)

# Add legend
plt.legend(outer_wedges, labels, title="Categories", loc="best", bbox_to_anchor=(1, 0.5))

# Add title
plt.title('Sales Trends of Various Categories in the Condiment Market in Q1 2024\nInner Circle: Q1 2023 | Outer Circle: Q1 2024')

# Add data source description
plt.figtext(
    -0.1, 0.1,
    "Data Source: Magic Mirror Insight, '2024 China Condiment Industry Development Trends'\n"
    "Data Description: The condiment market refers to the products in the condiments/jams/salads/dried \nnon - staple food category under the grain, oil, condiments/instant \nfood/dried goods/baked goods category on the three platforms of Tmall Taobao, JD.com, and Douyin.",
    ha='left', fontsize=9
)

plt.tight_layout()
plt.show()