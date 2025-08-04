import matplotlib.pyplot as plt
import numpy as np

# Define data strictly according to the chart order (keep the original order)
data = [
    {"province": "Guangxi", "region": "Western", "growth": 145},
    {"province": "Ningxia", "region": "Western", "growth": 135},
    {"province": "Inner Mongolia", "region": "Western", "growth": 135},
    {"province": "Tianjin", "region": "Eastern", "growth": 120},
    {"province": "Jiangxi", "region": "Central", "growth": 105},
    {"province": "Liaoning", "region": "Northeastern", "growth": 100},
    {"province": "Jiangsu", "region": "Eastern", "growth": 100},
    {"province": "Hebei", "region": "Eastern", "growth": 90},
    {"province": "Zhejiang", "region": "Eastern", "growth": 85},
    {"province": "Hainan", "region": "Eastern", "growth": 85},
    {"province": "Guizhou", "region": "Western", "growth": 80},
    {"province": "Shanghai", "region": "Eastern", "growth": 75},
    {"province": "Heilongjiang", "region": "Northeastern", "growth": 70},
    {"province": "Guangdong", "region": "Eastern", "growth": 65},
    {"province": "Hubei", "region": "Central", "growth": 60},
    {"province": "Sichuan", "region": "Western", "growth": 55},
    {"province": "Shanxi", "region": "Central", "growth": 45},
    {"province": "Shandong", "region": "Eastern", "growth": 40},
    {"province": "Chongqing", "region": "Western", "growth": 40},
    {"province": "Xinjiang", "region": "Western", "growth": 35},
    {"province": "Beijing", "region": "Eastern", "growth": 30},
    {"province": "Henan", "region": "Central", "growth": 25},
    {"province": "Hunan", "region": "Central", "growth": 20},
    {"province": "Jilin", "region": "Northeastern", "growth": 10}
]

# Extract data
provinces = [item["province"] for item in data]
regions = [item["region"] for item in data]
growths = [item["growth"] for item in data]

# Region - color mapping (strictly match the original image)
region_color = {
    "Eastern": "#4CADDF",  # Blue
    "Central": "#8FC31F",  # Green
    "Western": "#FBBE28",  # Orange
    "Northeastern": "#F26522"  # Red
}
colors = [region_color[reg] for reg in regions]

# Create a canvas
plt.figure(figsize=(8, 10))  # Adjust the canvas size to fit the data

# Create the main x - axis (bottom x - axis)
ax1 = plt.subplot(111)

# Draw a horizontal bar chart (the order of Y - axis data is reversed)
y_pos = np.arange(len(provinces))
bars = ax1.barh(y_pos[::-1], growths, color=colors, height=0.7)

# Set Y - axis labels (province names, keep the original order)
ax1.set_yticks(y_pos)
ax1.set_yticklabels(provinces[::-1], fontsize=10)

# Set the bottom x - axis ticks (percentage format)
ax1.set_xlim(0, 150)
ax1.set_xticks([0, 30, 60, 90, 120, 150])
ax1.set_xticklabels(["0%", "30%", "60%", "90%", "120%", "150%"], fontsize=9)
ax1.set_xlabel("Growth Rate", fontsize=10)

# Create the top x - axis (share the Y - axis with the bottom x - axis)
ax2 = ax1.twiny()
ax2.set_xlim(ax1.get_xlim())  # Ensure the top and bottom x - axes have the same range
ax2.set_xticks([0, 30, 60, 90, 120, 150])
ax2.set_xticklabels(["0%", "30%", "60%", "90%", "120%", "150%"], fontsize=9)

# Add a title
plt.title("Year - on - year growth rate of searches for new domestic products by users in each province in 2020",
          fontsize=12, fontweight="bold", y=1.03)

# Manually build the legend (match the original position and style)
from matplotlib.patches import Patch
legend_patches = [
    Patch(color=region_color["Eastern"], label="Eastern"),
    Patch(color=region_color["Central"], label="Central"),
    Patch(color=region_color["Western"], label="Western"),
    Patch(color=region_color["Northeastern"], label="Northeastern")
]
ax1.legend(handles=legend_patches, bbox_to_anchor=(1, 0.7),
           fontsize=9, frameon=False)

# Adjust the layout (avoid overlapping of legend and content)
plt.subplots_adjust(left=0.3, right=0.8)  # Reserve space on the right for the legend

# Add data labels (correct the order)
for i, bar in enumerate(bars):
    width = bar.get_width()
    ax1.text(width + 2, bar.get_y() + bar.get_height() / 2,
             f"{growths[i]}%",  # Correct the index, directly use i
             ha='left', va='center', fontsize=9)

# Add a note (strictly restore the bottom note)
plt.figtext(0.55, 0.05, "Note: The regional division refers to the four major economic regions in China.",
            ha="center", fontsize=8, color="gray")

# Display the chart
plt.show()