import matplotlib.pyplot as plt

# Data preparation
labels = ["1-3 times", "4-6 times", "7-9 times", "10 times and above"]
sizes = [41.0, 45.0, 10.0, 4.0]  # Proportion (%)
colors = ["lightpink", "coral", "sandybrown", "brown"]  # Color scheme, similar to the original image

fig, ax = plt.subplots(figsize=(8, 6))

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    sizes, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,  # Adjust the starting angle to make the pie chart distribution more reasonable
    pctdistance=0.8  # Adjust the label position to avoid overlapping with the legend
)

ax.set_title('Distribution of weekly consumption frequency of local life service users in China in 2023', fontsize=14)

# Set the legend (same position and style as the original image)
ax.legend(
    wedges, 
    labels, 
    title="Weekly consumption frequency", 
    loc="center left", 
    bbox_to_anchor=(1, 0.5)
)

# Optimize the label text color (use white text for dark slices and black text for light slices)
for autotext in autotexts:
    autotext.set_color('white' if autotext.get_position()[1] > 0.5 else 'black')

plt.tight_layout()
plt.show()