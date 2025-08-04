import matplotlib.pyplot as plt

# Province data
provinces = ["Liaoning", "Jiangsu", "Hubei", "Beijing", "Shandong", "Guangdong", "Zhejiang", "Shanghai", "Sichuan", "Hunan"]
# Corresponding number of gold medals
gold_medals = [36, 29, 26, 22, 22, 22, 16, 15, 14, 14]
# Set the color of the bar chart
bar_color = "#FFD700"  # Gold color, can be adjusted as needed
# Create a bar chart
bars = plt.bar(provinces, gold_medals, color=bar_color)
# Add a title and axis labels, set the font size
plt.title("Top 10 Provinces in Total Olympic Gold Medals from the 23rd to the 30th Olympics", fontsize=14, fontweight='bold')
plt.xlabel("Province", fontsize=12)
plt.ylabel("Number of Gold Medals", fontsize=12)
# Add numerical annotations
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height,
             '%d' % int(height),
             ha='center', va='bottom', fontsize=10)
# Rotate the x - axis tick labels to avoid overlap, adjust the rotation angle according to the actual situation
plt.xticks(rotation=45)
# Display the chart
plt.tight_layout()  # Automatically optimize the layout
plt.show()