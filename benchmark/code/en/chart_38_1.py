import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

# Data
labels = ['Under 18', '18 - 24', '25 - 29', 'Over 30']
sizes = [35, 48, 13, 4]
# Color settings, as close to the original chart as possible
colors = ['#4CAF50', '#FF9800', '#9E9E9E', '#795548']  

# Create a pie chart
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%',
                                  startangle=90, colors=colors)

# Set font size and other styles to make the display closer to the original chart
for text in texts + autotexts:
    text.set_fontsize(12)

# The following is the general process for adding a middle image. Replace 'your_image_path.png' with the actual image path.
# Assume the image is square and has been processed. This is just an example. You may need to adjust the size, position, etc. in practice.
# image = plt.imread('your_image_path.png')
# image_box = OffsetImage(image, zoom=0.3)  # zoom adjusts the image size
# ab = AnnotationBbox(image_box, (0, 0), frameon=False)
# ax.add_artist(ab)

# Set the chart title
ax.set_title('Age and Type of First-time Contact Lens Wearers', fontsize=14, y=1.05)

# Keep the pie chart circular
ax.axis('equal')

plt.show()