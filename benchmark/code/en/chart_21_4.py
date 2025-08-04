import matplotlib.pyplot as plt
import numpy as np

# City names
cities = ["Guangzhou", "Beijing", "Shanghai", "Shenzhen", "Hangzhou", "Fuzhou", "Ningbo", "Wenzhou", "Xiamen", "Wuhan"]
# Simulated bar chart data, generally showing height differences, can be fine - tuned according to actual situation
data = [30, 25, 22, 20, 18, 16, 19, 17, 15, 14]

x = np.arange(len(cities))  # x-axis coordinates
width = 0.5  # Bar width

fig, ax = plt.subplots(figsize=(10, 6))  # Create a canvas and axis object, set the figure size
# Draw the bar chart, set the colors to two tones close to the original image, the rgb values can be fine - tuned to be closer
bars1 = ax.bar(x[::2], data[::2], width, color=(209/255, 78/255, 68/255))  # Red - series bars
bars2 = ax.bar(x[1::2], data[1::2], width, color=(255/255, 235/255, 201/255))  # Light beige bars

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=10)  # 倾斜45度并右对齐

# Set the chart title
ax.set_title("Top 10 Popular Departure Cities for Spring Festival Travel", fontsize=14, fontweight='bold')

# Add x-axis label
ax.set_xlabel("City", fontsize=12)
# Add y-axis label and unit
ax.set_ylabel("Travel Heat Index", fontsize=12)

# Hide the top and right axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add numerical labels above each bar
for i, v in enumerate(data):
    ax.text(i, v + 0.5, str(v), ha='center', fontsize=10)

# Use pure drawing methods to create decorative elements instead of images
from matplotlib.patches import Polygon, Circle

# Create a hot air balloon shape
def create_balloon(ax, x, y, scale=1.0):
    # Balloon body
    balloon = Polygon([
        (x, y+15*scale), (x-5*scale, y+5*scale), (x-3*scale, y), 
        (x+3*scale, y), (x+5*scale, y+5*scale), (x, y+15*scale)
    ], fill=True, color=(209/255, 78/255, 68/255))
    ax.add_patch(balloon)
    
    # Basket
    basket = Polygon([
        (x-2*scale, y), (x-3*scale, y-3*scale), 
        (x+3*scale, y-3*scale), (x+2*scale, y)
    ], fill=True, color=(139/255, 69/255, 19/255))
    ax.add_patch(basket)
    
    # Ropes
    ax.plot([x-2*scale, x-2.5*scale], [y, y-1.5*scale], 'k-', linewidth=0.5)
    ax.plot([x+2*scale, x+2.5*scale], [y, y-1.5*scale], 'k-', linewidth=0.5)

# Add a hot air balloon decoration in the upper right corner
create_balloon(ax, 8.5, 32, scale=0.3)

plt.tight_layout()  # Adjust the layout to ensure that the labels are not obscured
plt.show()