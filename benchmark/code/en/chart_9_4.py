import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import random

# Set the random seed to ensure reproducibility of results
np.random.seed(42)
random.seed(42)

# Accurately extract chart data, adjust it to floating - point numbers and add a slight random offset
# Data format: Province: (Search ratio, Attention TGI, Region, Color)
province_data = {
    "Jiangxi": (4.2, 171.5, "Central", "#00cc99"),
    "Tianjin": (2.1, 132.3, "Eastern", "#66b3ff"),
    "Guizhou": (1.9, 121.7, "Western", "#ffcc66"),
    "Hebei": (6.3, 120.8, "Eastern", "#66b3ff"),
    "Shandong": (8.9, 131.2, "Eastern", "#66b3ff"),
    "Jiangsu": (10.1, 140.5, "Eastern", "#66b3ff"),
    "Ningxia": (1.0, 110.3, "Western", "#ffcc66"),
    "Shanghai": (3.2, 99.8, "Eastern", "#66b3ff"),
    "Zhejiang": (7.1, 100.4, "Eastern", "#66b3ff"),
    "Guangdong": (9.3, 100.7, "Eastern", "#66b3ff"),
    "Heilongjiang": (1.1, 90.2, "Northeastern", "#ff6666"),
    "Anhui": (2.9, 90.5, "Central", "#00cc99"),
    "Hubei": (4.1, 89.7, "Central", "#00cc99"),
    "Beijing": (3.8, 90.3, "Eastern", "#66b3ff"),
    "Guangxi": (1.2, 80.4, "Western", "#ffcc66"),
    "Hunan": (3.1, 79.8, "Central", "#00cc99"),
    "Jilin": (0.9, 70.6, "Northeastern", "#ff6666"),
    "Fujian": (3.3, 70.1, "Eastern", "#66b3ff"),
    "Chongqing": (1.1, 70.3, "Western", "#ffcc66"),
    "Yunnan": (1.8, 69.7, "Western", "#ffcc66"),
    "Shanxi": (2.2, 60.5, "Central", "#00cc99"),
    "Gansu": (0.8, 50.2, "Western", "#ffcc66"),
    "Xinjiang": (1.0, 40.3, "Western", "#ffcc66"),
    "Qinghai": (1.1, 30.1, "Western", "#ffcc66"),
    "Tibet": (0.9, 20.4, "Western", "#ffcc66"),
    "Henan": (5.2, 100.2, "Central", "#00cc99"),
    "Hainan": (1.0, 99.8, "Eastern", "#66b3ff"),
    "Liaoning": (3.1, 100.3, "Eastern", "#66b3ff"),
    "Sichuan": (5.0, 99.7, "Western", "#ffcc66"),
    "Inner Mongolia": (2.1, 120.5, "Western", "#ffcc66"),
    "Shaanxi": (1.9, 110.2, "Western", "#ffcc66"),
}

# Group by region
region_dict = defaultdict(list)
for prov, (ratio, tgi, region, color) in province_data.items():
    region_dict[region].append((prov, ratio, tgi, color))

# Create a canvas
plt.figure(figsize=(10, 7), facecolor='white')
ax = plt.gca()

# Draw a scatter plot (loop by region)
for region, prov_list in region_dict.items():
    ratios = [d[1] for d in prov_list]
    tgis = [d[2] for d in prov_list]
    colors = [d[3] for d in prov_list]
    ax.scatter(ratios, tgis, c=colors, label=region, s=50, zorder=2)

    # Add province text labels (fine - tune the position to avoid overlap)
    for d in prov_list:
        prov, ratio, tgi, _ = d
        # Manually fine - tune the label positions of some provinces (adjust according to the original image vision)
        if prov == 'Jiangxi':
            ax.text(ratio + 0.1, tgi - 5, prov, fontsize=9)
        elif prov in ['Tianjin', 'Jiangsu']:
            ax.text(ratio - 0.3, tgi + 2, prov, fontsize=9)
        else:
            ax.text(ratio + 0.1, tgi + 1, prov, fontsize=9)

# Draw a reference line for Attention TGI = 100
ax.axhline(y=100, color='gray', linestyle='--', linewidth=1, zorder=1)

# Set axis labels
ax.set_xlabel('Search ratio(%)', fontsize=12, labelpad=15)
ax.set_ylabel('Attention(TGI)', fontsize=12, labelpad=15)

# Set the title
ax.set_title('Search ratio and attention (TGI) of users in each province and city for new domestic products', fontsize=14, pad=20)

# Adjust the axis range and ticks
ax.set_xlim(0, 11)
ax.set_ylim(0, 180)
ax.set_xticks([1, 3, 5, 7, 9])  # Strictly match the x - axis ticks of the original image
ax.set_yticks(range(20, 180, 20))

# Set the legend (align the position with the original image)
ax.legend(loc='upper right', bbox_to_anchor=(1, 1), frameon=True, fontsize=10)

# Add a grid
ax.grid(linestyle='--', alpha=0.5, zorder=0)

# Optimize the layout
plt.tight_layout()
plt.show()