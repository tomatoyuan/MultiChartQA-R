import matplotlib.pyplot as plt
import numpy as np

# Categories
labels = ["Both Online and Offline", "Online Channels", "Offline Channels"]
# Proportion of each category (%), the data can be roughly the same
sizes = [75.8, 15.5, 8.7]
# Colors of each part of the pie chart, try to be close to the original image
colors = ["#A4C639", "#87D3F2", "#64B5F6"]

# Create a canvas and a sub - plot
fig, ax = plt.subplots(figsize=(6, 6))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, autopct='%1.1f%%', 
    startangle=140, colors=colors, 
    textprops={'color': 'black'}
)

# Beautify the annotation text (adjust the size, etc.)
for text in texts + autotexts:
    text.set_fontsize(12)

# Simulate the TGI arrow annotation (pointing to the offline channels)
# Find the wedge corresponding to the offline channels
offline_wedge = wedges[2]
# Calculate the annotation position
annotation = ax.annotate(
    'Consumers in Low - tier Cities\nTGI = 208',
    xy=offline_wedge.center,  # Center of the wedge
    xytext=(1.2, 0.8),  # Text position
    arrowprops=dict(
        facecolor='blue', 
        shrink=0.1, 
        width=1, 
        headwidth=5,
        connectionstyle="arc3,rad=0.3"  # Curved arrow
    ),
    ha='center', 
    va='bottom',
    color='blue', 
    fontsize=10
)

# Set the title
ax.set_title("Proportion of Purchase Channels for Chinese Baby Diaper Products in 2022", fontsize=14, fontweight="bold", y=1.05)

plt.tight_layout()  # Automatically adjust the layout
plt.show()