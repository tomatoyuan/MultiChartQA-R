import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Data
labels = ["Ice sports", "Folk ice and snow activities", "Ice and snow viewing experiences", "Land ice and snow activities"]
sizes = [27, 37, 25, 11]
# Corresponding colors (try to match the original image and fine - tune according to the actual situation)
colors = ['#4B9CD3', '#FF7F27', '#32CD32', '#FFD700']

fig, ax = plt.subplots(figsize=(8, 6))
# Draw a donut chart, wedgeprops sets the width of the donut
wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%",
                                  startangle=90, wedgeprops={"width": 0.4})

# Add a custom "¥" symbol in the middle of the donut to simulate the effect of the original image
center_circle = Circle((0, 0), 0.3, color='white')
ax.add_artist(center_circle)
ax.text(0, 0, '¥', ha='center', va='center', fontsize=40, color='orange')

# Adjust the size and color of the annotation text (optional) to make the annotation clearer
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_color('black')  # Make the values clearer on the colored blocks

ax.set_title('Consumption proportion of different ice and snow sports during the 2023 - 2024 ice and snow season')

plt.tight_layout()
plt.show()