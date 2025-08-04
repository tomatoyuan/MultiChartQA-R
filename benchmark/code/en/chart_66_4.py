import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Channel names
channels = ["Tmall", "JD", "Pet Store", "Taobao", "Pet Hospital"]
# Corresponding data (percentage)
data = [27, 27, 19, 17, 10]
# Icon paths, here assume you have corresponding local icon files, need to replace with actual paths
icon_paths = ["tmall_icon.png", "jd_icon.png", "pet_shop_icon.png", "taobao_icon.png", "pet_hospital_icon.png"]
# Color settings, similar to the green and gray in the original image
bar_colors = ["#A4C639", "#A4C639", "#A4C639", "#A4C639", "#A4C639"]
bg_colors = ["#D3D3D3"] * len(channels)

# Create a canvas
fig, ax = plt.subplots(figsize=(8, 5))

# Draw a bar chart, set the overall width, etc.
x = np.arange(len(channels))
bar_width = 0.6
for i in range(len(channels)):
    # Draw a gray background bar
    bg_rect = ax.bar(x[i], 100, bar_width, color=bg_colors[i], edgecolor="white")
    # Draw a colored foreground bar
    bar = ax.bar(x[i], data[i], bar_width, color=bar_colors[i], edgecolor="white")
    # Add data labels
    ax.annotate(f'{data[i]}%',
                xy=(x[i], data[i]),
                xytext=(5, -15),  # Adjust the label position
                textcoords="offset points",
                ha='center', va='bottom',
                color="black")

    # Process icons, here is a simple demonstration, for precise restoration, more detailed adjustments are needed
    try:
        icon = Image.open(icon_paths[i])
        icon = icon.resize((20, 20))  # Adjust the icon size
        fig.canvas.draw()
        ax_image = fig.add_axes([ax.get_xlim()[0] + i * (ax.get_xlim()[1] - ax.get_xlim()[0])/len(channels) - 0.03, 
                                 ax.get_ylim()[0] + 0.01, 0.05, 0.05])  # Icon position
        ax_image.imshow(icon)
        ax_image.axis("off")
    except:
        pass

# Set x-axis ticks and labels
ax.set_xticks(x)
ax.set_xticklabels(channels)
# Hide the y-axis
ax.set_yticks([])
ax.set_ylabel("")
# Set the title
ax.set_title("Top 5 Purchase Channels for Ointments", fontsize=14, fontweight="bold")

# Beautify the chart, hide the top, right, and bottom borders
for spine in ["top", "right", "bottom"]:
    ax.spines[spine].set_visible(False)
    
plt.show()